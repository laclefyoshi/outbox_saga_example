# outbox_saga_example

## service_order

Cusomter が Order を生成する

* Produce Topic: order-topic
    * `{transaction-id: , customer: , restaurant: }`
* Consume Topic: status-topic
    * `{transaction-id: , status: , from: }`

## service_optimizer

* Consume Topic: order-topic
    * `{transaction-id: , customer: , restaurant: }`
* Produce Topic: driver-topic, restaurant-topic, status-topic
    * `{transaction-id: , customer: , restaurant: }`
    * `{transaction-id: , customer: , driver: }`
    * `{transaction-id: , status: , from: optimizer-service }`

## service_driver

* Consume Topic: driver-topic
    * `{transaction-id: , customer: , restaurant: }`
* Produce Topic: status-topic
    * `{transaction-id: , status: , from: driver-service}`

## service_restaurant

* Consume Topic: restaurant-topic
    * `{transaction-id: , customer: , driver: }`
* Produce Topic: status-topic
    * `{transaction-id: , status: , from: restaurant-service}`

