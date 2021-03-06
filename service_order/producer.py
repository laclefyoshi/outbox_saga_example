# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import time
import random
import uuid

BROKERS = ['kafka-service:9092']
CONSUMERG = "service-order"
CONSUME_TOPIC = "status-topic"
PRODUCE_TOPIC = "order-topic"

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

customers = ["Penelope Chapman",
    "Bella Avery",
    "Boris Knox",
    "Heather Stewart",
    "Amelia Scott",
    "Madeleine Ross",
    "Liam Hughes",
    "Warren Hardacre",
    "Pippa Jones",
    "Amelia Peake"]

restaurants = ["Bistro Bazaar",
    "Bistro Captain",
    "Bistroporium",
    "Kitchen Sensation",
    "Kitchen Takeout",
    "Menu Feed",
    "Menu Gusto",
    "Munchies",
    "Munch Grill",
    "Munchtastic"]

while True:
    tid = str(uuid.uuid4())
    ## order
    customer = random.choice(customers)
    restaurant = random.choice(restaurants)
    data = {"transaction-id": tid, "customer": {"name": customer}, "restaurant": {"name": restaurant}}
    producer.send(PRODUCE_TOPIC, value=data)
    print(data)
    time.sleep(random.randint(5, 20))
    ## payment
    payment = random.choice([0, 1])  # cancel or done
    data = {"transaction-id": tid, "payment": payment}
    producer.send(PRODUCE_TOPIC, value=data)
    print(data)
    time.sleep(random.randint(10, 60))
