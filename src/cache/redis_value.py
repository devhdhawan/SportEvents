import redis
r = redis.Redis(host='localhost', port=6379, db=0)

key = 'match:SCORE2:score'  # Use the actual key from your test
value = r.get(key)
if value:
    print(f"Found Redis value: {value.decode('utf-8')}")
else:
    print("Key not found.")