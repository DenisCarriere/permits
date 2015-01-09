import os

folder = '/home/denis/Github/permits/JSON'

# Backup Geocoder results
for provider in ['osm','google','bing','nokia','mapquest','tomtom','arcgis']:
    os.system('mongoexport -d geocoder -c {provider} --out \
        {folder}/{provider}.json'.format(folder=folder, provider=provider))

# Backup Permits in MongoDB
os.system('mongoexport -d ottawa -c permits --out {folder}/permits.json'.format(folder=folder))