from pydantic import BaseModel

# Görev (Task) için temel veri şeması
class TaskBase(BaseModel):
    title: str
    description: str | None = None

# Yeni görev oluştururken kullanılacak şema
class TaskCreate(TaskBase):
    pass

# API'nin döndüreceği görev verisi
class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True