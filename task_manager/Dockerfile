FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create SSL directory and set permissions
RUN mkdir -p /app/ssl && \
    chmod 755 /app/ssl

# Make the certificate generation script executable
RUN chmod +x /app/generate_cert.sh

# Generate SSL certificates and set permissions
RUN /app/generate_cert.sh && \
    chmod 600 /app/ssl/private.key && \
    chmod 644 /app/ssl/certificate.crt

EXPOSE 8443

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8443", "--ssl-keyfile", "/app/ssl/private.key", "--ssl-certfile", "/app/ssl/certificate.crt"]