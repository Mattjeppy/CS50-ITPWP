import requests 
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# gets url from itunes
o = response.json()
# makes a json object
for result in o["results"]:
    # in the dictionary, from key results
    print(result["trackName"])
# weezer