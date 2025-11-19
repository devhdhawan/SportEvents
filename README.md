# Sport Events- Real-Time Sports Event Streaming System:

## Overview
This project simulates a real-time sports event streaming application similar to Cricbuzz. It leverages Apache Kafka for event streaming, Redis for caching, and WebSocket-based frontend updates. The goal is to provide live score updates and player stats for different sports using locally simulated data inputs.

## Features
- Real-time live score streaming for multiple sports events
- Kafka-based event producer simulation for score and player data
- Backend Kafka consumer to process and push updates to clients
- Redis caching layer for high read performance
- WebSocket-based frontend for dynamic live updates
- Local Docker containerization for easy deployment and development

## 🖼️ Project Architecture
```
text
flowchart TD
    A[⚡ Score Producer (Kafka)] -->|Publishes Events| B[(Kafka Broker)]
    B -->|Consumes Events| C[⚙️ Backend Consumer]
    C -->|Updates| D[🗃️ Redis Cache]
    C -->|Broadcasts| E[🔗 WebSocket Server]
    E -->|Delivers Live Data| F[💻 Web Frontend]
Producer: Simulates live sports data and feeds it to Kafka.
Consumer: Processes streams, updates Redis cache, and notifies the frontend.
WebSocket Server: Pushes real-time updates to the browser.
Frontend: Receives instant live scores and stats.
```


## 📁 Directory Structure
```
.
├── docs/
├── k8s/
│   ├── consumer.yaml
│   ├── frontend.yaml
│   ├── kafka.yaml
│   ├── producer.yaml
│   ├── redis.yaml
│   └── zookeeper.yaml
├── public/
│   └── index.html
├── src/
│   ├── Consumer/
│   │   ├── Consumer.py
│   │   └── Dockerfile
│   ├── KafkaFiles/
│   │   ├── __init__.py
│   │   ├── Dockerfile
│   │   ├── KafkaClientFactory.py
│   │   └── Producer.py
│   └── web/
│       ├── app.py
│       ├── Dockerfile
│       └── index.html
└── tests/
│── .gitignore
├── docker-compose.yml
├── Dockerfile
├── kubernetes_docs.md
├── LICENSE
├── README.md
├── requirements.txt
```

## 🛠️ Tech Stack
- Python – Backend & event simulation
- Apache Kafka – High-performance event messaging
- Redis – In-memory caching
- WebSockets – Real-time data push to the frontend
- Docker & Docker Compose – Containerization and orchestration
- Kubernetes – Ready for scalable deployments
- HTML/CSS/JavaScript – Frontend interface

## ⚡ Quick Start
1. Clone the Repository
    - bash
    - git clone https://github.com/devhdhawan/system_design.git
    - cd SPORTEVENTS
2. Spin Up Services (Docker)
    - bash
    - docker-compose up --build
    - This launches Kafka, Redis, backend, and frontend as containers.
3. Access the Live App
    - Open http://localhost:5000 (or your configured port)

## 🏗️ Manual Setup (No Docker)
- Install Python dependencies:
    - bash
    - pip install -r requirements.txt
    - Ensure Kafka and Redis are running locally.
    - Run Kafka producer and consumer scripts in src/kafka/.
    - Start the backend (src/web/app.py) and serve the frontend (src/web/index.html).

## 📊 Usage Example
- Simulate Events:
    - Run Producer.py to start pushing random scores/events.
- Process & Push Events:
    - Consumer.py reads from Kafka, updates Redis, and pushes to the UI.
- See the Live Feed:
    - Open the web UI to watch real-time updates for various sports.
- 🧩 Extend & Customize
    - Add new sports/events by writing additional producers/consumers.
    Plug into real sports APIs by replacing or extending the simulation logic.
    Scale in production via Kubernetes with manifests in /k8s/.

## 🤝 Contributing
- Fork & clone this repository
- Create a feature branch (git checkout -b feature/my-feature)
- Commit and push your work
- Open a Pull Request describing your changes
- Contact: For questions, suggestions, or collaboration, open an issue or - reach out on GitHub!
- Enjoy building and learning with the Sport Live Event App!

