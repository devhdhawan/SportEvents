# Sport Live Event App

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
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── kubernetes_docs.md
├── LICENSE
├── README.md
├── requirements.txt
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
```

