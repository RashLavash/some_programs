import requests


# Get-запрос к серверу

# response = requests.get('http://127.0.0.1:8000')
# response.encoding = 'UTF-8'
# print(response.text)

# Post-запрос к серверу
my_data = {
    'name': 'Rashid',
    'age': '20'
}


response = requests.post('http://127.0.0.1:8000', data=my_data)
response.encoding = 'UTF-8'
print(response.text)

