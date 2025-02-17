#!/usr/bin/env python3
"""
  Python function that returns 
  the list of school having a specific topic:
"""
def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for in the 'topics' field.

    Returns:
        A list of schools that have the given topic.
    """
    if mongo_collection is None:
        return []  # Return empty list if collection is invalid

    return list(mongo_collection.find({"topics": topic}))  # Query documents with topic in the 'topics' array
