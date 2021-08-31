#!/usr/bin/env python
import pika, sys, os
from createDataFrame import create_dataframe_from_str
from insertDataBase import insert_database_with_rabbitMQ
def main():
    count = 0
    #credentials = pika.PlainCredentials('quanglt', 'hoilamgi1')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        #temp = body.decode()
        #insert_database_with_rabbitMQ ((create_dataframe_from_str(temp)))
        
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    count = count + 1
    print (count)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
