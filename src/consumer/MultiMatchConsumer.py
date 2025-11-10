from kafka import KafkaConsumer
from flask_socketio import SocketIO, emit
from flask import Flask, send_from_directory
from flask import jsonify
import json
import redis
import time
import threading
import os

# Path to the web directory
WEB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'web'))

redis_client = redis.Redis(host = "localhost",port="6379",db=0)
app = Flask(__name__)
socketio = SocketIO(app=app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print("Frontend client connected to WebSocket.")

consumer = KafkaConsumer(
    "CricketEvent",
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def consume_event():
    print("Consumer thread started, waiting for messages...")
    try:
        for message in consumer:
            event = message.value
            match_id = event.get('match_id')
            print(f"Received event: {event}")

            # Cache event in Redis
            redis_key = f"match:{match_id}:latest"
            redis_client.set(redis_key, json.dumps(event), ex=300)
            print(f"Cached latest event for match {match_id} to Redis key '{redis_key}'")

            # Fetch from Redis before emitting
            cached_data = redis_client.get(redis_key)
            if cached_data:
                # Decode cached JSON from Redis
                cached_event = json.loads(cached_data.decode('utf-8'))

                # Emit cached data to WebSocket clients
                socketio.emit('score_update', cached_event)
                print(f"Emitted cached event to WebSocket clients for match {match_id}")

            time.sleep(1)

    except Exception as e:
        print(f"Error consuming events: {e}")
    finally:
        consumer.close()
        print("Consumer closed.")


@app.route("/")
def index():
    return send_from_directory(WEB_DIR, "index.html")

@app.route("/api/active-matches")
def active_matches():
    # Get all keys matching the pattern
    keys = redis_client.keys("match:*:latest")
    # Extract just the match_id parts
    match_ids = [key.decode().split(":")[1] for key in keys]
    return jsonify(sorted(set(match_ids)))


if __name__ == "__main__":
    threading.Thread(target=consume_event, daemon=True).start()
    socketio.run(app, host='0.0.0.0', port=5000)