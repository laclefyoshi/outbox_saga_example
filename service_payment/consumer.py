# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import time

BROKERS = ['kafka-service:9092']
CONSUMERG = "service-payment"
CONSUME_TOPIC = "order-topic"
FROM = "optimizer-payment"

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

transactions = {}

for message in consumer:
    msg = message.value
    print(msg)
    tid = msg["transaction-id"]
    if "payment" in msg:
        if msg["payment"] == 1:
            orderinfo = transactions[tid]
            ## paid order
            data = {"transaction-id": tid, "customer": orderinfo["customer"], "restaurant": orderinfo["restaurant"], "payment": 1}
            producer.send("order-topic", value=data)
            del transactions[tid]
        else: ## payment == 0/cancel
            del transactions[tid]
    else:
        customer_info = msg["customer"]
        restaurant_info = msg["restaurant"]
        data = {"customer": customer_info, "restaurant": restaurant_info}
        transactions[tid] = data
