#!/usr/bin/env python3
"""
find document model
"""


def schools_by_topic(mongo_collection, topic):
    """
    find document based on topic
    """
    return [doc for doc in mongo_collection.find({"topics": topic})]
