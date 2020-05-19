import pymongo
from databases.auth import user, passw

class DBConnection:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(f"mongodb+srv://{user}:{passw}@cluster0-oqiei.gcp.mongodb.net/test?retryWrites=true&w=majority")
            self.database = self.client["HackCovid-19"]  # Access DataBase
            self.collection = self.database["Collection_01"]  # Access collection
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