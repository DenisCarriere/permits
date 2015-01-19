from pymongo import MongoClient

client = MongoClient()

permits = {}

for item in client.ottawa.permits.find({},{'_id':0}):
	permits[item['location']] = item

for item in client.geocoder.google.find({}):
	item['permits'] = permits[item['properties']['location']]
	client.geocoder.google.save(item)