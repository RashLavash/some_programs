import requests



geo_api_server = 'http://geocode-maps.yandex.ru/1.x/'
geo_params = {
    'apikey': '39e26183-aaa8-4978-b294-d0b902ced272',
    'geocode': 'Махачкала',
    'format': 'json'
}
response = requests.get(geo_api_server, params= geo_params)
print(response.text)
json_response = response.json()
toponym = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']


print(toponym)
# print(toponym['Point']['pos'])

