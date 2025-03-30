from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routes import router
from rate_limit import limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=engine)

# app = FastAPI() 
app = FastAPI(debug=True)  # Debug mode'u aktif ediyoruz

# Configure CORS
origins = [
    "http://localhost",  # Local development
    "http://localhost:3000",  # React default port
    "http://localhost:8000",  # FastAPI default port
    "http://localhost:8080",  # Common development port
    "https://your-production-domain.com",  # Production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"],  # Exposes all headers
    max_age=3600,  # Cache preflight requests for 1 hour
)

# Add rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# API rotalarını ekleyelim
app.include_router(router)