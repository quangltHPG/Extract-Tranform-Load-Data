import pika

credentials = pika.PlainCredentials('quanglt', 'hoilamgi1')
parameters = pika.ConnectionParameters('192.168.113.86',
                                   5672,
                                   '/',
                                   credentials)
while 1:
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                    routing_key='hello',
                    body='Hello W0rld!')
    print(" [x] Sent 'Hello World!'")
connection.close()