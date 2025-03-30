from fastapi import FastAPI
import models
from database import engine
from routes import router

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# API rotalarını ekleyelim
app.include_router(router)