from pydantic import BaseModel, EmailStr, Field, validator, constr
from typing import Optional
from datetime import datetime
import re

# Görev (Task) için temel veri şeması
class TaskBase(BaseModel):
    title: constr(min_length=1, max_length=100, strip_whitespace=True) = Field(..., description="Task title")
    description: Optional[constr(max_length=500, strip_whitespace=True)] = Field(None, description="Task description")

    @validator('title')
    def validate_title(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty or just whitespace')
        return v.strip()

    @validator('description')
    def validate_description(cls, v):
        if v and len(v.strip()) > 500:
            raise ValueError('Description cannot exceed 500 characters')
        return v.strip() if v else v

# Yeni görev oluştururken kullanılacak şema
class TaskCreate(TaskBase):
    pass

# API'nin döndüreceği görev verisi
class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    completed: bool
    owner_id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    username: constr(min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_-]+$', strip_whitespace=True) = Field(..., description="Username (alphanumeric, underscore, and hyphen only)")

    @validator('username')
    def validate_username(cls, v):
        if not v.strip():
            raise ValueError('Username cannot be empty or just whitespace')
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('Username can only contain letters, numbers, underscores, and hyphens')
        return v.strip()

class UserCreate(UserBase):
    password: constr(min_length=8, max_length=100) = Field(..., description="Password (8-100 characters)")

    @validator('password')
    def validate_password(cls, v):
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one number')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        return v

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None