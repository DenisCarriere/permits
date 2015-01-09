import os
import re
import unicodecsv
from pymongo import MongoClient

# Create Mongo connection
client = MongoClient()
db = client.ottawa

# Erase Existing dataset
db.permits.remove({})

# Crawl all files within this Folder
for root, folder, files in os.walk('/home/denis/Github/permits/CSV'):
    for file_name in files:
        path = os.path.join(root, file_name)

        # Open each file
        with open(path) as f:
            reader = unicodecsv.DictReader(f, encoding='utf-8')
            for line in reader:
                # Add Extra Meta Tags
                null, year = os.path.split(root)
                line['year'] = year
                line['file_name'] = file_name

                # Georeferencing Attributes
                housenumber = line.get('ST')
                street_name = line.get('ROAD')
                city = 'Ottawa'

                # Remove Units from Housenumber (Ex: 228-A >> 228)
                expression = r"\w+"
                pattern = re.compile(expression)
                match = pattern.findall(housenumber)
                if len(match) == 2:
                    housenumber = match[0]
                    unit = match[1]
                    line['housenumber'] = housenumber
                    line['unit'] = unit
                else:
                    line['housenumber'] = housenumber

                # Location will be used for the single input when georeferencing
                if bool(housenumber and street_name):
                    location = u'{0} {1}, {2}'.format(housenumber, street_name, city)
                    line['location'] = location

                # Add each line in MongoDB
                db.permits.insert(line)

print 'Added rows MongoDB:', db.permits.count()