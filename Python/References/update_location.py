from pymongo import MongoClient

client = MongoClient()

for item in client.ottawa.permits.find({}):
    housenumber = item.get('housenumber')
    route = item.get('route')
    suffix = item.get('suffix')
    direction = item.get('direction')

    location = []
    if housenumber:
        location.append(str(housenumber))
    if route:
        location.append(route.title())
    if suffix:
        location.append(suffix)
    if direction:
        location.append(direction)

    item['location'] = ' '.join(location) + ', Ottawa'

    # Save MongoClient
    client.ottawa.permits.save(item)