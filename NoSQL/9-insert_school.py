#!/usr/bin/env python3
"""
Write a def to insert docs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs representing the document fields.

    Returns:
        The `_id` of the inserted document.
    """
    if mongo_collection is None:
        return None  # Return None if collection is invalid

    result = mongo_collection.insert_one(kwargs)  # Insert document
    return result.inserted_id  # Return the new document's _id
