from sqlalchemy import Column, Integer, String, Float
from database import Base

# GPU Telemetry Data Model
class GPUMetrics(Base):
    __tablename__ = "gpu_metrics"

    id = Column(Integer, primary_key=True, index=True)
    gpu_name = Column(String, index=True)
    temperature = Column(Float)
    usage = Column(Float)
    memory_used = Column(Float)
    memory_total = Column(Float)
    timestamp = Column(String)  # Store timestamp as string for simplicity
