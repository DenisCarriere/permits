import os
import unicodecsv
from pymongo import MongoClient

# Create Mongo connection
client = MongoClient()
db = client.ottawa

# Erase Existing dataset
db.permits.remove({})

# Crawl all files within this Folder
for root, folder, files in os.walk('/home/ubuntu/Github/permits/CSV'):
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

                # Add each line in MongoDB
                db.permits.insert(line)

print 'Added rows MongoDB:', db.permits.count()