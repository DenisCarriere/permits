#!/usr/bin/python
# coding: utf8
"""
Adding Attributes
=================
- location
"""

from pymongo import MongoClient

client = MongoClient()

for item in client.ottawa.permits.find({}):
    housenumber = item.get('housenumber')
    road = item.get('road')
    suffix = item.get('suffix')
    direction = item.get('direction')

    location = []
    if housenumber:
        location.append(str(housenumber))
    if road:
        location.append(road.title())
    if suffix:
        location.append(suffix)
    if direction:
        location.append(direction)

    item['location'] = ' '.join(location) + ', Ottawa, ON'

    # Save MongoClient
    client.ottawa.permits.save(item)