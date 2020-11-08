import pymongo
from databases.auth import dbuser, dbpassword

class DBConnection:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.t0gwi.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
            self.database = self.client["SmartGadget"]
            self.collection = self.collection["phrases"]


        except pymongo.errors.AutoReconnect as e:
            print(f"Could not connect to server: {e}")

    def save_sample(self, sample, label):
        self.collection.insert_one({
            'sample': sample,
            'label': label
            })

    def read_samples(self):
        data = self.collection.find({})
        array = []
        for sample in data:
            document = {
                "sample" : sample['sample'],
                "label" : sample['label']
            }
            array.append(document)
        return array 
