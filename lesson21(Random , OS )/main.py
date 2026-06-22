# import random

# contries = ["Kyrgysztan" , "Kazahstan" , "Russian"]
# print(random.choice(contries))
# random.shuffle(contries)
# print(contries)

# print(random.randint(1 , 1000))

# # from datetime import datetime

# # now1 = datetime.now()
# # print(now1)
# # print(now1.day , now1.month , now1.year)
# # print(now1.hour , now1.minute)

# # print(now1.strftime("%H:%M:%S"))

# import os
# print(os.name)
# print(os.getcwd())
# print(os.listdir())
# os.mkdir("New_Folder")
# print(os.path.exists("New_Folder"))



# import random
# running = True
# while running:
#     user_thing = str(input("Введите ваш предмет: Камень, Ножницы или Бумага: "))
#     things = ["Камень" , "Ножницы" , "Бумага"]
#     random_thing = random.choice(things)
    
#     def usebot(number):
#         print(f"Ваш ввод: {user_thing}" * number)
#         print(f"Ввод бота: {random_thing}\n" * number)
#     if user_thing not in things:
#         print("Введен неправильный предмет!")
#     if random_thing == user_thing:
#         usebot(1)
#         print("Ничья")
#     elif user_thing == "Камень" and random_thing == "Ножницы" or \
#          user_thing == "Ножницы" and random_thing == "Бумага" or \
#          user_thing == "Бумага" and random_thing == "Камень":
#              usebot(1)
#              print("Вы выйграли!")
    
#     else:
#         usebot(1)
#         print("Вы проиграли")
        
    
    
import random
running = True
random_num = random.randint(1, 100)
print("======Угадайте число======")
print("Угадайте заданное число между 1 и 100")
while running:
    num = int(input("Введите число: "))
    if num < random_num:
        print("Введенное вами число меньше чем загаданное")
    elif num > random_num:
        print("Введенное вами число больше чем загаданное")
    elif num > 100:
        print("Извините число может быть максимум 100")
    elif num == random_num:
        print(f"Вы угадали!\n Число было {random_num}")