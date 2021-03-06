# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import time

BROKERS = ['kafka-service:9092']
CONSUMERG = "service-restaurant"
CONSUME_TOPIC = "restaurant-topic"
PRODUCE_TOPIC = "status-topic"
FROM = "restaurant-service"

consumer = KafkaConsumer(
    CONSUME_TOPIC,
     bootstrap_servers=BROKERS,
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id=CONSUMERG,
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=BROKERS,
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

def produce(tid, status):
    data = {"transaction-id": tid, "status": status, "from": FROM}
    producer.send(PRODUCE_TOPIC, value=data)

for message in consumer:
    msg = message.value
    print(msg)
    tid = msg["transaction-id"]
    customer_info = msg["customer"]
    driver_info = msg["driver"]
    produce(tid, "cooking")
    time.sleep(7.0)
    produce(tid, "completed")
