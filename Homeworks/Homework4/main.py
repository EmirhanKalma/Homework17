total = 0

while True:
    if total == 1000:
        print("Вы накопили до 1000!")
        break
    num = int(input("Введите число: "))
    total += num