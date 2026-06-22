import json

#r(read) означает чтение файлы
#w(write) означает создание файла
#a(append) означает вставить или вписать в файл
#utf-8 вид кодировки символов

# with open("message.txt" , "r" , encoding='utf-8') as file:
#     print(file.read())
    
# with open("new.txt" , "w" , encoding='utf-8') as file:
#     file.write("Hello world")
    
# with open("new.txt" , "a" , encoding='utf-8') as file:
#     file.write("\nHello") #\n означает перенос на новую строку
    
contact_list = [
    {
    "name": "Talgat",
    "phone": "0900100200",
    "email": "talgat@talgat.com"
    },
    {
    "name": "Akylai",
    "phone": "0900100200",
    "email": "talgat@talgat.com"
    },
    {
    "name": "Tahir",
    "phone": "0900100200",
    "email": "talgat@talgat.com"
    },
]

with open("contacts.json" , "w" , encoding='utf-8') as file:
    json.dump(contact_list , file)
    
with open("contacts.json" , "r" , encoding='utf-8') as file:
    contact_list = json.load(file)
    print(f"""
Первый контакт: {contact_list[0]}
Второй контакт: {contact_list[1]}
Третий контакт: {contact_list[2]}"""
              .strip())