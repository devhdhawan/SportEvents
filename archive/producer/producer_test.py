from KafkaFiles import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic ="sportsevent"

def send_test_messages():
    for i in range(10):
        data = {
            'match_id': 'MATCH1',
            'score_id': 'SCORE'+str(i),
            'event': 'score_update',
            'team_a_score': 200 + i,
            'team_b_score': 190 + i,
            'timestamp': time.time()
        }
        producer.send(topic, value=data)
        print(f"Sent message: {data}")
        time.sleep(1)

if __name__ == "__main__":
    send_test_messages()