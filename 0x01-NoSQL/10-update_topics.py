#!/usr/bin/env python3
"""
insert document model
"""


def update_topics(mongo_collection, name, topics):
    """
    isert document
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
