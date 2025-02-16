#!/usr/bin/env python3
"""
Write a def to list all docs
"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """Return all documents in a MongoDB collection or an empty list if none exist."""
    return list(mongo_collection.find()) or []
