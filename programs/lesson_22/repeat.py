import requests



my_params = {
    'id': 123
}
response = requests.get(
    'https://ru.wikipedia.org/wiki/',
    params=my_params
                        )

print(response.content)
print(response.status_code)
print(response.text)


post_data = {
    'fio': 'Magomedov M.M.',
    'age': 25
}
response = requests.post(
    'https://ru.wikipedia.org/wiki/',
    data=post_data )

print(response.text)