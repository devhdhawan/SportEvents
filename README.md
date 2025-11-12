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

```
/sports-event
│
├── src/
│   ├── producer/           # Kafka producer scripts simulating live data
│   ├── consumer/           # Kafka consumer scripts processing streams
│   ├── cache/              # Redis cache management code
│   ├── web/                # Frontend and backend API server code
│
├── docs/                   # Diagrams, architecture, deployment guide
├── tests/                  # Unit and integration tests
├── Dockerfile              # Docker container definitions
├── docker-compose.yml      # Docker Compose orchestration file
├── README.md               # Project overview and setup
└── requirements.txt        # Python dependencies
```

/sports-event
│
├── src/
│   ├── Producer.py           # Kafka producer scripts simulating live data
│   ├── Consumer.py          # Kafka consumer scripts processing streams
│   ├── KafkaClientFactory.py   # Creating Objects for Producer, Consumer and Redis
│   ├── index.html             # Frontend and backend API server code
│
├── docs/                   # Diagrams, architecture, deployment guide
├── tests/                  # Unit and integration tests
├── Dockerfile              # Docker container definitions
├── docker-compose.yml      # Docker Compose orchestration file
├── README.md               # Project overview and setup
└── requirements.txt        # Python dependencies
```