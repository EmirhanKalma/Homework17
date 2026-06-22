#Exersice 1
for i in range(10, 101, 10):
    print(i)
#Exersice 2
for i in range(10, 81):
    if i % 2 == 0:
        print(i)
#Exerisice 3
# Запрашиваем ввод
try:
    number = int(input("Введите число для таблицы умножения: "))

    print(f"Таблица умножения для числа {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
except ValueError:
    print("Ошибка: пожалуйста, введите целое число.")