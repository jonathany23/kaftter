# Gestión de mesajes usando el API Twitter
## Objetivo
Con el proposito de poner en practica lo aprendido en el curso de Kafka Administracion & Desarrollo.
- Crear una aplicación productor de mensajes Kafka
- Crear una aplicación consumidor de mensajes Kafka

## Descripción de la Aplicación
- Usa el API de twitter para descargar tweet relacionado a un tema que este en tendencia.
- Usa la libreria [Tweepy](https://www.tweepy.org/) para realizar la conexion entre la aplicación y Twitter.
- Crear una aplicación productor que envia tweets como mensajes
- Crear una aplicación consumidor que recibe y procesa los mensajes tweets
- Guargar tweet en una base de datos mongodb

## Herramientas
- Python
- Kafka
- Tweepy
- kafka-python
- Mongodb
- PyMongo
- MongoDB Atlas

## Dependencias
### Tweepy
        pip install tweepy
### Kafka
        pip install kafka-python
### PyMongo
        python -m pip install pymongo

## Arquitectura
![Arquitectura Kaftter](https://github.com/jonathany23/kaftter/blob/main/util/img/arqutectura.png?raw=true)

## Ejecución
1. Descargue los binarios de Apache Kafka y Apache Zookeeper "kafka-standalone":

        https://storage.googleapis.com/instaladores-academy/kafka/kafka-standalone.rar

1. Subir ZooKeeper 
Ingresar al directorio de zookeeper y ejecutar el siguiente comando en la terminal.
        
        ./zkServer.sh start-foreground
1. Subir Kafka
Ingresar al directorio de kafka y ejecutar el siguiente comando en la terminal.

        ./kafka-server-start.sh ../config/server.properties
1. Crear topic


        ./kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 2 --topic us_elections

1. Iniciar Consumidor 1
Ingresar a la carpera del proyecto. Abrir una nueva terminal y ejecutar el siguiente comando.

        python consumer/consumer.py
1. Iniciar Consumidor 2
Abrir una nueva terminal y ejecutar nuevamente el siguiente comando.

        python consumer/consumer.py
1. Iniciar Productor
Abrir una nueva terminal y ejecutar el siguiete comando.

        python Twitter.py    
