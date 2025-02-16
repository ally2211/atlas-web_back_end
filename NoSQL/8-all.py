#!/usr/bin/env python3
"""
Write a def to list all docs

def list_all(mongo_collection):
    return list(mongo_collection.find()) or []

"""
from pymongo import MongoClient


# Force compatibility with older MongoDB versions
client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000, directConnection=True)

# Select the database
db = client.my_database  # Replace with your actual database name
collection = db.school   # Replace with your actual collection name

# Function to list all documents
def list_all(mongo_collection):
    """Return all documents in a MongoDB collection or an empty list if none exist."""
    return list(mongo_collection.find()) or []


