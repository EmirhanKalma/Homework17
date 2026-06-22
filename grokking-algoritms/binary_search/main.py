def binary_search(arr , item):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        quess = arr[mid]
        if quess == item:
            return mid
        elif quess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1 , 2 ,34 , 123 , 95 , 34 , 1 , 54 , 12]

my_list.sort()


answer = binary_search(my_list , 12)
print(answer)