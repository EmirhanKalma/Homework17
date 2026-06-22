# # # #If & Else Условия
# # # a = int(input("Enter your age: "))
# # # if a >= 18:
# # #     print("Okay , you are old enough.")
# # # elif a >= 80:
# # #     print("Amm , the programm think's that you are VERY old.")
# # # else:
# # #     print("Stop , you are young.")

# # # if True:
# # #     print("True")
# # # else:
# # #     print("False")

# # # # Python сравнивает строки посимвольно (лексикографически), 
# # # # используя коды Unicode для каждого символа.
# # # # 'H' (код 72) меньше, чем 'R' (код 82), 
# # # # поэтому условие 'Hello' > 'Roma' дает False.

# # # if 'Hello' > 'Roma': 
# # #     print("Странно1")
# # # else:
# # #     # Программа переходит сюда, так как 'H' идет в алфавите раньше 'R'
# # #     print("Странно2")

# # # # Если оба значения — строки, Python сравнивает их по кодам Unicode (UTF-8)
# # # # Код цифры '1' = 49
# # # # Код буквы 'Ф' = 1060
# # # # 49 НЕ больше 1060, поэтому "18" < "Фонарик"

# # # if "18" > "Фонарик":
# # #     print("Это не сработает")
# # # else:
# # #     print("Сработает это, так как 'Ф' в таблице Unicode стоит гораздо дальше")


# # # money = True
# # # if True:
# # #     print("Кайф")
# # # else:
# # #     print("Даа уж нормально :/ .")


# # #Exersice
# # work = int((input("Enter your age of working managment(ONLY NUMBERS): ")))
# # if work >= 3:
# #     print("You are hired!")
# # else:
# #     print("Sorry, but we can't hire you, but don't worry, you can come to our internship.")



# # correct_password = 1234567
# # password = input("Enter password: ")
# # if password == correct_password:
# #     print('Correct password')
# # else:
# #     print("Incorrcer password")















# #Exersice
# name = str(input("Enter your name: "))
# print("Hi , " + name)
# print("Okay , so Welcome to Stanford University")
# ilts = int(input("First , can you please enter your IELTS result's (if you didn't pass ILETS , WE CAN'T APROVE YOU : "))
# marks = int(input("Enter your average rating form school: "))
# olympiad = int(input("Enter the number of Olympiads you participated in: "))
# winolymo = int(input("Enter the number of Olympiads in which you won places: "))
# job = str(input("Enter the kob you want ot be on future: "))
# print("Okay , so let us think about your application...")


# import time

# def wait_five_seconds():
#     # Запоминаем время начала
#     start_time = time.time()
    
#     print("Начинаю процесс...")
    
#     # Цикл работает, пока не пройдет 5 секунд
#     while time.time() - start_time < 5:
#         for dots in [".  ", ".. ", "...", "   "]:
#             # Проверяем время еще и внутри цикла, чтобы выйти сразу
#             if time.time() - start_time >= 5:
#                 break
                
#             print(f"\rWait{dots}", end="", flush=True)
#             time.sleep(0.3) # Скорость анимации
            
#     # Чистим строку после завершения
#     print("\rГотово!          ")

# # Запуск
# wait_five_seconds()

    
# if ilts >= 7.5:
#     print("So you passed ilets very well.")
#     print("Entered: " , ilts)
# else:
#     print("You passed ilets not well , but let us see other results.")
#     print("Entered: " , ilts)

# if marks >= 4.5:
#     print("Amm yeah your marks are. very good")
#     print("Entered: " , marks)
# else:
#     print("You had not good marks , but nothing let's check other application.")
#     print("Entered " + marks)
   
    
# if olympiad >= 50:
#     print("Yeah you participated in a lot of olympiad's")
#     print("Entered: " , olympiad)
# else:
#     print("You didn't participate in many olympiads ,but nothing let's check other application.")
#     print("Entered " + olympiad) 
    
    
# if winolymo >= 30:
#     print("Yeah you won a lot of olympiad's")
#     print("Entered: " , winolymo)
# else:
#     print("You won in many olympiads ,but nothing let's check other application.")
#     print("Entered " + winolymo)   





if "Hello" > 1000 or 1000 < "hello": #Ну OR как бы если и ЕЩЕ КАК БЫ ТАК
    print("JKdjasda")