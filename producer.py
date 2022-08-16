
import pika
import time
import random
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('13.214.190.7')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange="topicexchange", exchange_type=ExchangeType.topic)

data = {
    "business.asia.order":"A Asian business ordered goods", 
    "user.payments":"A Asia user paid for something",
    "shop": "user ordered something",
    "user.asia" : "user and asia both consumer will get this"
}

messageID = 1
while(True):
    routing_key, messages = random.choice(list(data.items()))
    message = f"{messages}: {messageID}"
    channel.basic_publish(exchange="topicexchange", routing_key=f"{routing_key}", body=message)
    time.sleep(random.randint(1, 4))
    print(messageID, f"{routing_key}")
    messageID+=1

