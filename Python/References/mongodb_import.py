import os

folder = '/home/denis/Github/permits/JSON'


# Import Geocoder results
for provider in ['osm','google','bing','nokia','mapquest','tomtom','arcgis']:
    os.system('mongoimport -d geocoder -c {provider} --drop --file \
        {folder}/{provider}.json'.format(folder=folder, provider=provider))

# Import Permits in MongoDB
os.system('mongoimport -d ottawa -c permits --file {folder}/permits.json --drop'.format(folder=folder))