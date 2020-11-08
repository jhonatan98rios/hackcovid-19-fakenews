import os
import pymongo
# from databases.auth import dbuser, dbpassword

dbuser = os.environ['USER']
dbpassword = os.environ['MONGO']

class DBConnection:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("mongodb+srv://"+dbuser+":"+dbpassword+"@cluster0.t0gwi.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
            self.database = self.client["FarejaFatos"]
            self.collection = self.collection["Samples"]


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
