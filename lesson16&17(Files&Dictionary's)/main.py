# import json

# message = """
# Это приложение для хранения контактов.
# """

# contact_list = [
#     {
#     "name": "Talgat",
#     "phone": "0900100200",
#     "email": "talgat@talgat.com"
#     },
#     {
#     "name": "Akylai",
#     "phone": "0900100200",
#     "email": "talgat@talgat.com"
#     },
#     {
#     "name": "Tahir",
#     "phone": "0900100200",
#     "email": "talgat@talgat.com"
#     },
# ]
# print(message)

# while True:
#     user_command = input("""
# Выберите действие.
# 1 - добавить контакт
# 2 - посмотреть все контакты
# 3 - поиск контактов
# 4 - удалить по имени
#         """).strip()

#     if user_command == "1":
#         contact_name = input("Введите имя:")
#         contact_phone = input("Введите номер телефона:")
#         contact_email = input("Введите email:")
        
#         new_contact = {
#             "name": contact_name,
#             "phone": contact_phone,
#             "email": contact_email
#         }
        
#         with open("contacts.json" , "a" , encoding='utf-8') as file:
#             file.write(new_contact)
#         print("Контакт успешно добавлен")

#     elif user_command == "2":
#         print("======================ВАШИ КОНТАКТЫ ======================")
#         with open("contacts.json" , "r" , encoding='utf-8') as file:
#             contact_list = json.load(file)
#         for contact in contact_list:
#             print(f"Имя: {contact['name']}, Номер: {contact['phone']}, Почта: {contact['email']}")
#     # elif user_command == "3":
#     #     search_name = input("Введите имя контакта: ").lower()
        
#     #     print("========================= Найденные контакты=========================== ")
#     #     for contact in contact_list:
#     #         if search_name == contact["name"].lower():
#     #             print(f"Имя: {contact["name"]} Телефон: {contact["phone"]} Email: {contact["email"]}")
#     # elif user_command == "4":
#     #     remove_name = input("Введите имя контакта: ").lower()
        
#     #     for contact in contact_list:
#     #         if remove_name == contact["name"].lower():
#     #             contact_list.remove(contact)


with open("result.txt" , "r" , encoding='utf-8') as file:
    for line in file:
        names = []
        scores = []
        line_arr = line.split(": ")
        
    
