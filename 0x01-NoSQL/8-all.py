#!/usr/bin/env python3
"""
all document model
"""
import pymongo


def list_all(mongo_collection):
    """
    list all document
    """

    return mongo_collection.list()
