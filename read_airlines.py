
import json
from pprint import pprint

with open('airlines.json') as json_data:
    airlines = json.load(json_data)

print("len(airlines)=",len(airlines))

print("airlines[0]",airlines[0])
