"""Utils for creating and loading dialogue datasets."""

import logging
import json
import os
import re

def LoadFile(file_path):
    """load raw data file."""
    data = None
    if file_path.endswith(".json"):
        with open(file_path) as f:
            data = json.load(f)
    elif file_path.endswith(".txt"):
        with open(file_path) as f:
            data = f.read().strip("\n").split("\n")
    else:
        logging.error("Cannot recognize the file to be loaded.") 

    return data


class DataManager:
    """Creates training and test data."""

    def __init__(self):
        self.data_dir = ""
        self.ontology = {}