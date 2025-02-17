#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb+srv://myAtlasDBUser:HelloAgain22@myatlasclusteredu.asusjdu.mongodb.net/')
    # client = MongoClient('mongodb://127.0.0.1:27017')
    # print("✅ Connected to:", client.server_info())  # Shows MongoDB version
    # print("✅ Databases:", client.list_database_names())  # Lists all databases
    school_collection = client.school.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
    '''
    print("✅ Using database:", client.list_database_names())
    
    school_collection.insert_many([
    {"name": "School A"},
    {"name": "School B"}
    ])
    print("✅ Inserted test data.")
    '''