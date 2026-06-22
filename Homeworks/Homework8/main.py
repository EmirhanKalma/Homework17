#1
# import requests

# url = "https://google.com"
# while True:
#     responce = requests.get(url)
#     if responce.status_code == 200:
#         print("Запрос Успешно отправлен!")
#     else:
#         print(f"Ошибка: {responce.status_code}")
        


#2
# import requests
# url = "https://jsonplaceholder.typicode.com/invalid_page."
# while True:
#     responce = requests.get(url)
#     if responce.status_code == 404:
#         print("Страница не найдена")

#3
# import requests
# url = "https://catfact.ninja/fact"
# responce = requests.get(url)
# if responce.status_code == 200:
#     cat_json = responce.json()
#     print(cat_json["fact"])

#4
# while True:
#   import requests
#   url = "https://dog.ceo/api/breeds/image/random"
#   responce = requests.get(url)
#   if responce.status_code == 200:
#       cat_json = responce.json()
#       print(cat_json["message"])