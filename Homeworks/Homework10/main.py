import json



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


while True:
    user_command = input("""
1. Добавить новый контакт
2. Показать все контакты
3. Найти контакт
4. Удалить контакт
5. Выход
Выберите действие (1-5): """).strip()

    if user_command == "1":
        contact_name = input("Введите имя: ")
        contact_phone = input("Введите номер телефона: ")
        contact_email = input("Введите email: ")


        new_contact = {
            "name": contact_name,
            "phone": contact_phone,
            "email": contact_email
        }
        
    
        # indent - количетсво отступов(пробелов)
        indent=4
# Это отступы (количество пробелов).
# Зачем нужно: Без этого параметра JSON запишется в одну длинную-длинную строчку. Это неудобно читать человеку.
# Как работает: Число 4 говорит Python: «Сделай отступ в 4 пробела для каждого вложенного элемента».
# Результат: Благодаря этому твой файл в VS Code выглядит красиво и структурировано 
# , а не как сплошная каша из текста.
        try:
            with open("contacts.json", "r", encoding='utf-8') as file:
                current_contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            current_contacts = []
                
        current_contacts.append(new_contact)
        
        with open("contacts.json", "w", encoding='utf-8') as file:
            json.dump(current_contacts, file, indent=4 )
           
        print("Контакт успешно добавлен")

    elif user_command == "2":
        print("======================ВАШИ КОНТАКТЫ ======================")
        with open("contacts.json" , "r" , encoding='utf-8') as file:
            contact_list = json.load(file)
        for contact in contact_list:
            print(f"Имя: {contact['name']}, Номер: {contact['phone']}, Почта: {contact['email']}")
    elif user_command == "3":
        search_name = input("Введите имя контакта: ").lower()
        
        print("========================= Найденные контакты=========================== ")
        for contact in contact_list:
            if search_name == contact["name"].lower():
                print(f"Имя: {contact["name"]} Телефон: {contact["phone"]} Email: {contact["email"]}")
    elif user_command == "4":
        remove_name = input("Введите имя контакта: ").lower()
        
        for contact in contact_list:
            if remove_name == contact["name"].lower():
                contact_list.remove(contact)
    elif int(user_command) == 5:
        break

