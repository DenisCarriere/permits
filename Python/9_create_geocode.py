#!/usr/bin/python
# coding: utf8
from pymongo import MongoClient


client = MongoClient()

# Store in memory
google = {}
for item in client.geocoder.google.find({},{'_id':0}):
    google[item['properties']['location']] = item

# Add to Ottawa > Geocoder
print client.ottawa.permits.count()
client.ottawa.geocoder.remove({})
for item in client.ottawa.permits.find({},{'_id':0}):
    result = {
        'type':'feature',
        'geometry': {'type':'Point', 'coordinates': [0.0, 0.0]},
        'properties': {},
        }
    search = google[item['location']]
    result.update(search)
    result['properties'].update(item)

    # Store Result in MongoDB > Ottawa > Geocoder
    client.ottawa.geocoder.save(result)

print client.ottawa.geocoder.count()