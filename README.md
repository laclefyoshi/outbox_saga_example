# outbox_saga_example

## service_order

Cusomter が Order を生成する

Produce Topic: order-topic
Consume Topic: status-topic

## service_optimizer

Consume Topic: order-topic
Produce Topic: restaurant-topic, driver-topic

## service_driver

Consume Topic: driver-topic
Produce Topic: status-topic

## service_restaurant

Consume Topic: restaurant-topic
Produce Topic: status-topic

