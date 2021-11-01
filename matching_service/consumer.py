# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json

consumer = KafkaConsumer(
    'matching-topic',
     bootstrap_servers=['kafka-service:9092'],
     auto_offset_reset='lastest',
     enable_auto_commit=True,
     group_id='matching-service',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['kafka-service:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for message in consumer:
    message = message.value
    print(message)


