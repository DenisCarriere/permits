import geocoder
import json
import argparse
import os
import time
from pymongo import MongoClient


# Simple CLI function
parser = argparse.ArgumentParser(description="Geocode an arbitrary number of strings from Command Line.")
parser.add_argument('-p', '--provider', help="provider (choose from: bing,"+\
"geonames, google, mapquest, nokia, osm, tomtom, geolytica, arcgis, yahoo)", default='bing')
args = parser.parse_args()
provider = args.provider

# Connect to MongoDB
client = MongoClient()
db_ottawa = client.ottawa
db_geocoder = client.geocoder[provider]

# Store values in memory 
container = []
for item in db_ottawa.permits.find({}, {'_id':0}):
    container.append(item)

container_geocoder = {}
for item in db_geocoder.find({}, {'properties.location':1}):
    container_geocoder[item['properties']['location']] = True

# Print Results
print 'Provider:',provider
print 'Permits:', len(container)
print 'Geocoded:', len(container_geocoder)

# Loop inside all permits
for item in container:
    location = item.get('location')

    if location:
        # Only find ones that don't exist in Geocoder DB
        if not location in container_geocoder:

            # Geocode address
            g = geocoder.get(location, provider=provider, timeout=15.0)

            # Append all Attributes with Geocode + Permits
            geojson = g.geojson
            geojson['properties'].update(item)

            # Break if OVER QUERY using Google
            if g.status in ['OVER_QUERY_LIMIT']:
                print 'Over QUERY'
                exit()
                os.system('nmcli con down id CyberGhost')
                time.sleep(60*5)
                print 'Shuting Down CyberGhost...'
                os.system('nmcli con up id CyberGhost')
                time.sleep(10)
                print 'Cyberghost Active!'
            elif g.status in ['ZERO_RESULTS']:
                db_geocoder.insert(geojson)
                print provider, 'Added ZERO:', location
            elif g.ok:
                # Add data in Mongo Database
                db_geocoder.insert(geojson)
                print provider, 'Added:', location
            else:
                print 'Fail:',g, location
