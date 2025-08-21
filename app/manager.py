import os
from pymongo import MongoClient
from .connection import ReadData
from .processor import Processor

MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
MONGO_HOST = os.getenv("MONGO_HOST", "mongo-app")
MONGO_DB = os.getenv("MONGO_INITDB_DATABASE", os.getenv("MONGO_DB", "mydb"))
MONGO_USER = os.getenv("MONGO_USERNAME")
MONGO_PASS = os.getenv("MONGO_PASSWORD")


# URI = f"mongodb+srv://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB.lower()}.gurutam.mongodb.net/"
URI = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"

class Manager:
    @staticmethod
    def pypeline():
        client = MongoClient(URI)
        data_reader = ReadData(client,"IranMalDB")
        df = data_reader.get_data()
        proc = Processor(df)
        proc.range_emotion()
        proc.list_weapons()
        return proc.data.to_dict(orient="records")
