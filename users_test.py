from requests import get

print(get('http://127.0.0.1:5000/api/users').json())  # все правильно
print(get('http://127.0.0.1:5000/api/users/r'))  # некорректный id
print(get('http://127.0.0.1:5000/api/users/9999').json())  # несуществующий id
print(get('http://127.0.0.1:5000/api/users/2').json())  # приватный профиль
print(get('http://127.0.0.1:5000/api/users/1').json())  # все правильно
