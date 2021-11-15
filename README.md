# outbox_saga_example

## service_order

Cusomter が Order を生成する

* Produce Topic: order-topic
    * `{transaction-id: , customer: , restaurant: }`
    * `{transaction-id: , payment: [1, 0]}`
        * 1: done, 0: cancel
* Consume Topic: status-topic
    * `{transaction-id: , status: , from: }`

## service_payment

* Consume Topic: order-topic
    * `{transaction-id: , customer: , restaurant: }`
    * `{transaction-id: , payment: [true, cancel]}`
* Produce Topic: order-topic
    * `{transaction-id: , customer: , restaurant: , payment: 1}`

## service_optimizer

* Consume Topic: order-topic
    * `{transaction-id: , customer: , restaurant: , payment: 1}`
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

