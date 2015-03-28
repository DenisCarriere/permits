import requests


headers = {
    'Host': 'maps.ottawa.ca',
    'Origin': 'http://maps.ottawa.ca'
}
url = 'http://maps.ottawa.ca/GeoOttawaReports/Reports/Report.aspx?reportName=PropertyInformation&Municipal_Address_Id=%27___A552E%27&extent=-8427741.5302%2c5685492.849100001%2c-8427700.7635%2c5685517.659199998&sr=3857'
r = requests.get(url, headers=headers)

print(r.content)