from pymongo import MongoClient

class MyMongoConnector():

    def __init__(self, host='localhost', port=27017, dbName='text_for_lesson'):
        self.client = MongoClient(host=host, port=port)
        self.db = self.client[dbName]



    def insert_data_into_collection(self, collection_name='twitter_test_collection', data=None, verbose=False):
        if data is None:
            print("No data was given")
            return None

        collection = self.db[collection_name]
        collection.insert_one(data)
        if verbose:
            print(f'inserted data into {collection}')
        return None

    def query_all_from_collection(self, collection='twitter_test_collection'):
        res = self.db[collection].find({})
        return res

    def drop_collection(self, collection='twitter_test_collection'):
        print(f"dropping collection: {collection}")
        self.db.drop_collection(collection)
        print(f"-----------\nSanity Check-> Collections = {self.db.list_collection_names()}\n-----------")
        return None



if __name__=="__main__": # this is extremely standard in python
    connector = MyMongoConnector()
    connector.insert_data_into_collection(collection_name='new_collection', data={"name": "Juan Sanchez", "age": "32"})
    res = list(connector.query_all_from_collection())
    print(res)