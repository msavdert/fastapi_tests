from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import GPUMetrics
from database import get_db
from pydantic import BaseModel
from datetime import datetime

# API Router
router = APIRouter()

# Pydantic Schema for data validation
class GPUMetricsCreate(BaseModel):
    gpu_name: str
    temperature: float
    usage: float
    memory_used: float
    memory_total: float
    timestamp: str

# Get all GPU metrics
@router.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):
    return db.query(GPUMetrics).all()

# Get GPU metrics by ID
@router.get("/metrics/{metric_id}")
def get_metric(metric_id: int, db: Session = Depends(get_db)):
    metric = db.query(GPUMetrics).filter(GPUMetrics.id == metric_id).first()
    if metric is None:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric

# Post new GPU metrics
@router.post("/metrics")
def create_metric(metric: GPUMetricsCreate, db: Session = Depends(get_db)):
    db_metric = GPUMetrics(
        gpu_name=metric.gpu_name,
        temperature=metric.temperature,
        usage=metric.usage,
        memory_used=metric.memory_used,
        memory_total=metric.memory_total,
        timestamp=metric.timestamp,
    )
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric
