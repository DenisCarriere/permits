from pymongo import MongoClient
import os


client = MongoClient()

lookup_suffix = {
    'GT': 'Gate',
    'DRWY': 'Driveway',
    'DR': 'Drive',
    'PL': 'Place',
    'CIR': 'Circle',
    'PRIV': 'Private',
    'RD': 'Road',
    'CRES': 'Crescent',
    'AVE': 'Avenue',
    'AV.': 'Avenue',
    'AV': 'Avenue',
    'GRV': 'Grove', 
    'GR': 'Grove',
    'GDN': 'Garden',
    'PK': 'Park',
    'TERR': 'Terrace', 
    'TER': 'Terrace',
    'CRT': 'Court',
    'CT': 'Court',
    'RDG':'Ridge',
    'TR': 'Trail',
    'TRL': 'Trail',
    'BLVD': 'Boulevard',
    'HTS': 'Heights',
    'HGTS': 'Heights',
    'SQ': 'Square',
    'ST': 'Street',
    'PKWY': 'Parkway',
    'PKY': 'Parkway',
}

lookup_direction = {
    'E': 'East',
    'W': 'West',
    'N': 'North',
    'S': 'South',
}

lookup_table = {}
lookup_table.update(lookup_suffix)
lookup_table.update(lookup_direction)

def search(line, lookup):
    for word in line.split(' '):
        word = word.upper()
        if word in lookup:
            return lookup[word]

def strip_road(line, lookup):
    line = line.split(' ')
    for word in line:
        word = word.upper()
        if word in lookup:
            line.pop(line.index(word))
    if line:
        return ' '.join(line).strip()


for item in client.ottawa.permits.find({}):
    road = item.get('ROAD')
    if road:
        suffix = search(road, lookup_suffix)
        direction = search(road, lookup_direction)
        route = strip_road(road, lookup_table)
        
        if suffix:
            item['suffix'] = suffix
        if direction:
            item['direction'] = direction
        if route:
            item['route'] = route

        client.ottawa.permits.save(item)