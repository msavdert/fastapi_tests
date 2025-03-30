import requests
import random
import time
import json
from datetime import datetime
import os

# API endpoint from environment variable
API_URL = os.getenv("API_URL", "http://localhost:8000")

# GPU specifications
GPU_MODELS = [
    {
        "name": "NVIDIA GeForce RTX 4090",
        "model": "RTX 4090",
        "memory_total": 24576,  # 24GB
        "max_power": 450,  # Watts
        "max_temp": 88,  # Celsius
        "base_clock": 2235,  # MHz
        "boost_clock": 2520,  # MHz
    },
    {
        "name": "NVIDIA GeForce RTX 3080",
        "model": "RTX 3080",
        "memory_total": 10240,  # 10GB
        "max_power": 320,  # Watts
        "max_temp": 93,  # Celsius
        "base_clock": 1440,  # MHz
        "boost_clock": 1710,  # MHz
    },
    {
        "name": "NVIDIA GeForce RTX 3060",
        "model": "RTX 3060",
        "memory_total": 12288,  # 12GB
        "max_power": 170,  # Watts
        "max_temp": 83,  # Celsius
        "base_clock": 1320,  # MHz
        "boost_clock": 1777,  # MHz
    }
]

def generate_random_telemetry(gpu_specs):
    """Generate random GPU telemetry data based on GPU specifications"""
    return {
        "temperature": round(random.uniform(30, gpu_specs["max_temp"]), 2),
        "power_usage": round(random.uniform(50, gpu_specs["max_power"]), 2),
        "memory_usage": round(random.uniform(1000, gpu_specs["memory_total"]), 2),
        "memory_total": gpu_specs["memory_total"],
        "gpu_utilization": round(random.uniform(0, 100), 2),
        "fan_speed": round(random.uniform(0, 100), 2),
        "clock_speed": round(random.uniform(gpu_specs["base_clock"], gpu_specs["boost_clock"]), 2),
        "voltage": round(random.uniform(0.8, 1.2), 2),
        "pcie_throughput": round(random.uniform(0, 5000), 2),
        "additional_metrics": {
            "compute_utilization": round(random.uniform(0, 100), 2),
            "memory_bandwidth": round(random.uniform(0, 500), 2),
            "pcie_bandwidth": round(random.uniform(0, 1000), 2)
        }
    }

def create_gpu(gpu_specs):
    """Create a new GPU in the system"""
    gpu_data = {
        "name": f"{gpu_specs['name']}-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "model": gpu_specs["model"],
        "serial_number": f"SN-{random.randint(1000000, 9999999)}"
    }
    
    response = requests.post(f"{API_URL}/gpus/", json=gpu_data)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print(f"Error creating GPU: {response.text}")
        return None

def send_telemetry(gpu_id, gpu_specs):
    """Send telemetry data for a specific GPU"""
    telemetry_data = generate_random_telemetry(gpu_specs)
    telemetry_data["gpu_id"] = gpu_id
    
    response = requests.post(f"{API_URL}/telemetry/", json=telemetry_data)
    if response.status_code == 200:
        print(f"Sent telemetry data for GPU {gpu_id} ({gpu_specs['name']}): {json.dumps(telemetry_data, indent=2)}")
    else:
        print(f"Error sending telemetry: {response.text}")

def main():
    # Create GPUs
    gpu_ids = []
    for gpu_specs in GPU_MODELS:
        gpu_id = create_gpu(gpu_specs)
        if gpu_id:
            gpu_ids.append((gpu_id, gpu_specs))
            print(f"Created GPU with ID: {gpu_id} ({gpu_specs['name']})")
        else:
            print(f"Failed to create GPU: {gpu_specs['name']}")
    
    if not gpu_ids:
        print("No GPUs were created. Exiting...")
        return
    
    # Send telemetry data every second for each GPU
    try:
        while True:
            for gpu_id, gpu_specs in gpu_ids:
                send_telemetry(gpu_id, gpu_specs)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping telemetry simulation...")

if __name__ == "__main__":
    main() 