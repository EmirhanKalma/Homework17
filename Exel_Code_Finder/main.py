file_name = "data.txt"
running = True
founded_codes = []
unknown_codes = []
while running:
    finder = input(f"Введите сроку которую хотите найти в файле (0 - Выйти){file_name}: ")
    
    if finder == "0":
        running = False
        if founded_codes: # Проверяем, есть ли вообще что записывать
            with open("founded_codes.txt", 'a', encoding='utf-8') as file:
                for code in founded_codes:
                    file.write(code + '\n') # Пишем каждый код с новой строчки
                    
        # Записываем неизвестные коды (режим 'a')
        if unknown_codes:
            with open("unknown_codes.txt", 'a', encoding='utf-8') as file:
                for code in unknown_codes:
                    file.write(code + '\n')
        
        print(f"Найденные коды: {founded_codes}")
        print(f"Ненайденные коды: {unknown_codes}")
    
    elif finder:
            with open(file_name , 'r' , encoding='utf-8') as file:
                string_find = file.read()
                if finder in string_find:
                    founded_codes.append(finder)
                    print(f"Строка есть в файле {file_name}")
                else:
                    unknown_codes.append(finder)
                    print(f"ОШИБКА: Строка {finder} не найдена в файле {file_name}")

    
    else:
         print("ОШИБКА")