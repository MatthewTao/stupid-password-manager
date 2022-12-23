import json


def read_json_config(path):
    """
    Reads a JSON file and returns a python dict
    """
    with open(path, "r") as read_file:
        config = json.load(read_file)
    return config
