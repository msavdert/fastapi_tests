# 🚀 GPU Metrics API

A FastAPI-based API to collect, store, and visualize GPU telemetry data using **PostgreSQL** and **Grafana**.

## 📖 Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Setup & Installation](#setup--installation)
- [Deployment with Docker Compose](#deployment-with-docker-compose)
- [Deployment with Ansible](#deployment-with-ansible)
- [API Endpoints](#api-endpoints)
- [Roadmap](#roadmap)
- [License](#license)

## 📌 Overview
**GPU Metrics API** collects and stores GPU performance telemetry, making it available through a REST API. The stored data is visualized using **Grafana**, and the system is designed to be scalable and easily deployable via **Docker Compose** or **Ansible**.

This project simulates **real-world database API implementations** at companies like NVIDIA.


## 🏗 Architecture
```
+------------+        +------------+        +------------+
|   Client   | -----> |   FastAPI  | -----> | PostgreSQL |
+------------+        +------------+        +------------+
                                |               
                                v              
                        +----------------+    
                        |   Grafana UI   |    
                        +----------------+    
```


## 🛠 Technologies Used
- **FastAPI** - High-performance Python web framework
- **PostgreSQL** - Database for storing telemetry data
- **Grafana** - Dashboard for visualizing collected metrics
- **Docker & Docker Compose** - Containerized environment
- **Ansible** - Automated deployment & server provisioning


## 🚀 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/gpu-metrics-api.git
cd gpu-metrics-api
```

### 2️⃣ Install Dependencies
```bash
cd api
pip install -r requirements.txt
```

### 3️⃣ Run FastAPI Locally
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: [http://localhost:8000/docs](http://localhost:8000/docs)


## 🐳 Deployment with Docker Compose
### 1️⃣ Start Services
```bash
docker-compose up -d
```

### 2️⃣ Stop Services
```bash
docker-compose down
```


## 🤖 Deployment with Ansible
1️⃣ **Update Inventory File (`hosts.ini`)**
```ini
[gpu_server]
192.168.1.100 ansible_user=root
```

2️⃣ **Run Ansible Playbook**
```bash
ansible-playbook -i hosts.ini deploy.yml
```


## 🔗 API Endpoints
| Method | Endpoint          | Description                     |
|--------|------------------|---------------------------------|
| GET    | `/metrics`       | Fetch GPU telemetry data       |
| POST   | `/metrics`       | Submit new GPU metrics         |
| GET    | `/metrics/{id}`  | Get details of a specific entry |

Full API documentation is available at: [http://localhost:8000/docs](http://localhost:8000/docs)


## 🛤 Roadmap
### 🔹 1️⃣ Define Requirements & Architecture
- Identify project scope and objectives.
- Choose FastAPI + PostgreSQL for performance and scalability.

### 🔹 2️⃣ Develop FastAPI Backend
- Implement API endpoints.
- Create database schema in PostgreSQL.

### 🔹 3️⃣ Set Up Docker & Containerize Services
- Write `Dockerfile` and `docker-compose.yml`.
- Test deployment locally.

### 🔹 4️⃣ Automate Deployment with Ansible
- Create playbooks for installation and deployment.
- Deploy on a remote server.

### 🔹 5️⃣ Integrate Grafana for Visualization
- Configure dashboards to monitor GPU performance.


## 📜 License
This project is licensed under the MIT License.