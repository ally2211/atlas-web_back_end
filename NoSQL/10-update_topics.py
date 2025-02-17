#!/usr/bin/env python3
"""
 Python function that changes all topics 
 of a school document based on the name:
"""
def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the school's name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set in the document.

    Returns:
        None
    """
    if mongo_collection is None:
        return None  # If collection is invalid, do nothing

    mongo_collection.update_many(
        {"name": name},  # Find documents where name matches
        {"$set": {"topics": topics}}  # Update the topics field
    )
