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
│   ├── kafka/
│   │   ├── Producer.py
│   │   ├── Consumer.py
│   │   ├── KafkaClientFactory.py
│   ├── web/
│   │   └── index.html
|   |   └── app.py
├── docs/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

