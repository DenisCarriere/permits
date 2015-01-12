from pymongo import MongoClient

client = MongoClient()

for item in client.ottawa.permits.find({}):
	location = item['location']
	if not ', ON' in location:
		item['location'] = location + ', ON'

	client.ottawa.permits.save(item)