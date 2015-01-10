#!/usr/bin/python
# coding: utf8
from pymongo import MongoClient
import re

"""
Fixing Attributes
=================
- FT2
- VALUE
- PERMIT
- DU

Adding Attributes
=================
- housenumber
- unit
- direction
- city
"""

client = MongoClient()

for item in client.ottawa.permits.find({}):
    # Hardcode Attributes
    item['city'] = 'Ottawa'

    # Convert to Integers
    item['FT2'] = int(item['FT2'])
    item['VALUE'] = int(item['VALUE'])
    item['PERMIT'] = int(item['PERMIT'])
    item['DU'] = int(item['DU'])

    # Remove Units from Housenumber (Ex: 228-A >> 228)
    housenumber = item.get('ST')
    expression = r"\w+"
    pattern = re.compile(expression)
    match = pattern.findall(housenumber)
    if len(match) > 0:
        housenumber = int(match[0])
        item['housenumber'] = housenumber
    if len(match) > 1:
        try:
            item['unit'] = int(match[1])
        except:
            item['unit'] = match[1]
    if len(match) > 2:
        item['unit'] = '{0}-{1}'.format(match[1], match[2])

    # Remove blank fields
    for keys, values in item.items():
        if values == '':
            save = True
            del item[keys]

    # Save MongoDB
    client.ottawa.permits.save(item)

