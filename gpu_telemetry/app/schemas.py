from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime

class GPUBase(BaseModel):
    name: str
    model: str
    serial_number: str

class GPUCreate(GPUBase):
    pass

class GPU(GPUBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class GPUTelemetryBase(BaseModel):
    temperature: float = Field(..., ge=0, le=100)
    power_usage: float = Field(..., ge=0)
    memory_usage: float = Field(..., ge=0)
    memory_total: float = Field(..., ge=0)
    gpu_utilization: float = Field(..., ge=0, le=100)
    fan_speed: float = Field(..., ge=0, le=100)
    clock_speed: float = Field(..., ge=0)
    voltage: float = Field(..., ge=0)
    pcie_throughput: float = Field(..., ge=0)
    additional_metrics: Optional[Dict] = None

class GPUTelemetryCreate(GPUTelemetryBase):
    gpu_id: int

class GPUTelemetry(GPUTelemetryBase):
    id: int
    gpu_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class GPUTelemetryResponse(BaseModel):
    gpu_id: int
    timestamp: datetime
    metrics: Dict[str, float]
    additional_metrics: Optional[Dict] = None

class GPUTelemetryStats(BaseModel):
    gpu_id: int
    avg_temperature: float
    max_temperature: float
    avg_power_usage: float
    max_power_usage: float
    avg_memory_usage: float
    max_memory_usage: float
    avg_gpu_utilization: float
    max_gpu_utilization: float
    time_range: str 