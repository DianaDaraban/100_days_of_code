import datetime

import requests
pixela_endpoint = 'https://pixe.la/v1/users'
PIXELA_TOKEN = 'Tangodeedee_12!'
PIXELA_USERNAME ='dianadaraban'

pixela_params = {
    'token':PIXELA_TOKEN,
    'username':PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor':'yes',
}
response = requests.post(url=pixela_endpoint, json=pixela_params)

graph_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs'

graph_config = {
    'id':'graph1',
    'name':'Cycling Graph',
    'unit':'Km',
    'type':'float',
    'color':'momiji'
}

headers = {
    'X-USER-TOKEN': PIXELA_TOKEN
}
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

graph_value_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{graph_config['id']}'

today = datetime.datetime.now()
graph_value_params = {
    'date': f'{today.strftime('%Y%m%d')}',
    'quantity': '10.5',
}

value_response = requests.post(url=graph_value_endpoint, headers=headers, json=graph_value_params)

print(value_response.text)