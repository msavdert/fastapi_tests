# GPU Telemetry and Performance Management System

A comprehensive system for collecting, monitoring, and analyzing GPU performance metrics. Built with FastAPI, PostgreSQL, Prometheus, and Grafana.

## Features

- 🔍 Real-time GPU performance monitoring
- 📊 Detailed metric collection and analysis
- 📈 Visualization with Grafana
- 🔄 Prometheus integration
- 🗄️ PostgreSQL database support
- 🐳 Docker and Docker Compose support
- 📝 Swagger API documentation

## Collected Metrics

- Temperature (°C)
- Power consumption (W)
- Memory usage (MB)
- GPU utilization (%)
- Fan speed (%)
- Clock speed (MHz)
- Voltage (V)
- PCIe throughput (MB/s)
- Additional metrics (compute utilization, memory bandwidth, etc.)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd gpu_telemetry
```

2. Start Docker containers:
```bash
docker-compose up --build
```

3. Services will be available at:
- FastAPI: http://localhost:8000
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- PostgreSQL: localhost:5432

## API Endpoints

### GPU Operations
- `POST /gpus/` - Add new GPU
- `GET /gpus/` - List all GPUs
- `GET /gpus/{gpu_id}` - Get specific GPU

### Telemetry Operations
- `POST /telemetry/` - Send GPU telemetry data
- `GET /telemetry/{gpu_id}` - Get telemetry data for specific GPU
- `GET /telemetry/{gpu_id}/stats` - Get GPU statistics

## Simulation

The project includes a simulator service that generates random GPU telemetry data. It runs automatically when you start the containers with `docker-compose up`.

To run the simulator manually:
```bash
python scripts/simulate_gpu.py
```

## Grafana Dashboard

Access Grafana:
1. Navigate to http://localhost:3000
2. Default credentials:
   - Username: admin
   - Password: admin
3. The Prometheus data source is automatically configured
4. A sample dashboard for GPU metrics is automatically imported

The dashboard includes:
- GPU Temperature
- Power Usage
- Memory Usage
- GPU Utilization

## Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the database:
```bash
docker-compose up db -d
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## Prometheus Metrics

The following metrics are collected in Prometheus:
- `gpu_temperature` - GPU temperature
- `gpu_power_usage` - Power consumption
- `gpu_memory_usage` - Memory usage
- `gpu_utilization` - GPU utilization
- `telemetry_requests_total` - Total telemetry requests

## Architecture

The system consists of several components:
1. FastAPI Application: Handles API requests and data processing
2. PostgreSQL Database: Stores GPU and telemetry data
3. Prometheus: Collects and stores time-series metrics
4. Grafana: Visualizes metrics and provides dashboards
5. Simulator Service: Generates test data

## Security

- All API endpoints are accessible over HTTPS
- Database credentials are managed through environment variables
- Prometheus and Grafana run behind a firewall
- Rate limiting is implemented on API endpoints

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 