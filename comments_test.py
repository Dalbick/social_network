from requests import get

print(get('http://127.0.0.1:5000/api/comments').json())  # все правильно
print(get('http://127.0.0.1:5000/api/comments/r'))  # некорректный id
print(get('http://127.0.0.1:5000/api/comments/9999').json())  # несуществующий id
print(get('http://127.0.0.1:5000/api/comments/1').json())  # все правильно
