import json
import sys
sys.path.insert(0,'gen_config')


def get_config():
    print(__file__)
    with open("gen_config/config.json", "r") as f:
        config = json.load(f)
        return config

