
import requests

url = 'http://api.duckduckgo.com/?q="presidents of the united states"&format=json'

# get the data about the photos
response = requests.get(url)

print(response.json())

