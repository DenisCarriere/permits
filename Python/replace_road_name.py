from pymongo import MongoClient

client = MongoClient()

for item in client.ottawa.permits.find({'road':'Unity Street'}):
	print item
	exit()
	item['road'] = 'Saturn'
	item['suffix'] = 'Crescent'
	item['location'] = item['location'].replace('Sternes, Des Private','Saturn Crescent')
	#client.ottawa.permits.save(item)


# Sternes, Des Privates >> Saturn Crescent
# Unity Street >> LeBoutillier Avenue