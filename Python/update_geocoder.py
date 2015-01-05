from pymongo import MongoClient

client = MongoClient()


container = {}

for item in client.ottawa.permits.find({},{'_id':0}):
    permit = item.get('PERMIT')
    housenumber = item.get('housenumber')
    if container.get(permit):
        container[permit].update({housenumber:item})
    else:
        container[permit] = {housenumber: item}

for provider in ['bing','nokia', 'mapquest','tomtom','arcgis','opencage']:
    for item in client.geocoder[provider].find({}):
        properties = item.get('properties')
        try:
            housenumber = int(properties.get('housenumber'))
        except:
            housenumber = None
        try:
            permit = int(properties.get('PERMIT'))
        except:
            permit = None

        if bool(permit and housenumber):
            
            ottawa = container.get(permit).get(housenumber)
            
            if ottawa:
                item['properties'].update(ottawa)
                client.geocoder[provider].save(item)
