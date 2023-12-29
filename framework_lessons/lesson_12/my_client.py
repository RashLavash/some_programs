from requests import get, post, put, delete


print(get('http://localhost:8000/posts').json())
print(post('http://localhost:8000/posts', json={'text': 'Rash'}).json())

# print(get('http://localhost:8000/posts/1').json())
# print(put('http://localhost:8000/posts/1', json={'name': 'Rash'}).json())
# print(delete('http://localhost:8000/posts/1').json())


