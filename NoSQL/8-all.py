#!/usr/bin/env python3
"""
Write a def to list all docs
"""
from pymongo import MongoClient

# Function to list all documents
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({}))



