import requests
from myConfig import KEY
pre_location = '&location='

enderecos = ['AVENIDA UNIVERSITARIA, 345 - UNIVERSITARIO, CRICIÚMA - SC, 88806000',
'BR 282 KM 246, 0 - ITARARE, SÃO JOSÉ DO CERRITO - SC, 88570000',
'FAZENDA PRIMAVERA SC 160 KM 07, 0 - INTERIOR, CAMPO ERÊ - SC, 89980000',
'R MONSENHOR GERCINO, 2071 - ITAUM, JOINVILLE - SC, 89210155',
'R ASSIS BRASIL, 119 - MARIA GORETTI, CHAPECÓ - SC, 89801222']

all_enderecos = ''
for endereco in enderecos:
    all_enderecos += pre_location+endereco

url = f'http://www.mapquestapi.com/geocoding/v1/batch?key={KEY}{all_enderecos}'

data = """
{
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

