from math import sqrt

#1
def say_goodbye(name):
    print(f"Пока {name}")
    
#2
def power(a, b):
    return a ** b 

#3
def is_even(number):
    num_check = number % 2
    if num_check == 0:
        return True
    else:
        return False
    
#4
def find_max(a, b, c):
    return max(a , b , c)

#5
def count_vowels(text):
    vowels = ["a", "e", "i", "y", "u", "o"] # Заодно добавил пропущенную букву "i"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count