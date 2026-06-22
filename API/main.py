# import requests
# import json

# # api = "https://v6.exchangerate-api.com/v6/488a5159e919278df08a79c7/latest/USD"

# # responce = requests.get(api)
# # if responce.status_code == 200:
# #     course_dict = responce.json()
# #     whole_course = course_dict["conversion_rates"]
# #     with open("exchange.json" , "w" , encoding='utf-8') as file:
# #          json.dump(str(whole_course) , file)
# #     print("=========Курс Доллара=========")
# #     print(f"""{whole_course["USD"]} доллар - {whole_course["EUR"]} евро
# # {whole_course["USD"]} доллар - {whole_course["KGS"]} сомов
# # {whole_course["USD"]} доллар - {whole_course["RUB"]} рублей""")
# #     print("=========Конвертатор в доллары=========")
# #     exchange = str(input("Введите волюту которуб хотите конвертировать(EUR , RUB , KGS): "))
# #     if exchange == "EUR":
# #         eur_usd = int(input("Введите количетсво евро: "))
# #         eur_to_usd = whole_course["USD"] / whole_course["EUR"]
# #         print(f"{eur_usd} евро - {eur_usd * eur_to_usd}")
# #     elif exchange == "RUB":
# #         eur_usd = int(input("Введите количетсво рублей: "))
# #         eur_to_usd = whole_course["USD"] / whole_course["RUB"]
# #         print(f"{eur_usd} рублей - {eur_usd * eur_to_usd}")
# #     elif exchange == "KGS":
# #         eur_usd = int(input("Введите количетсво сомов: "))
# #         eur_to_usd = whole_course["USD"] / whole_course["KGS"]
# #         print(f"{eur_usd} сомов - {eur_usd * eur_to_usd}")
# # else:
# #     print(responce.status_code)


# # api = "http://api.open-notify.org/astros.json"

# # response = requests.get(api)
# # if response.status_code == 200:
# #     people_dict = response.json()
# #     space_people = people_dict["number"]
# #     all_peopl_space = people_dict["people"]
# #     print(all_peopl_space)
# #     print(f"Количесво людей в космосе на данный момент: {space_people}")
# #     for person in all_peopl_space:
# #         print(f"Имя: {person['name']} (Корабль: {person['craft']})")
# #     final_data = {
# #         "name": all_peopl_space ,
# #         "total": space_people
# #     }
# #     with open("cosmos.json" , "a" , encoding='utf-8') as file:
# #       json.dump(str(final_data) , file)
# # else:
# #     print(response.status_code)
      
      
# import requests

# api = "http://api.open-notify.org/astros.json"
# response = requests.get(api)

# if response.status_code == 200:
#     data = response.json()
#     people = data["people"]
    
#     # 1. Создаем начало HTML-страницы
#     html_content = """
#     <html>
#     <head>
#         <meta charset="UTF-8">
#         <title>Космонавты в небе</title>
#         <style>
#             body { font-family: sans-serif; background: #1a1a2e; color: white; text-align: center; }
#             .card { background: #16213e; padding: 15px; margin: 10px; border-radius: 10px; display: inline-block; border: 1px solid #0f3460; }
#             h1 { color: #e94560; }
#             .card:hover{transform: translateY(4px); transition: 2s;}
#         </style>
#     </head>
#     <body>
#         <h1>Кто сейчас в космосе?</h1>
#     """

#     # 2. Добавляем карточки людей через цикл
#     for person in people:
#         html_content += f"""
#         <div class="card">
#             <h3>{person['name']}</h3>
#             <p>Корабль: {person['craft']}</p>
#         </div>
#         """

#     # 3. Закрываем теги
#     html_content += "</body></html>"

#     # 4. Сохраняем всё это в HTML файл
#     with open("index.html", "w", encoding="utf-8") as f:
#         f.write(html_content)
    
#     print("Готово! Открой файл index.html в браузере.")