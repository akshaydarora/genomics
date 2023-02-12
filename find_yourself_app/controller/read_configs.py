import json


def read_json_config():
    with open("configs/config.json", "r") as rf:
        return json.load(rf)
    return None