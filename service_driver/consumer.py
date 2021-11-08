# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import time

BROKERS = ['kafka-service:9092']
CONSUMERG = "service-driver"
CONSUME_TOPIC = "driver-topic"
PRODUCE_TOPIC = "status-topic"
FROM = "driver-service"

consumer = KafkaConsumer(
    CONSUME_TOPIC,
     bootstrap_servers=BROKERS,
     auto_offset_reset='lastest',
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
