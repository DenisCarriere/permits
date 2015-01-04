from pymongo import MongoClient
from haversine import haversine


client = MongoClient()
max_confidence = 8
min_confidence = 9
test_provider = 'google'

test = {}
for item in client.geocoder[test_provider].find({'properties.confidence': {'$lte': max_confidence}}):
    test[item['properties']['location']] = item

google = {}
google_count = 0
for item in client.geocoder.google.find({'properties.confidence': {'$gte': min_confidence}}):
    google[item['properties']['location']] = item

bing = {}
bing_count = 0
for item in client.geocoder.bing.find({'properties.confidence': {'$gte': min_confidence}}):
    bing[item['properties']['location']] = item

osm = {}
osm_count = 0
for item in client.geocoder.osm.find({'properties.confidence': {'$gte': min_confidence}, 'properties.quality':'house'}):
    osm[item['properties']['location']] = item

arcgis = {}
arcgis_count = 0
for item in client.geocoder.arcgis.find({'properties.confidence': {'$gte': min_confidence}}):
    arcgis[item['properties']['location']] = item

nokia = {}
nokia_count = 0
for item in client.geocoder.nokia.find({'properties.confidence': {'$gte': min_confidence}}):
    nokia[item['properties']['location']] = item

results = {}
for location, values in test.items():
    if location in arcgis:
        arcgis_count += 1
        results[location] = arcgis[location]
    if location in bing:
        bing_count += 1
        results[location] = bing[location]
    if location in nokia:
        nokia_count += 1
        results[location] = nokia[location]
    if location in osm:
        osm_count += 1
        results[location] = osm[location]

leftover = {}
for location, values in test.items():
    if not location in results:
        leftover[location] = values

for location, value in results.items():
    print '{0} - {1} ({2}, {3})'.format(
        location, 
        value['properties']['provider'],
        value['properties']['lat'],
        value['properties']['lng']
    )

print 'Test:', len(test)
print 'Google:', len(google)
print 'Bing:', len(bing), '+', bing_count
print 'Nokia:', len(nokia), '+', nokia_count
print 'ArcGIS:', len(arcgis), '+', arcgis_count
print 'OSM:', len(osm), '+', osm_count
print 'Results:', len(results)
print 'Leftover:', len(leftover)