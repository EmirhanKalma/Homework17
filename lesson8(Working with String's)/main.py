# #Строки

# string = "Arbuzz"

# print(string[0])
# print(string[-1])
# print(string[2:5])
# print(string[::-1])

# cart = ["Apple" , "Milk" , "Potato"]
# cart_reversed = cart[::-1]
# print(cart.reverse())

# message = 'privet sosed'
# print(message.upper())#Делает все буквы в слове маленькими

# message2 = "WHERE ARE YOU"
# print(message2.lower())#Делает все буквы в  слове маленьким

# name = "emirhan and rmirhan"
# print(name.capitalize()) #Делает первую букву слова ЗАГЛАВНОЙ 

# book = 'war and peace'
# print(book.title()) # Также работает только уже во всех словах делает первую букву заглавной во всей строке

# spaces = '                                         space                        '
# print(spaces)
# print(spaces.strip()) #Удаляет все пробелы в строке

# text = 'Давным давно в тридевятом царстве жил царь Гвидон'
# print(text.replace("Гвидон" , "Секретная информация")) #Заменяет гвидон на Секретная информация

# student = ["Эмирхан" , "Адилет" , "Бакай" , "сардар"]

# name = "Сардар"
# if name.lower or name.upper or name.capitalize or name.strip:
#     print("""
# Цель найдена! Вызываем полицию,Национальную гвардию, Военных, 
# Скорую, Пожарных, Спецназ, Призедента, Прьмьер-Министра обороны ,
# авианосцы, танкеры. По сигналу будет сброшена атомная бомба.
#           """.strip())

# if "Сардар" in student:
#     print("Цель найдена!")




# number = input("Введите число: ")

# if number.isdigit(): #isdigit() проверяет является строка числом
#     print("Правльно")
# else:
#     print("Вы ввели строку или другой формат")
    
    
# name = input("Введите имя: ")

# if not name.isalpha():#isalpha() проверяет есть ли в строке число,символы тогда False , а если только буквы то True
#     print("Несанкцанированое имя")
# else:
#     print("Все верно имя найденно на сервере")
    
    
# string = "Apple"
# string_list = ["a" , "b" , "c"]


# print(string_list[-1])


string = "Azbuka"
print(string.split('A  a'))

number = "101010"
print(number.split("0"))

name = 'samat'
print(name.split("m"))