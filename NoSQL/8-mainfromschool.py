#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    try:
        client = MongoClient('mongodb://127.0.0.1:27017', serverSelectionTimeoutMS=5000)
        print(client.server_info())  # ✅ This should print MongoDB details
    except Exception as e:
        print(f"❌ MongoDB Connection Error: {e}")
        exit(1)  # Stop execution if MongoDB is not accessible

    db = client.school
    school_collection = db.school

    print("✅ Connected to database. Collection count:", school_collection.count_documents({}))  # DEBUG

    schools = list_all(school_collection)

    if not schools:
        print("⚠️ No documents found in the collection.")
    else:
        for school in schools:
            print("[{}] {}".format(school.get('_id'), school.get('name')))

    cursor = school_collection.find()
    for doc in cursor:
        print(doc)  # This should print all documents