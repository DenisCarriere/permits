from pymongo import MongoClient
import os


client = MongoClient()

lookup_suffix = {
    'GT': 'Gate',
    'DRWY': 'Driveway',
    'DR': 'Drive',
    'DR.': 'Drive',
    'PL': 'Place',
    'CIR': 'Circle',
    'CIRC': 'Circle',
    'CREEK': 'Creek',
    'PRIV': 'Private',
    'RD': 'Road',
    'RD.': 'Road',
    'CRES': 'Crescent',
    'AVE': 'Avenue',
    'AVE.': 'Avenue',
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
    'STE': 'Saint',
    'STE.': 'Saint',
    'PKY': 'Parkway',
    'GROVE': 'Grove',
    'WAY': 'Way',
    'RIDGE': 'Ridge',
    'LANE': 'Lane',
    'SIDE': 'Side',
    'PARK': 'Park',
    'CREST': 'Crest',
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
    words = line.split(' ')
    container = [words[0]]
    for word in words[1:]:
        word = word.upper()
        if not word in lookup:
            container.append(word)
    if container:
        return ' '.join(container)
    else:
        # Only return the first word
        if words:
            return words[0] 


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
            item['route'] = route.title()
        client.ottawa.permits.save(item)