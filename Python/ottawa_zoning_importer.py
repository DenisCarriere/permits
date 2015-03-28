#!/usr/bin/python
# coding: utf8

import json
import requests
from geojson import Polygon

lookup_part = {
    6: {'description': 'Residential Zones', 'sections': '155-168'},
    7: {'description': 'Institutional Zones', 'sections': '169-172'},
    8: {'description': 'Open Space and Leisure Zones', 'sections': '173-180'},
    9: {'description': 'Environmental Zones', 'sections': '183-184'},
    10: {'description': 'Mixed Use / Commerical Zones', 'sections': '185-198'},
    11: {'description': 'Industrial Zones', 'sections': '199-206'},
    12: {'description': 'Transportation Zones', 'sections': '207-210'},
    13: {'description': 'Rural Zones', 'sections': '211-236'},
    14: {'description': 'Other Zones', 'sections': '237-238'},
}
lookup_subzoning = {
    'R1': ['R1%s' % chr(x) for x in range(ord('A'), ord('Z') + 1)],
    'R2': ['R2%s' % chr(x) for x in range(ord('A'), ord('Z') + 1)],
    'R3': ['R3%s' % chr(x) for x in range(ord('A'), ord('Z') + 1)],
    'R4': ['R4%s' % chr(x) for x in range(ord('A'), ord('Z') + 1)],
    'R5': ['R5%s' % chr(x) for x in range(ord('A'), ord('Z') + 1)],
    'O1': ['O1%s' % chr(x) for x in range(ord('A'), ord('S') + 1)],
    'RI': ['RI%i' % x for x in range(1, 9)],
    'RU': ['RU%i' % x for x in range(1, 5)],
    'AG': ['AG%i' % x for x in range(1, 9)],
    'IL': ['IL%i' % x for x in range(1, 10)],
}

lookup_zoning = {
    'R1': {'part': 6, 'description': 'Residential First Density Zone', 'sections': '155-156'},
    'R2': {'part': 6, 'description': 'Residential Second Density Zone', 'sections': '157-158'},
    'R3': {'part': 6, 'description': 'Residential Third Density Zone', 'sections': '159-160'},
    'R4': {'part': 6, 'description': 'Residential Fourth Density Zone', 'sections': '161-162'},
    'R5': {'part': 6, 'description': 'Residential Fifth Density Zone', 'sections': '163-164'},
    'RM': {'part': 6, 'description': 'Mobile Home Zone', 'sections': '167-168'},
    'I1': {'part': 7, 'description': 'Minor Institutional Zone', 'sections': '169-170'},
    'I2': {'part': 7, 'description': 'Major Institutional Zone', 'sections': '171-172'},
    'L1': {'part': 8, 'description': 'Community Leisure Facility Zone', 'sections': '173-174'},
    'L2': {'part': 8, 'description': 'Major Leisure Facility Zone', 'sections': '175-176'},
    'L3': {'part': 8, 'description': 'Central Experimental Farm', 'sections': '177'},
    'O1': {'part': 8, 'description': 'Parks and Open Space Zone', 'sections': '179-180'},
    'EP': {'part': 9, 'description': 'Environmental Protection Zone', 'sections': '183-184'},
    'AM': {'part': 10, 'description': 'Arterial Mainstreet Zone', 'sections': '185-186'},
    'GM': {'part': 10, 'description': 'General Mixed Use Zone', 'sections': '187-188'},
    'LC': {'part': 10, 'description': 'Local Commercial Zone', 'sections': '189-190'},
    'MC': {'part': 10, 'description': 'Mixed-Use Centre Zone', 'sections': '191-192'},
    'MD': {'part': 10, 'description': 'Mixed-Use Downtown Zone', 'sections': '193-194'},
    'TD': {'part': 10, 'description': 'Transit Oriented Development Zone', 'sections': '195-196'},
    'TM': {'part': 10, 'description': 'Traditional Mainstreet Zone', 'sections': '197-198'}, 
    'IG': {'part': 11, 'description': 'General Industrial Zone', 'sections': '199-200'},
    'IH': {'part': 11, 'description': 'Heavy Industrial Zone', 'sections': '201-202'},
    'IL': {'part': 11, 'description': 'Light Industrial Zone', 'sections': '203-204'},
    'IP': {'part': 11, 'description': 'Business Park Industrial Zone', 'sections': '205-206'},
    'T1': {'part': 12, 'description': 'Air Transportation Facility Zone', 'sections': '207-208'},
    'T2': {'part': 12, 'description': 'Ground Transportation Zone', 'sections': '209-210'},
    'AG': {'part': 13, 'description': 'Agricultural Zone', 'sections': '211-212'},
    'ME': {'part': 13, 'description': 'Mineral Extraction Zone', 'sections': '213-214'},
    'MR': {'part': 13, 'description': 'Mineral Aggregate Reserve Zone', 'sections': '215-216'},
    'RC': {'part': 13, 'description': 'Rural Commercial Zone', 'sections': '217-218'},
    'RG': {'part': 13, 'description': 'Rural General Industrial Zone', 'sections': '219-220'},
    'RH': {'part': 13, 'description': 'Rural Heavy Industrial Zone', 'sections': '221-222'},
    'RI': {'part': 13, 'description': 'Rural Institutional Zone', 'sections': '223-224'},
    'RR': {'part': 13, 'description': 'Rural Residential Zone', 'sections': '225-226'},
    'RU': {'part': 13, 'description': 'Rural Countryside Zone', 'sections': '227-228'},
    'VM': {'part': 13, 'description': 'Village Mixed-Use Zone', 'sections': '229-230'},
    'V1': {'part': 13, 'description': 'Village Residential First Density Zone', 'sections': '231-232'},
    'V2': {'part': 13, 'description': 'Village Residential Second Density Zone', 'sections': '233-234'},
    'V3': {'part': 13, 'description': 'Village Residential Third Density Zone', 'sections': '235-236'},
    'DR': {'part': 14, 'description': 'Development Reserve Zone', 'sections': '237-238'},
}

# GeoJSON format
collection = {
    "type": "FeatureCollection",
    "features": []
}

# Loop threw all Zonings
for zoning in lookup_zoning.keys():
    location = zoning
    """
    for subzoning in lookup_subzoning.get(zoning, [zoning]):
        if subzoning:
            location = subzoning
        else:
            location = zoning
    """
    # URL Request to GeoOttawa Services
    url = 'http://maps.ottawa.ca/arcgis/rest/services/Zoning/MapServer/find'
    params = {
        'searchText': location,
        'layers': 3,
        'f': 'json',
        'sr': 4326,
    }
    r = requests.get(url, params=params)
    results = r.json()['results']
    print('Requesting Zoning: %s (count %i)' % (location, len(results)))

    # Loop threw each feature
    for item in results:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': Polygon(item['geometry']['rings'])['coordinates']
            },
            'properties': {
                'zoning_main': item['attributes']['ZONE_MAIN'],
                'zoning_code': item['attributes']['ZONE_CODE'],
                'zoning_parent': item['attributes']['PARENTZONE'],
                'zoning_description': lookup_zoning[zoning[:2]]['description'],
                #'subzoning': subzoning,
                'sections': lookup_zoning[zoning[:2]]['sections'],
                'part': lookup_zoning[zoning[:2]]['part'],
                'part_description': lookup_part[lookup_zoning[zoning[:2]]['part']]['description'],
                'date': item['attributes']['CONS_DATE'],
                'object_id': item['attributes']['OBJECTID_12'],
            }
        }
        # Store feature into GeoJSON collection
        collection['features'].append(feature)

# Save file
with open('/home/denis/GIS/Ottawa_Zoning.json', 'w') as f:
    f.write(json.dumps(collection))
