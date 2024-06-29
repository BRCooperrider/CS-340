from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, username, password):
        #Initialize the Mongo Client
        #Connection variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30578
        DB = 'AAC'
        COL = 'animals'
        
        #Initialize connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
#Implement the C in CRUD
    def create(self, data):
        if data is not None:
            insert_result = self.database.animals.insert_one(data) #data should be in dictionary
            return True if insert_result.acknowledged else False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
#Implement the R in CRUD
    def read(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria)
            return data
        else:
            #data = self.database.animals.find({})
            raise Exception("Nothing to save, because data parameter is empty")
            
        #return data
    
#Implement the U in CRUD
    def update(self, data, updatedValue):
        if data is None:
            raise Exception("No search criteria given")
        elif updatedValue is None:
            raise Exception("No update value is given")
        else:
            update_result = self.database.animals.update_one(data, {"$set": updatedValue})
            return update_result.modified_count
        
#Implement the D in CRUD
    def delete(self, data):
        if data is not None:
            delete_result = self.database.animals.delete_one(data)
            return delete_result.deleted_count
        else:
            raise Exception("Invalid search criteria")