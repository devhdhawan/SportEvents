from kafka import KafkaConsumer
import json
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)


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
        eventDate  = message.value
        match_id = eventDate.get("match_id")
        score_id = eventDate.get("score_id")
        score = eventDate.get("team_a_score")

        # Store in Redis cache with key
        redis_key = f"match:{score_id}:score"
        redis_client.set(redis_key, score, ex=300)  # expire in 300 seconds
        print(f"Cached to Redis key: {redis_key}")


if __name__ == "__main__":
    consume_messages()
