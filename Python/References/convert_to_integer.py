from pymongo import MongoClient
import re


client = MongoClient()
db = client.ottawa.permits

for item in db.find({}):
    for key in ['VALUE','housenumber','year','PERMIT','FT2','DU']:    
        value = str(item[key])

        # Only find the first set of numbers
        expression = r"-?\d+"
        pattern = re.compile(expression)
        match = pattern.search(value)
        if match:
            value = match.group()
        
        if value:
            item[key] = int(value)

    db.save(item)