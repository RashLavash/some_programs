import requests


youtube_url = 'https://www.youtube.com/results'
youtube_query = {
    'search_query': 'bmw'
}

response = requests.get(youtube_url, params= youtube_query)
print(response.url)
print(response.status_code) 
# print(response.text) 
# print(json_response)