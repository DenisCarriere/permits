from pymongo import MongoClient

client = MongoClient()

for item in client.ottawa.permits.find({'unit':{'$exists':True}}):
    unit = item.get('unit')
    try:
        item['unit'] = int(unit)
        save = True
    except:
        save = False
    
    if save:
        client.ottawa.permits.save(item)
