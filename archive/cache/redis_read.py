import redis
import json

#Connect to Redis
redis_client = redis.Redis(host = "localhost",port="6379",db=0)

def get_live_score(match_id):
    redis_key = f"match:{match_id}:latest"
    cached_data = redis_client.get(redis_key)
    
    if cached_data:
        event = json.loads(cached_data.decode('utf-8'))
        return event

    else:
        return {"error": "No live data found for this match"}
