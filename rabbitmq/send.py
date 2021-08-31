#!/usr/bin/env python
import pika
while 1:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()
    temp = 1
    channel.queue_declare(queue='temp')

    channel.basic_publish(exchange='', routing_key='hello', body='hello HPDQ' + str(temp))
    print(" [x] Sent ", temp)
connection.close()
