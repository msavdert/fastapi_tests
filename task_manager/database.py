from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# .env dosyasını yükleyelim
load_dotenv()

# PostgreSQL bağlantı URL'si
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/task_db")

# SQLAlchemy motorunu oluşturuyoruz
engine = create_engine(DATABASE_URL)

# Oturum (session) oluşturmak için sessionmaker kullanıyoruz
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy Base sınıfı
Base = declarative_base()

# Veritabanı bağlantısını yönetecek fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()