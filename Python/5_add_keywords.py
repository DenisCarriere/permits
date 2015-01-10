#!/usr/bin/python
# coding: utf8
from pymongo import MongoClient
import re

"""
Adding Attributes
=================
- keyword
"""

keywords = [
    r'construct a [\d+] storey',
    r'construct a [\d+] unit',
    r'construct a semi detached dwelling',
    r'construct a triplex',
    r'construct a semi-detached dwelling',
    r'construct a detached dwelling',
    r'detached dwelling',
    r'photovoltaic',
    r'tenant fit[- ]?up',
    r'boathouse',
    r'cabana',
    r'roof',
    r'sunroom',
    r'porch',
    r'canopy',
    r'riding arena',
    r'pavillion',
    r'sidewalk',
    r'patio',
    r'enclosure',
    r'carport',
    r'basement',
    r'deck',
    r'gazibo',
    r'gazebo',
    r'shed',
    r'bathroom',
    r'garage',
    r'kitchen',
    r'interior',
    r'addition',
    r'plumbing',
    r'solar',
    r'marijuana',
    r'season sunroom',
    r'farm building',
    r'horse stable',
    r'block',
    r'demolition',
    r'demolish',
    r'greenhouse',
    r'grain bin',
    r'fireplace',
    r'woodstove',
    r'storage building',
    r'convert a duplex into a triplex',
    r'swim spa',
    r'nutrient storage facility',
    r'stove',
    r'silo',
    r'kiosk',
    r'window',
    r'fire escape',
    r'alteration[s]?',
]

def match_keyword(string):
    for keyword in keywords:
        pattern = re.compile(keyword)
        match = pattern.findall(string.lower())
        if match:
            return match[0]


client = MongoClient()
for item in client.ottawa.permits.find({}):
    description = item.get('DESCRIPTION')
    item['keyword'] = match_keyword(description)
    
    if not item['keyword']:
        try:
            print 'WARNING Keyword:', description
        except:
            pass

    # Save MongoDB
    client.ottawa.permits.save(item)