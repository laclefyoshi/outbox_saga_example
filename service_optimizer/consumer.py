# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import time

BROKERS = ['kafka-service:9092']
CONSUMERG = "service-optimizer"
CONSUME_TOPIC = "order-topic"
FROM = "optimizer-service"

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


for message in consumer:
    message = message.value
    msg = json.loads(message)
    tid = msg["transaction-id"]
    customer_info = msg["customer"]
    restaurant_info = msg["restaurant"]
    data = {"transaction-id": tid, "status": "in progress", "from": FROM}
    producer.send("status-topic", value=data)
    ## restaurant
    data = {"transaction-id": tid, "customer": customer_info, "driver": {"name": "Alice"}}
    producer.send("restaurant-topic", value=data)
    ## driver
    data = {"transaction-id": tid, "cusotmer": customer_info, "restaurant": restaurant_info}
    producer.send("driver-topic", value=data)
    data = {"transaction-id": tid, "status": "completed", "from": FROM}
    producer.send("status-topic", value=data)
