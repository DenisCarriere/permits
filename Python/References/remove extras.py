from pymongo import MongoClient

client = MongoClient()

for item in client.geocoder.google.find({}):
	location = item['properties']['location']
	if not ', ON' in location:
		client.geocoder.google.remove(item)