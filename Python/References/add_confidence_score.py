from pymongo import MongoClient
from haversine import haversine

client = MongoClient()
db = client.ottawa.geocoder

def confidence_score(km):
    # Score is less than maximum
    for score, maximum in [
        (10, 0.25),
        (9, 0.5),
        (8, 1),
        (7, 5),
        (6, 7.5),
        (5, 10),
        (4, 15),
        (3, 20),
        (2, 25)]:
        if km < maximum:
            return score
    # Greater than 25km
    if isinstance(km, (float,int)):
        return 1
    # Cannot determine score
    return 0

for provider in ['google']:
    for item in db[provider].find({'properties.confidence':{'$not':{'$gte':0}}}):
        bbox = item.get('bbox')
        confidence = 0
        if bbox:
            southwest = (bbox[1], bbox[0])
            northeast = (bbox[3], bbox[2])
            km = haversine(northeast, southwest)
            confidence = confidence_score(km)

        # Save in MongoDB
        item['properties']['confidence'] = confidence
        db[provider].save(item)