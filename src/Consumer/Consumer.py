import sys
import os

# Add the parent directory of 'Consumer' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from KafkaFiles.KafkaClientFactory import KafkaClientFactory
# from .KafkaClientFactory import KafkaClientFactory
import threading
import redis
from flask import Flask
import json
import time
import os
from flask import send_from_directory


# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*")

bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
factory = KafkaClientFactory(bootstrap_servers=bootstrap_servers)
topic = 'Sports'
consumer = factory.create_consumer(topic)
redis_client = factory.create_redis_client()
# WEB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'web'))



def consume_event(socketio):
    print("Consumer started")
    try:
        for message in consumer:
            event = message.value
            match_id = event.get('match_id')
            print(f"Received event: {event}")

            redis_key = f"match:{match_id}:latest"
            redis_client.set(redis_key, json.dumps(event), ex=300)
            socketio.emit('score_update', event)
            print(f"Cached & emitted event for match {match_id}")
            time.sleep(1)
    except Exception as e:
        print(f"Error consuming events: {e}")
    finally:
        consumer.close()
        print("Consumer closed.")

# @app.route("/")
# def index():
#     return send_from_directory(app.root_path, "index.html")

# if __name__ == "__main__":
#     threading.Thread(target=consume_event, daemon=True).start()
#     socketio.run(app, host='0.0.0.0', port=5000)
