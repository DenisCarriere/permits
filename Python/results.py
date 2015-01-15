from pymongo import MongoClient

client = MongoClient()

def find_errors():
	count = 0
	for item in client.geocoder.ottawa.find({'properties.accuracy':{'$exists':False}}):
		location = item['properties']['location']
		google = client.geocoder.google.find_one({'properties.location':location})
		confidence = google['properties']['confidence']
		if not confidence >= 8:
			ottawa = client.ottawa.permits.find_one({'location':location})
			print 'ERROR',location, ottawa['CONTRACTOR']

def contractor(name='glenview'):
	count = 0
	errors = 0
	for item in client.ottawa.permits.find({}):
		location = item['location']
		contractor = item.get('CONTRACTOR','').lower()
		if name in contractor:
			count += 1
			google = client.geocoder.google.find_one({'properties.location':location})
			confidence = google['properties']['confidence']
			if not confidence >= 8:
				print location
				errors += 1

	print name, ':',count
	print 'Errors:', errors


if __name__ == '__main__':
	contractor()