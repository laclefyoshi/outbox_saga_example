# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'matching-topic',
     bootstrap_servers=['kafka-service:9092'],
     auto_offset_reset='lastest',
     enable_auto_commit=True,
     group_id='matching-service',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print(message)
