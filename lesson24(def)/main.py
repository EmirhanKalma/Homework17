# def check_age():
    
#     try:
#         age = int(input("Введите ваш возвраст: "))
#         if age <= 18:
#             print("Маленький")
#             return False
#         elif age >= 18:
#             print("Можно")
#             return True
#         else:
#             print("Слишком мал")
#             return False
#     except ValueError:
#         print("Вы ввели неправльный ти данных.")
#         return False


# if check_age() == True:
#     print("Проходите")
# else:
#     print("Вход запрещен")

    
# def say_hello(name):
#     print(f"Hello {name}")
    
# say_hello("Emirhan")

# def create_business_card(name , profession):
#     card = f"Имя: {name} , Проффесия:  {profession}"
#     return card

# def check_password(password):
#     if len(password) >= 8:
#         for letter in password:
#             if letter.isdigit():
#                 return True
#             else:
#                 return False
        
#     elif len(password) < 8:
#         for letter in password:
#             if letter.isdigit():
#                 return True
#             else:
#                 return False
            
# check_password("Hello12")
# print(check_password("Hello1234"))


# def get_receipt_stats(*args):
#     try:
#         reciept_check = {
#             "total": sum(args) ,
#             "max_price": max(args) ,
#             "count": len(args)
#         }
#         return reciept_check
#     except ValueError:
#         print("Введен неверный тип данных")


def process_data(numbers, action): 
    res = []
    for num in numbers:
        new_num = action(num)
        res.append(new_num)
        
    return res

my_list = [10, 20, 30]
result = process_data(my_list, lambda x: x / 2)
print(result) 

@logger
def add_numbers(a, b):
    return a + b
print("Вызываем функцию")
add_numbers(5, 7)
print("Функция завершина")