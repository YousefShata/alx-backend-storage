#!/usr/bin/env python3
"""
insert document model
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    isert document
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
