from pymongo import MongoClient

client = MongoClient()


for provider in ['osm','opencage','arcgis','bing','google','nokia','mapquest','tomtom']:
    db = client.geocoder[provider]
    for item in db.find({}):
        geom = item.get('geometry')
        if geom:
            coord = geom.get('coordinates')
            if coord:
                lng, lat = coord
                item['properties']['lat'] = lat
                item['properties']['lng'] = lng
                db.save(item)