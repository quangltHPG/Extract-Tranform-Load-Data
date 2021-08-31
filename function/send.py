#!/usr/bin/env python
import pika

def client_send(strData):
    #connection = pika.BlockingConnection(
    #    pika.ConnectionParameters(host='localhost'))

    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('rabbit@raspberrypi',
                                        5672,
                                        '/',
                                        credentials)      
    connection = pika.BlockingConnection(parameters)  
    channel = connection.channel()
    
    channel.queue_declare(queue='temp')

    channel.basic_publish(exchange='', routing_key='hello', body=strData)
    print(" [x] Sent ", strData)
    connection.close()

strData = "hello quanglt"
client_send(strData)