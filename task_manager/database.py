from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy motorunu oluşturuyoruz
engine = create_engine(SQLALCHEMY_DATABASE_URL)

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