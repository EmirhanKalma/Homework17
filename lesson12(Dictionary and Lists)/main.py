# dictionary = {
#     "name": "Timur",
#     "age": 12
# }#Здесь это список и он отличается от массива
# arr = [
#     'Timur' ,
#     12
# ]#Это массив

# # print(arr[0])#Тут тоже разница чтобы нам распечатать имя Timur нужно обращаться к нему по индексу
# # print(dictionary["age"])#А вот здесь нам нужно обращаться по перемнной age чтобы распечатать возвраст


# #Создадим например список паспорт там мы указываем все что нужно
# passport_list = {
#     "name": "Emirhan",
#     "age": 12 ,
#     "boy": True
# }
# #Теперь создадим массив тоже нашего паспорта 
# passport_massive = [
#     "Emirhan" ,
#     12 , 
#     True
# ]

# print(passport_list["name"])#И вот здесь и стоит главное отличие чтобы нам ввывести имя с пасорта в 
# #списке нужно указать как ы подназвание переменной ну она у нас name и туту понятно
# print(passport_massive[0])#А вот здесь тяжело разобраться чтобы вывести имя нужно знать индекс имени и тогда мы и сможем легко 
# #вывести имя , но вот если у нас прям много там типов данных в списке напрмиер 2000 и имя где-то 
# #там поэтому массив именно здесь проигравает

# # Emirhan = {
# #     "username" : "Emi(O_O)" , 
# #     "real_name" : "Emirhan" ,
# #     "followers_number" : "34" , 
# #     "following" : "17" , 
# #     "like_record" : "1,200,434"
# # }
# # print(Emirhan["real_name"])

student = {
    "name" : "Emirhan Kalmamatov" ,
    "grade": "7-B" ,
    "age" : 13 ,
    "school" : "Kelechek MiT" , 
    "marks" : {
        "math" : [2, 3 ,2 , 2 , 2 , 2 , 2] ,
        "russian" : [2, 3 ,2 , 2 , 2 , 2 , 2] 
    }
}

marks_emirhan = {
    "math" : [ 5 , 5 , 5 , 5 , 5 , 5 , 5 ] ,
    "english" : [5 , 5 , 5 , 5 , 5 , 5 , 5 , 5] ,
    "russian" : [5 , 5 , 5 , 5 , 5 , 5 , 5 , 5]
}


print(student["name"])
student["grade"] = "11 - A"



del student["school"]
print(student)

student["marks"]["math"] = [5 , 5 , 5 , 5 , 5 , 5 , 5]
print(student)

servers = {
    "google.com" : "123.456.789.101"
}


wheather = {
    "temperature" : "12"
    "...."
}


stock_data = {
    "coin_name" : "bitcoin" , 
    "price_usd" : 60000 ,
    "date" : "18.04.26" ,
    "time" : "18:42:34 PM"
}

bus_data = {
    "bus_name" : 10 ,
    "location" : {
        "lattitude" : 100,
        "longtude" : 60
    }
}