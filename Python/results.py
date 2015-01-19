from pymongo import MongoClient
from haversine import haversine


client = MongoClient()

def find_errors():
    count = 0
    for item in client.geocoder.ottawa.find({}):
        location = item['properties']['location']
        google = client.geocoder.google.find_one({'properties.location':location})
        confidence = google['properties']['confidence']
        if not confidence >= 8:
            ottawa = client.ottawa.permits.find_one({'location':location})
            print 'ERROR',location, ottawa['CONTRACTOR']

def contractor(name):
    count = 0
    errors = 0
    for item in client.ottawa.permits.find({}):
        location = item['location']
        contractor = item.get('CONTRACTOR','').lower()
        if name in contractor:
            count += 1
            google = client.geocoder.google.find_one({'properties.location':location})
            ottawa = client.geocoder.ottawa.find_one({'properties.location':location, 'properties.lat':{'$exists':1}})
            confidence = google['properties']['confidence']
            city = google['properties'].get('city')
            
            lat, lng = google['properties'].get('lat'), google['properties'].get('lng')

            if bool(ottawa and lat):
                latlng2 = ottawa['properties']['lat'], ottawa['properties']['lng']
                distance = haversine([lat, lng], latlng2) * 1000
            else:
                distance = 50000
            

            if not city == 'Ottawa':
                print 'CITY ERROR:',city, location
            elif not lat:
                print 'NO COORD:', location
            elif distance >= 250:
                print 'DISTANCE ERROR:', distance, location
                errors += 1

            elif confidence < 8:
                print 'CONFIDENCE ERROR:', confidence, location
                errors += 1


    print name, ':',count
    print 'Errors:', errors

def calculate_distance():
    ottawa = {}
    for item in client.geocoder.ottawa.find({'properties.lat':{'$exists':1}}):
        location = item['properties']['location']
        latlng = item['properties']['lat'], item['properties']['lng']
        ottawa[location] = latlng

    google = {}
    for item in client.geocoder.google.find({'properties.lat':{'$exists':1}}):
        location = item['properties']['location']
        confidence = item['properties']['confidence']
        latlng = item['properties']['lat'], item['properties']['lng']
        try:
            distance = haversine(ottawa.get(location), latlng) * 1000
        except:
            print location
            distance = 99999
            client.geocoder.google.remove(item)

def municipality_builder(municipality, builder):
    search = {
        'permits.CONTRACTOR': builder,
        'permits.MUNICIPALITY': municipality
    }
    count = 0
    for item in client.geocoder.google.find(search):
        confidence = item['properties']['confidence']
        location = item['properties']['location']
        if confidence < 8:
            count += 1
            print location
    print 'Total:', count

    
if __name__ == '__main__':
    #find_errors()
    #contractor('greenmark')
    #calculate_distance()
    municipality_builder('Cumberland','TAMARACK DEVELOPMENTS CORPORATION')