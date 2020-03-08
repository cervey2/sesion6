from pymongo import MongoClient

client = MongoClient(host=['localhost'], port = 27017, username='', password = '')
db = client.Ecobici

#db = client.list_database_names()

client.list_databases_names

db = client.ecobici








