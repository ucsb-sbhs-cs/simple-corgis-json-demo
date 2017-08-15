
import json
from pprint import pprint

with open('music.json') as json_data:
    music = json.load(json_data)

print("type(music)=",type(music))
print("len(music)=",len(music))

print("music[0]=",end="")
pprint(music[0])

for m in music:
    print ('{:30} {:30}'.format(m["artist"]["name"],m["song"]["title"]))


