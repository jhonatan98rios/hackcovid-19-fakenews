import os
import pymongo
""" from databases.auth import dbuser, dbpassword """

dbuser = os.environ['USER']
dbpassword = os.environ['PASS']

class DBConnection:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("mongodb+srv://"+dbuser+":"+dbpassword+"@cluster0.oqiei.gcp.mongodb.net/FarejaFatos?retryWrites=true&w=majority")
            self.database = self.client["FarejaFatos"]
            self.collection = self.database["Samples"]

        except pymongo.errors.AutoReconnect as e:
            print(f"Could not connect to server: {e}")

    def save_sample(self, sample):
        self.collection.insert_one({
            'sample': sample,
        })

    def read_samples(self):
        data = self.collection.find({})
        array = []
        for sample in data:
            document = {
                "sample" : sample['sample'],
            }
            array.append(document)
        return array 
