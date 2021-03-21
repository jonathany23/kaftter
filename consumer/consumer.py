# pip install kafka-python
# https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
from kafka import KafkaConsumer
from pymongo import MongoClient

import json
import bson
import datetime

import sys
sys.path.insert(1, '/Users/jonathany23/Dropbox/kafka_dev/kaftter')
from util.kaffter_constants import Constants

#Kafka consumer glogal config
topic = 'us_elections'
group_id = 'grp01'
bootstrap_server = ['localhost:9092']
#auto_offset_reset = 'earliest'
auto_offset_reset = 'latest'

#Mongo connection config
mg_user = Constants.MDB_USER
mg_pwd = Constants.MDB_PASSWORD
mg_dbname = Constants.MDB_DB_NAME
mg_conn_string = "mongodb+srv://"+str(mg_user)+":"+str(mg_pwd)+"@kaftter.4fjhv.mongodb.net/"+str(mg_dbname)+"?retryWrites=true&w=majority"

client = MongoClient(mg_conn_string)
#Mongodb database
db = client['kaftter']
#Mongodb collection
coll = db['tweets']

# Para consumir los ultimos mensajes y auto-commit offsets
consumer = KafkaConsumer(topic,
                         group_id=group_id,
                         bootstrap_servers=bootstrap_server,
                         auto_offset_reset=auto_offset_reset)
#Start time
start = datetime.datetime.now()
for message in consumer:
    # Los campos value y key son bytes -- decodifique si es necesario
    '''print ("topic=%s partition=%d offset=%d key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value.decode('utf-8')))'''
    msg = message.value.decode('utf-8')
    #message value to string
    msg_str = json.loads(msg)
    #message string to dict
    msg_json = json.loads(msg_str)
    #send to save to mongodb
    x = coll.insert_one(msg_json)
    #End time
    end = datetime.datetime.now()
    print("tiempo "+ str(end - start)+" topic "+str(message.topic)+" particion: "+str(message.partition)+" offset: "+str(message.offset))


