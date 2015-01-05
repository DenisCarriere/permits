#!/usr/bin/python
# coding: utf8

import fiona
import os
from pymongo import MongoClient

# Create Mongo connection
client = MongoClient()
provider = 'google'
db = client.geocoder[provider]
path = '/home/ubuntu/GIS/{0}.shp'.format(provider)

# Build container with all the features of MongoDB
print 'Building container...'
container = []
for item in db.find({'geometry':{'$exists':True}},{'_id':0}):
    container.append(item)

# Get all attributes
print 'Reading attributes...'
blank = {}
properties = {}
for item in container:
    for p in item.get('properties').keys():
        blank[str(p)] = ''
        properties[str(p)] = 'str'

# Only define the Integer fields, the rest will be Strings
properties.update({
    'FT2':'int',
    'FT2_unit':'int',
    'TOTAL_unit':'int',
    'COST_unit': 'float',
    'lat': 'float',
    'lng': 'float',
    'year':'int',
    'VALUE':'int',
    'VALUE_unit': 'int',
    'PERMIT':'int',
    'housenumber':'int',
    'DU':'int',
})
# Fiona input for schema must be a list
properties = list(properties.items())

# Shapefile parameters
crs = {'init':'epsg:4326'}
driver = 'ESRI Shapefile'
encoding = 'utf-8'
schema = {
    'geometry':'Point',
    'properties': properties
}

# Confirm if folder path exists
folder, file_name = os.path.split(path)
if folder:
    if not os.path.exists(folder):
        os.mkdir(folder)

# Create Shapefile
print 'Creating Shapefile...'
with fiona.open(
    path, 'w', 
    driver=driver, 
    schema=schema, 
    crs=crs, 
    encoding=encoding) as sink:
    for item in container:
        # Ensures Blank fields for the schema
        baseline = blank
        baseline.update(item.get('properties'))
        item['properties'] = baseline
        try:
            sink.write(item)
        except:
            print item
            exit()
print 'Done!'