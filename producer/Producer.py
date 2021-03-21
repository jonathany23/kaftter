# pip install kafka-python
# https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html
from kafka import KafkaProducer
import json


def kafka_producer(str_json):
    ''' Producer to send tweet message to broker Kafka
    '''
    #Kafka global config
    topic = 'us_elections'
    bootstrap_server = ['localhost:9092']
    limit = 10

    producer = KafkaProducer(bootstrap_servers=bootstrap_server)

    # produce asynchronously
    '''for i in range(limit):
        producer.send(topic,key=b'%i' % i, value=b'mensaje %d' % i)
        producer.flush()
        print("mensaje enviado: " + 'mensaje %d' % i)'''

    # produce json messages
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    producer.send(topic, str_json)
    producer.flush()