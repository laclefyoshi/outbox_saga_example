# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import time

CONSUME_TOPIC = "driver-topic"
PRODUCE_TOPIC = "status-topic"

consumer = KafkaConsumer(
    CONSUME_TOPIC,
     bootstrap_servers=['kafka-service:9092'],
     auto_offset_reset='lastest',
     enable_auto_commit=True,
     group_id='service-driver',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['kafka-service:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

def produce(tid, status):
    data = {"transaction-id": tid, "status": status, "from": "driver-service"}
    produ.send(PRODUCE_TOPIC, value=data)

for message in consumer:
    message = message.value
    msg = json.loads(message)
    tid = msg["transaction-id"]
    customer_info = msg["customer"]
    restaurant_info = msg["restaurant"]
    produce(tid, "assigned")
    time.sleep(5.0)
    produce(tid, "in progress")
    time.sleep(7.0)
    produce(tid, "completed")
