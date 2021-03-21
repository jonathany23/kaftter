#db.inventory.deleteMany({ status : "A" })
from pymongo import MongoClient
from util.kaffter_constants import Constants

#Mongo config
mg_user = Constants.MDB_USER
mg_pwd = Constants.MDB_PASSWORD
mg_dbname = Constants.MDB_DB_NAME
mg_conn_string = "mongodb+srv://"+str(mg_user)+":"+str(mg_pwd)+"@kaftter.4fjhv.mongodb.net/"+str(mg_dbname)+"?retryWrites=true&w=majority"

client = MongoClient(mg_conn_string)
db = client['kaftter']
coll = db['tweets']

#x = coll.delete_many({ "created_at":  "/Nov 08/" })
for x in coll.find({}, { "created_at" : "/Nov 08/" }):
    print(x['_id'])
    coll.delete_one({'_id': x['_id']})