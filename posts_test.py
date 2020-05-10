from requests import get

print(get('http://127.0.0.1:5000/api/posts').json())  # все правильно
print(get('http://127.0.0.1:5000/api/posts/r'))  # некорректный id
print(get('http://127.0.0.1:5000/api/posts/9999').json())  # несуществующий id
print(get('http://127.0.0.1:5000/api/posts/2').json())  # приватный пост
print(get('http://127.0.0.1:5000/api/posts/1').json())  # все правильно
