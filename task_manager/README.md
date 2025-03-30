# Task Manager API

Bu proje, FastAPI kullanılarak geliştirilmiş güvenli ve ölçeklenebilir bir Task Manager API'sidir. JWT tabanlı kimlik doğrulama, rate limiting, HTTPS desteği ve güçlü input validasyonu içerir.

## Özellikler

- 🔐 JWT tabanlı kimlik doğrulama ve yetkilendirme
- 🛡️ HTTPS desteği
- ⚡ Rate limiting
- 🔍 Input validasyonu
- 🗄️ PostgreSQL veritabanı
- 🐳 Docker ve Docker Compose desteği
- 🔄 CORS yapılandırması
- 📝 API dokümantasyonu (Swagger UI)

## Gereksinimler

- Docker
- Docker Compose
- OpenSSL (SSL sertifikaları için)

## Kurulum

1. Projeyi klonlayın:
```bash
git clone <repository-url>
cd task_manager
```

2. SSL sertifikalarını oluşturun:
```bash
chmod +x generate_cert.sh
./generate_cert.sh
```

3. Docker container'larını başlatın:
```bash
docker-compose up --build
```

## API Endpoints

### Kimlik Doğrulama
- `POST /register` - Yeni kullanıcı kaydı
- `POST /token` - JWT token alma

### Task İşlemleri
- `GET /tasks/` - Tüm taskları listele
- `POST /tasks/` - Yeni task oluştur
- `GET /tasks/{task_id}` - Belirli bir taskı getir
- `PUT /tasks/{task_id}` - Task güncelle
- `DELETE /tasks/{task_id}` - Task sil
- `PATCH /tasks/{task_id}/toggle-completion` - Task tamamlama durumunu değiştir

## Güvenlik Özellikleri

- JWT tabanlı kimlik doğrulama
- HTTPS zorunluluğu
- Rate limiting
- Güçlü şifre politikası
- Input validasyonu
- CORS yapılandırması

## Rate Limiting Kuralları

- Kimlik doğrulama endpointleri: 5 istek/dakika
- Task endpointleri: 30 istek/dakika
- Genel endpointler: 100 istek/dakika

## Veritabanı Şeması

### User Tablosu
- id (Primary Key)
- email (Unique)
- username (Unique)
- hashed_password
- is_active
- created_at

### Task Tablosu
- id (Primary Key)
- title
- description
- completed
- owner_id (Foreign Key)
- created_at
- updated_at

## Ortam Değişkenleri

`.env` dosyasında aşağıdaki değişkenleri yapılandırın:

```env
# Database Configuration
DATABASE_URL=postgresql://postgres:postgres@db:5432/taskdb

# JWT Configuration
SECRET_KEY=your-super-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API Configuration
API_V1_PREFIX=/api/v1
ENVIRONMENT=development

# Rate Limiting
RATE_LIMIT_PER_MINUTE=30
AUTH_RATE_LIMIT_PER_MINUTE=5

# HTTPS Configuration
HTTPS_ENABLED=true
SSL_KEYFILE=/app/ssl/private.key
SSL_CERTFILE=/app/ssl/certificate.crt
```

## API Kullanım Örnekleri

### Kullanıcı Kaydı
```bash
curl -k -X POST "https://localhost:8443/register" \
-H "Content-Type: application/json" \
-d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "Test123!@#"
}'
```

### Token Alma
```bash
curl -k -X POST "https://localhost:8443/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=testuser&password=Test123\!\@\#"
```

### Task Oluşturma
```bash
curl -k -X POST "https://localhost:8443/tasks/" \
-H "Authorization: Bearer YOUR_TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "title": "Test Task",
    "description": "This is a test task"
}'
```

## Geliştirme

1. Geliştirme ortamını hazırlayın:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2. Veritabanını oluşturun:
```bash
docker-compose up db -d
```

3. Uygulamayı çalıştırın:
```bash
uvicorn main:app --reload --ssl-keyfile ssl/private.key --ssl-certfile ssl/certificate.crt
```

## Test

API'yi test etmek için `test_cors.html` dosyasını kullanabilirsiniz:
```bash
python -m http.server 8000
```
Sonra tarayıcınızda `http://localhost:8000/test_cors.html` adresine gidin.

## Güvenlik Tavsiyeleri

1. Production ortamında güçlü bir SECRET_KEY kullanın
2. SSL sertifikalarını güvenli bir şekilde yönetin
3. Rate limiting kurallarını ortamınıza göre ayarlayın
4. Veritabanı şifrelerini güvenli bir şekilde saklayın
5. CORS politikalarını sıkılaştırın

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. 