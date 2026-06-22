# import requests
# import time


# print("____Генератор шуток____")
# time.sleep(1)
# print("""Правила:
# 1. Просто читай шутки, ты можешь поставить лайк или дизлайк""")

# like_jokes = []
# dislike_jokes = []

# i = 0
# while True:
#     i += 1
#     url = "https://official-joke-api.appspot.com/random_joke"
#     responce = requests.get(url)
#     if responce.status_code == 200:
#         joke_dict = responce.json()
#         print(f"""
# Шутка {i}:
# Тип шутки: {joke_dict['type']} , 
# Шутка: {joke_dict['setup']} , {joke_dict['punchline']} ,
# ID шутки: {joke_dict['id']}""")
#         time.sleep(5)
#         like_dislike = input(f"Оцените {i}-ю шутку (1 - лайк, 2 - дизлайк): ")
#         if like_dislike == "1":
#             like_jokes.append(f"Шутка {i}: {joke_dict['setup']} , {joke_dict['punchline']}")
#         elif like_dislike == "2":
#             dislike_jokes.append(f"Шутка {i}: {joke_dict['setup']} , {joke_dict['punchline']}")
#         time.sleep(1)
#         stop = input("Хотите остановиться? (y - да, n - нет): ")
#         if stop == "y":
#             print(f"""
# Количество просмотренных шуток: {i} , 
# Понравившиеся шутки: {like_jokes} , 
# Непонравившиеся шутки: {dislike_jokes}""")
#             break
#         elif stop == "n":
#             continue
#     else:
#         print(f"Ошибка. Код статуса API {responce.status_code}")

