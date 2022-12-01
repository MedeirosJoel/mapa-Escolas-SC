import requests
from myConfig import KEY
url = f'http://www.mapquestapi.com/geocoding/v1/batch?key={KEY}'


data = """
{
    "locations": [
        {
            "location": 'Av. 15 de Novembro, 61 - Aeroporto, Araranguá - SC, 88905-112'
        },
        {
            "location": 'R. Abílio Geronimo Pereira, 9999 - Cidade Universitária, Araranguá - SC, 88705-240'
        }
    ],
    "options": {
        "maxResults": -1,
        "thumbMaps": true,
        "ignoreLatLngInput": false
    }
}
"""
headers = {}

response = requests.request("POST", url, headers=headers, data=data)
print(response.text)
