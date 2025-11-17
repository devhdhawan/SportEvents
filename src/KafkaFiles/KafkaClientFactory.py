import json
from kafka import KafkaProducer, KafkaConsumer
import redis


class Singleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__( *args, **kwargs)
        return cls._instance[cls]


class KafkaProducerSingleton(metaclass=Singleton):
    def __init__(self,bootstrap_servers='localhost:9092', **kwargs):
        self.producer = KafkaProducer(
            bootstrap_servers=[bootstrap_servers],
            value_serializer=kwargs.get('value_serializer', lambda v: json.dumps(v).encode('utf-8')),
            key_serializer=kwargs.get('key_serializer', lambda k: k.encode('utf-8'))
        )
    
    def get_producer(self):
        return self.producer


class KafkaConsumerSingleton(metaclass=Singleton):
    def __init__(self,topic, group_id=None, auto_offset_reset='earliest',bootstrap_servers='localhost:9092',**kwargs):
        self.consumer = KafkaConsumer(
            topic,
            group_id=group_id,
            auto_offset_reset=auto_offset_reset,
            value_deserializer= (lambda m: json.loads(m.decode('utf-8'))))
    
    def get_consumer(self):
        return self.consumer

class RedisClassSingleton(metaclass=Singleton):
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.Redis(host=host, port=port, db=db)

    def get_redis_client(self):
        return self.redis_client

class KafkaClientFactory:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.bootstrap_servers = bootstrap_servers

    def create_producer(self, value_serializer=None, key_serializer=None,**kwargs):
        return KafkaProducerSingleton(self.bootstrap_servers,**kwargs).get_producer()

    def create_consumer(self, topic, group_id=None, auto_offset_reset='earliest', **kwargs):
        return KafkaConsumerSingleton(topic, group_id, auto_offset_reset, **kwargs).get_consumer()

    def create_redis_client(self, host='localhost', port=6379, db=0):
        return RedisClassSingleton(host, port, db).get_redis_client()