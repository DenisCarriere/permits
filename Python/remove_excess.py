from pymongo import MongoClient

client = MongoClient()

permits = {}

for item in client.ottawa.permits.find({}):
	permits[item['location']] = ''

for item in client.geocoder.google.find({}):
	location = item['properties']['location']

	if not location in permits:
		print 'REMOVED:', location
		client.geocoder.google.remove({'properties.location':location})