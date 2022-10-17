import pymongo

CONNECTION_STRING = "mongodb+srv://hemed:Hmd.Man9@fezaalumni.fhgp8.mongodb.net/Labelling?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.Labelling

