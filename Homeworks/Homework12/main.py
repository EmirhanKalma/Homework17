#1
with open("hello.txt" , "w" , encoding='utf-8') as file:
    file.write("hellow world")
    
#2
with open("hello.txt" , "r" , encoding='utf-8') as file:
    print(file.read())
    
#3
name = str(input("Введите имя файла: ")) 
with open(name , "r" , encoding='utf-8') as file:
    lines = file.readlines() # Создает список из всех строк
    count = len(lines)
    print(f"Количество строк в файле {name}: {count}")
    
#4
name = str(input("Введите имя файла: ")) 
with open( name, 'r', encoding='utf-8') as file:
    content = file.read()
    words = content.split()
    print(f"Всего слов в файле {name}: {len(words)}")