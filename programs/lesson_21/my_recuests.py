import requests

# Пример запроса сайта
# response = requests.get('https://www.youtube.com/')
# print(response)
# print(response.status_code)
# print(response.content)
# print(response.text)

# response = requests.get('https://static-maps.yandex.ru/v1?ll=28.978178,41.011218&spn=0.016457,0.00619&l=map&apikey=YOUR_API_KEY')
# print(response)


api_server = 'https://static-maps.yandex.ru/1.x/'
map_params = {
    'll': '28.978178,41.011218', 
    'spn': '0.016457,0.00619', 
    'l': 'map'
}

response = requests.get(api_server, map_params)
print(response.text)