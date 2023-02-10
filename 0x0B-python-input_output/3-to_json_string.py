#!/usr/bin/python3
"""fuction that returns JSON rep"""
import json

def to_json_string(my_obj):
    """return a JSON object
    args:
        my_obj: object to return
    """
    return json.dumps(my_obj)
