#!/usr/bin/env python3
"""
all document model
"""
import pymongo


def list_all(mongo_collection):
    """
    list all document
    """ 
    return [doc for doc in mongo_collection.find()]
