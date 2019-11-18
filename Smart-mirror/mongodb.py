import pymongo

client = pymongo.MongoClient("mongodb+srv://nejc:<password>@cluster0-zn8kc.mongodb.net/test?retryWrites=true&w=majority")
db = client.test