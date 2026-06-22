#len - измеряет длину строки (Числа не работают)
from math import sqrt
#Проект
number = int(input("Enter a  first number: "))
number2 = int(input("Enter a second number: "))
operation = str(input("Enter a mathematical operation[+ , - , * , / , √ , pefagor(pef) , degree(step)]: "))
    
if operation == "+":
    print(number + number2)
elif operation == "-":
    print(number - number2)
elif operation == "*":
    print(number * number2)
elif operation == "/":
    if number2 == 0:
        print(0)
    else:
        print(number / number2)
elif operation == "√":
    if number <= 0:
        print("Impossible operation!")
    else:
        print(sqrt(number))
elif operation == "pef":
    if number <= 0 or number2 <= 0:
        print("Impossible operation")
    else:
        pef = (number ** 2) + (number2 ** 2)
        print(sqrt(pef))
    
elif operation == "step":
    print(number ** number2)
else:
    print("Invalid data")


