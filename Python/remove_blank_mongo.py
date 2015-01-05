from pymongo import MongoClient

client = MongoClient()

for item in client.ottawa.permits.find({}):
    save = False
    for keys, values in item.items():
        if not values:
            save = True
            del item[keys]

    if save:
        client.ottawa.permits.save(item)