#Множества , листы и Tuple's

#Множетсва - Это мешок с уникальными вещами. В множестве не может быть двух одинаковых элементов.
#В нем нельзя держать одинаковые чила или данные
my_set = {1,2,3,4,5 , True , "Hello"}
print(my_set)

#Листы - это просто упорядоченный список элементов. Как список покупок.
# В нем можно менять, добавлять и убирать
my_list = ["bread" , "egg" , 1 , 2 , True]
print(my_list)
print(my_list[0])
print(my_list[0:3:1])

#Кортежи(Tuple's) - то неизменяемый список. Представьте, что вы написали список покупок, заламинировали его и положили под бронированное стекло.
#Нечего нельзя добавлять или удалять. Просто неизменяемый набор данных
my_tuple = (55.7558, 37.6173)
print(my_tuple)
print(my_tuple[0]) #Можем принтить как обычно



#Задание
# numbers = (10 , 20 , 30)
# numbers[0] = 120
# print(numbers)
#'tuple' object does not support item assignment

text = str(input("Введите строку: "))
new_letters = []
new_letters.append(set(list(text)))
print(new_letters)


numbers = (10 , 20 , 30 , 40 , 50)
num = int(input("Введите число"))
if num in numbers:
    print("Число есть в кортэже")
else:
    print("Число не найдено в кортэжэ")