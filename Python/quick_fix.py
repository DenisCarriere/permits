from pymongo import MongoClient

client = MongoClient()

for item in client.geocoder.google.find({}):
	location = item['properties']['location']

	if item.get('location'):
		del item['location']
		client.geocoder.google.save(item)

	if not ', Ottawa, ON' in location:
		if ', Ottawa' in location:
			item['properties']['location'] = location.replace(', Ottawa', ', Ottawa, ON')
			client.geocoder.google.save(item)