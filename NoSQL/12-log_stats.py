#!/usr/bin/env python3
"""
Nginx logs stats script
"""

from pymongo import MongoClient

def nginx_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.
    """
    # Connect to MongoDB
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    nginx_collection = db.nginx

    # Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs per method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\t{method}: {count}")

    # Count logs where method=GET and path=/status
    status_logs = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_logs} status check")

if __name__ == "__main__":
    nginx_stats()
