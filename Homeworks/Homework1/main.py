#Arithmetics
#1
cappuccino = 150
americano = 150
raf = 150
bun = 70
samsa = 70

total = cappuccino + americano + raf + bun + samsa
print(total)

#2
print(2 ** 10)

#3
marks = [100, 115, 150, 180, 185, 200]
minus = sum(marks) / len(marks)
print(minus)

#4
width = 1578
height = 9756
perimetr = (width + height) *2
s = width * height
print(f"Периметр: {perimetr} , Площадь: {s}")

#5
minutes = 275
hours = minutes // 60
remaining_minutes = minutes % 60
print("Часов:", hours)
print("Минут:", remaining_minutes)

#6
tempe = 451
c = (tempe - 32) *5 / 9
print(c)

#7
from math import sqrt
print(sqrt(123456789))