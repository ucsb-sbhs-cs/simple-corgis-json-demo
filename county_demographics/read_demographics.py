
import json
from pprint import pprint

def findCounty(counties,state,countyName):

    for c in counties:
        if c["State"]==state and c["County"]==countyName:
            return c


with open('demographics.json') as json_data:
    counties = json.load(json_data)

print("type(counties)=",type(counties))
print("len(counties)=",len(counties))

print("counties[0]=",end="")
pprint(counties[0])

sb = findCounty(counties,"CA","Santa Barbara County")

pprint(sb)

