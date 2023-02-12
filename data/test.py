import json
import os

path = os.getcwd()
print(path)
with open("config.json", "r") as rf:
    print( json.load(rf))
