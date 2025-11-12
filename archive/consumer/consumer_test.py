from KafkaFiles import KafkaConsumer
import json

consumer = KafkaConsumer(
    "sportsevent",
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    consumer_timeout_ms=10000
)

def consume_messages():
    print("Starting consumer...")
    for message in consumer:
        print(f"Received: {message.value}")

if __name__ == "__main__":
    consume_messages()
