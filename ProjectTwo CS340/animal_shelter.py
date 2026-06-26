from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:

    def __init__(self, username='aacuser', password='SNHU1234'):
        # Initialize MongoDB client
        self.client = MongoClient(
            f'mongodb://{username}:{password}@localhost:27017/?authSource=aac'
        )

        # Connect to database and collection
        self.database = self.client['aac']
        self.collection = self.database['animals']

    # CREATE
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError as e:
                print("Create Error:", e)
                return False
        else:
            raise Exception("Nothing to save because data parameter is empty")

    # READ
    def read(self, query):
        try:
            result = self.collection.find(query)
            return list(result)
        except PyMongoError as e:
            print("Read Error:", e)
            return []

    # UPDATE
    def update(self, query, new_values):
        try:
            result = self.collection.update_many(
                query,
                {"$set": new_values}
            )
            return result.modified_count
        except PyMongoError as e:
            print("Update Error:", e)
            return 0

    # DELETE
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print("Delete Error:", e)
            return 0