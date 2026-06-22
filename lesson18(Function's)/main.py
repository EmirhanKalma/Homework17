#def Функции
#Например написанная функция для задания в домшке №12 3 задание
def count_line(filename):
    with open(str(filename) , 'r' , encoding='utf-8') as file:
        lines = file.readlines() # Создает список из всех строк
        count = len(lines)
        print(f"Количество строк в файле {filename}: {count}")
    return count
        
count_line("results.txt")


