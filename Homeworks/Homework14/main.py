# def

def get_max(a, b):
    if a > b:
        print(f"Число {a} больше чем {b}")
        return a
    else:
        print(f"Число {b} больше чем {a}")
        return b

get_max(1 , 2)

def get_sum(arr):
    total = 0
    
    for num in arr:
        total = total + num
    print(f"Сумма чисел равно: {total}")
    return(total)


get_sum([1 , 2 , 3])

def is_palindrom(str1):
    clean_str = str1.replace(" ", "").lower()
    return clean_str == clean_str[::-1]
    

        
def average(arr):
    total = sum(arr)
    length = len(arr)
    print(f"Средне-арифмитическое: {total / length}(округлено: {total // length})")
    return total / length

average([5 , 5 , 4])

def get_longest_word(str1):
    split_str = str1.split(" ")
    longest = ""   
    for word in split_str:
        if len(word) > len(longest):
            longest = word
    return longest

print(f"Самое длинное слово: {get_longest_word("hello my name is Emirhan")}")