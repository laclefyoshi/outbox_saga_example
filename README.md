# outbox_saga_example

## order_service

Customer から Order を受け取る

* Input: Order(Customer, Store/Thing)
* Output to Kafka: Transaction-id, Order

Order の結果を表示する

* Input from Kafka: Transaction-id, Order, Status
* Output: Order, Status

## matching_service

Order を受け取り、Deliverman をアサインする

* Input from Kafka: Transaction-id, Order
* Output to Kafka: Transaction-id, Order, Deliverman

## delivery_service

Deliverman が Store から Thing を受け取る
Deliverman が Customer に Thing を届ける

* Input from Kafka: Transaction-id, Order, Deliverman
* Output to Kafka: Transaction-id, Order, Status


