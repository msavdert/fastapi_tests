import requests
import random
import time
import json
from datetime import datetime
import os

# API endpoint from environment variable
API_URL = os.getenv("API_URL", "http://localhost:8000")

def generate_random_telemetry():
    """Generate random GPU telemetry data"""
    return {
        "temperature": round(random.uniform(30, 85), 2),
        "power_usage": round(random.uniform(50, 300), 2),
        "memory_usage": round(random.uniform(1000, 8000), 2),
        "memory_total": 8192,  # 8GB GPU
        "gpu_utilization": round(random.uniform(0, 100), 2),
        "fan_speed": round(random.uniform(0, 100), 2),
        "clock_speed": round(random.uniform(1000, 2000), 2),
        "voltage": round(random.uniform(0.8, 1.2), 2),
        "pcie_throughput": round(random.uniform(0, 5000), 2),
        "additional_metrics": {
            "compute_utilization": round(random.uniform(0, 100), 2),
            "memory_bandwidth": round(random.uniform(0, 500), 2),
            "pcie_bandwidth": round(random.uniform(0, 1000), 2)
        }
    }

def create_gpu():
    """Create a new GPU in the system"""
    gpu_data = {
        "name": f"GPU-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "model": "NVIDIA GeForce RTX 3080",
        "serial_number": f"SN-{random.randint(1000000, 9999999)}"
    }
    
    response = requests.post(f"{API_URL}/gpus/", json=gpu_data)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print(f"Error creating GPU: {response.text}")
        return None

def send_telemetry(gpu_id):
    """Send telemetry data for a specific GPU"""
    telemetry_data = generate_random_telemetry()
    telemetry_data["gpu_id"] = gpu_id
    
    response = requests.post(f"{API_URL}/telemetry/", json=telemetry_data)
    if response.status_code == 200:
        print(f"Sent telemetry data for GPU {gpu_id}: {json.dumps(telemetry_data, indent=2)}")
    else:
        print(f"Error sending telemetry: {response.text}")

def main():
    # Create a GPU
    gpu_id = create_gpu()
    if not gpu_id:
        print("Failed to create GPU. Exiting...")
        return
    
    print(f"Created GPU with ID: {gpu_id}")
    
    # Send telemetry data every second
    try:
        while True:
            send_telemetry(gpu_id)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping telemetry simulation...")

if __name__ == "__main__":
    main() 