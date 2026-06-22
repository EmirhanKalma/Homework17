#1
age = 20
if age <= 18:
    print('Enter')
else:
    print("Too young")

#2
password_length = 6

if 8 <= password_length <= 20:
    print("Correct")
else:
    print("Invalid length")
    
#3
letter = 'e'

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("Correct")

#4
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print('Weekend')
else:
    print("Weekday")
    
#5
num = 14
lennum = len(str(num))

if lennum > 0:
    print('Correct')
else:
    print("Incorrect")

if num % 2 == 0:
    print("It's even number")
else:
    print("It's odd number")
    
#6
age = 15
if age >= 13 and age <= 19:
    print('You are teen')
else:
    print("Not teen")