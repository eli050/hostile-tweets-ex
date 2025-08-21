import pandas as pd
from pymongo import MongoClient




class ReadData:
    def __init__(self,client: MongoClient, db_name: str , collection_name: str = "tweets") -> None:
        self.client = client
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]


    def get_data(self):
        """Fetch all documents from the collection."""
        try:
            df = pd.DataFrame(list(self.collection.find()))
            df["_id"] = df["_id"].astype(str)
            return df
        except Exception as e:
            raise Exception(f"Failed to fetch data: {e}") from e



# client = MongoClient("mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
# data_reader = ReadData(client,"IranMalDB")
# print(client.admin.command("ping"))
# df = data_reader.get_data()
#
# proc = Processor(df)
# proc.range_emotion()
# proc.list_weapons()
# a =proc.data.to_json(orient="records")
# pprint(json.loads(a))