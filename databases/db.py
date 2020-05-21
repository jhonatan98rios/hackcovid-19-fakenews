import pymongo
from databases.auth import dbuser, dbpassword

class DBConnection:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(f"mongodb://{dbuser}:{dbpassword}@ds163757.mlab.com:63757/heroku_9407v38l")
            #self.database = self.client["HackCovid-19"]  # Access DataBase
            self.database = self.client["heroku_9407v38l"]  # Access DataBase
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


# Heroku connection string: mongodb://<dbuser>:<dbpassword>@ds163757.mlab.com:63757/heroku_9407v38l
# databasename: heroku_9407v38l
# collection: Collection_01
# user: heroku_9407v38ll
# passw: P$yJb2hdi$wW35u

# Shell
# mongo ds163757.mlab.com:63757/heroku_9407v38l -u heroku_9407v38ll -p P$yJb2hdi$wW35u