from requests import get, post, put, delete


# print(get('http://localhost:8000/posts').json())
# print(get('http://localhost:8000/posts/1').json())
# print(post(
#     'http://localhost:8000/posts',
#     json={
#         'title': 'Заголовок 3',
#         'text': 'Текст публикации 3',
#         'author_id': 3
#         }).json())

print(get('http://localhost:8000/posts').json())
# print(put(
#     'http://localhost:8000/posts/1', 
#     json={
#         'title': 'Измененный заголовок',
#         'text': 'Измененный text',
#         'author_id': 5
#         }
#     ).json())
# print(delete('http://localhost:8000/posts/1').json())