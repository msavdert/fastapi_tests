from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge
import time

from . import models, schemas
from .database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GPU Telemetry API",
    description="API for collecting and monitoring GPU performance metrics",
    version="1.0.0"
)

# Initialize Prometheus metrics
gpu_temperature = Gauge('gpu_temperature', 'GPU temperature in Celsius')
gpu_power_usage = Gauge('gpu_power_usage', 'GPU power usage in watts')
gpu_memory_usage = Gauge('gpu_memory_usage', 'GPU memory usage in MB')
gpu_utilization = Gauge('gpu_utilization', 'GPU utilization percentage')
telemetry_requests = Counter('telemetry_requests_total', 'Total number of telemetry requests')

# Initialize Prometheus instrumentator
Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    return {"message": "Welcome to GPU Telemetry API"}

@app.post("/gpus/", response_model=schemas.GPU)
def create_gpu(gpu: schemas.GPUCreate, db: Session = Depends(get_db)):
    db_gpu = models.GPU(**gpu.dict())
    db.add(db_gpu)
    db.commit()
    db.refresh(db_gpu)
    return db_gpu

@app.get("/gpus/", response_model=list[schemas.GPU])
def read_gpus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gpus = db.query(models.GPU).offset(skip).limit(limit).all()
    return gpus

@app.get("/gpus/{gpu_id}", response_model=schemas.GPU)
def read_gpu(gpu_id: int, db: Session = Depends(get_db)):
    gpu = db.query(models.GPU).filter(models.GPU.id == gpu_id).first()
    if gpu is None:
        raise HTTPException(status_code=404, detail="GPU not found")
    return gpu

@app.post("/telemetry/", response_model=schemas.GPUTelemetry)
def create_telemetry(telemetry: schemas.GPUTelemetryCreate, db: Session = Depends(get_db)):
    # Update Prometheus metrics
    gpu_temperature.set(telemetry.temperature)
    gpu_power_usage.set(telemetry.power_usage)
    gpu_memory_usage.set(telemetry.memory_usage)
    gpu_utilization.set(telemetry.gpu_utilization)
    telemetry_requests.inc()

    db_telemetry = models.GPUTelemetry(**telemetry.dict())
    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    return db_telemetry

@app.get("/telemetry/{gpu_id}", response_model=list[schemas.GPUTelemetry])
def read_telemetry(
    gpu_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    telemetry = db.query(models.GPUTelemetry)\
        .filter(models.GPUTelemetry.gpu_id == gpu_id)\
        .offset(skip)\
        .limit(limit)\
        .all()
    return telemetry

@app.get("/telemetry/{gpu_id}/stats", response_model=schemas.GPUTelemetryStats)
def get_telemetry_stats(
    gpu_id: int,
    time_range: str = "1h",
    db: Session = Depends(get_db)
):
    # Calculate time range
    end_time = time.time()
    if time_range == "1h":
        start_time = end_time - 3600
    elif time_range == "1d":
        start_time = end_time - 86400
    elif time_range == "1w":
        start_time = end_time - 604800
    else:
        raise HTTPException(status_code=400, detail="Invalid time range")

    # Query telemetry data
    telemetry_data = db.query(models.GPUTelemetry)\
        .filter(
            models.GPUTelemetry.gpu_id == gpu_id,
            models.GPUTelemetry.timestamp >= start_time,
            models.GPUTelemetry.timestamp <= end_time
        )\
        .all()

    if not telemetry_data:
        raise HTTPException(status_code=404, detail="No telemetry data found for the specified time range")

    # Calculate statistics
    stats = {
        "gpu_id": gpu_id,
        "avg_temperature": sum(t.temperature for t in telemetry_data) / len(telemetry_data),
        "max_temperature": max(t.temperature for t in telemetry_data),
        "avg_power_usage": sum(t.power_usage for t in telemetry_data) / len(telemetry_data),
        "max_power_usage": max(t.power_usage for t in telemetry_data),
        "avg_memory_usage": sum(t.memory_usage for t in telemetry_data) / len(telemetry_data),
        "max_memory_usage": max(t.memory_usage for t in telemetry_data),
        "avg_gpu_utilization": sum(t.gpu_utilization for t in telemetry_data) / len(telemetry_data),
        "max_gpu_utilization": max(t.gpu_utilization for t in telemetry_data),
        "time_range": time_range
    }

    return stats 