from pymongo import MongoClient

client = MongoClient()


container = []
permits = {}

for item in client.ottawa.permits.find({}):
    container.append(item)
    permit = item.get('PERMIT')
    if permit:
        if permits.get(permit):
            permits[permit] += 1
        else:
            permits[permit] = 1

for item in container:
    value = item.get('VALUE')
    ft2 = item.get('FT2')
    permit = item.get('PERMIT')
    count = permits.get(permit)

    if value:
        item['VALUE_unit'] = value / count
    if ft2:
        item['FT2_unit'] = ft2 / count
    if bool(value and ft2):
        item['COST_unit'] = float(value) / float(ft2)
    item['TOTAL_unit'] = count

    client.ottawa.permits.save(item)