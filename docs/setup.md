# BioMCP-Hub Setup Guide

🚀 **Installation & Deployment Guide for BioMCP-Hub**

## 📌 Prerequisites
Before installing BioMCP-Hub, ensure you have the following dependencies installed:

- Python 3.8+
- pip package manager
- Docker (if using containerized deployment)
- PostgreSQL or MongoDB (for structured metadata storage, optional)

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/BioMCP-Hub.git
cd BioMCP-Hub
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables (Optional)
Create a `.env` file to configure database connections and API keys (if applicable):
```sh
DB_URL=postgresql://user:password@localhost/biomcp
PUBMED_API_KEY=your_api_key
```

## 🚀 Running the MCP Hub
```sh
python api/hub.py
```

## 📡 Running MCP Modules
To start a specific module, navigate to its directory and run:

**Genome Analysis Module**:
```sh
python modules/genome_analysis/server.py
```

**Sequence Alignment Module**:
```sh
python modules/sequence_alignment/server.py
```

**Data Search Module** (Example: PubMed search):
```sh
python modules/data_search/pubmed_search.py --query "CRISPR gene editing"
```

## 🐳 Docker Deployment

### 1️⃣ Build the Docker Image
```sh
docker build -t biomcp-hub .
```

### 2️⃣ Run the Container
```sh
docker run -d -p 5000:5000 --name biomcp biomcp-hub
```

### 3️⃣ Using Docker Compose (Recommended)
```sh
docker-compose up -d
```

## ☁️ Kubernetes Deployment (Optional)
If deploying on Kubernetes, use the provided `k8s/biomcp-hub.yaml` manifest:
```sh
kubectl apply -f k8s/biomcp-hub.yaml
```

## 🎯 Next Steps
- ✅ Customize modules in `modules/`
- ✅ Integrate with databases for persistent storage
- ✅ Add authentication & role-based access control (RBAC)

---
This document provides step-by-step instructions for setting up and deploying BioMCP-Hub. For advanced configurations, refer to **[architecture.md](architecture.md)**.
