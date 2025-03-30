from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GPU(Base):
    __tablename__ = "gpus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    model = Column(String)
    serial_number = Column(String, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    telemetry_data = relationship("GPUTelemetry", back_populates="gpu")

class GPUTelemetry(Base):
    __tablename__ = "gpu_telemetry"

    id = Column(Integer, primary_key=True, index=True)
    gpu_id = Column(Integer, ForeignKey("gpus.id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Performance metrics
    temperature = Column(Float)
    power_usage = Column(Float)  # in watts
    memory_usage = Column(Float)  # in MB
    memory_total = Column(Float)  # in MB
    gpu_utilization = Column(Float)  # percentage
    fan_speed = Column(Float)  # percentage
    
    # Additional metrics
    clock_speed = Column(Float)  # in MHz
    voltage = Column(Float)  # in volts
    pcie_throughput = Column(Float)  # in MB/s
    additional_metrics = Column(JSON)  # for any other metrics
    
    # Relationships
    gpu = relationship("GPU", back_populates="telemetry_data") 