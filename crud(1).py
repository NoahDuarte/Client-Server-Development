# 1. create a python file called animal_shelter.py and paste the AnimalShelter class.
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, db, collection):
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[collection]

    # Create method that inserts document(s) into a specified MongoDB database and specified collection
    def create(self, data):
        # Checks to see if the data is null or empty
        if data is not None:
            if data:
                # inserts document(s) into the specified database and specified collection
                self.database.animals.insert_one(data)
                return True
        else:
            # raise an exception if there is no data to save and return false
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    def read(self, search):
        # Checks to see if the data is null or empty
        if search is not None:
            # search through specified database and collection and returns document(s) if found.
            searchResult = list(self.database.animals.find(search, {"_id": False}))
            return searchResult
        else:
            # returns an exception if the data is empty or nothing to search
            exception = "Nothing to search, because data parameter is empty"
            return exception
    
    # Update method that queries for and changes document(s) from a specified MongoDB database and specified collection
    def update(self, search, update_data):
        # Input -> arguments to function should be the key/value lookup pair to use with the MongoDB driver Find API call.
        # The last argument to the function will be a set of key/value pairs in the data type acceptable to the MongoDB
        if search is not None and update_data is not None:
            # driver update_one() or update_many() API call.
            result = self.database.animals.update_many(search, {"$set": update_data})
            return result.modified_count
        else:
            # Return -> The number of objects modified in the collection.
            raise Exception("Nothing to update, because search or update_data parameter is empty")

    # Delete method that queries for and removes document(s) from a specified MongoDB database and specified collection
    def delete(self, search):
        # Input -> arguments to function should be the key/value lookup pair to use with the MongoDB driver find API call.
        if search is not None:
            result = self.database.animals.delete_many(search)
            return result.deleted_count
        else:
            # Return -> The number of objects removed from the collection.
            raise Exception("Nothing to delete, because search parameter is empty")
