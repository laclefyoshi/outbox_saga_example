# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json

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

for message in consumer:
    message = message.value
    print(message)
    data = {}
    producer.send(PRODUCE_TOPIC, value=data)
