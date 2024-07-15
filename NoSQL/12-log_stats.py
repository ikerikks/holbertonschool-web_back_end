#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


# if __name__ == "__main__":
#     client = MongoClient()
#     collection = client.logs.nginx

#     count = collection.count_documents({})

#     print("{} logs".format(count))
#     print("Methods:")

#     methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
#     for method in methods:
#         print("\tmethod {}: {}".format(method,
#                                          collection.count_documents
#                                          ({"method": method})))

#     count_status = collection.count_documents({"method": "GET",
#                                                "path": "/status"})
#     print("{} status check".format(count_status))


def log_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Number of documents in the collection
    log_count = collection.count_documents({})

    # Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # GET requests with path /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Print results
    print(f"{log_count} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
