import pymongo, os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING")

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.Labelling

