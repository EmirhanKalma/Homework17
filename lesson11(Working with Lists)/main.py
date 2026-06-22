# num = [1,2,3,4 , 12 , 20]
# # num.append(1) # Добавляет в самый конец кода
# # print(num)
# # num.pop(0)
# # num.remove(1)
# # print(num)
# # fruits = ["apple", "banana", "apple"]
# # fruits.remove("apple")
# # print(fruits)

# # num.sort(reverse=True)#От саого большого к самому меньшему фильтруе массив
# # print(num)

# text = "Kyrgyzstan"
# print(text[:4])

# word = "banana"
# print(word.replace("a", "o"))

# text = "Apple,Banana,Orange"
# fruits = text.split(",")
# print(len(fruits))


# fruit = "red,blue,green"
# print(fruit.split(","))

# print("-".join(["A", "B", "C"]))


# for i in range(10):
#     print("Hello")



logs = [
    "10:01 AM [INFO] Server started successfully.",
    "10:05 AM [WARNING] High memory usage.",
    "10:15 AM [ERROR] Database connection failed.",
    "10:22 AM [INFO] User login successful.",
    "10:45 AM [ERROR] Payment gateway timeout."
]
# Output:
#     """
#     Error: Database connection failed. 
#     Time: 10:15 AM
#     """


 
print(f"Number of logs: {len(logs)}")

for log in logs:
    if "ERROR" in log:
        parts = log.split("[ERROR]")
        time = parts[0]
        message = parts[1]
        print(f"Error: {message}") 
        print(f"Time: {time}")     


# binary = "11100010101010101010001010111010101010011010010010011101010111010010010010010101001001"

# one_number = binary.count("1")
# zero_number = binary.count("0")

# print(f"""
# {one_number} 1
# {zero_number} 0
#       """)


votes = "Аман" , "Аман" , "Аман" , "Акылай" , "Хамиля" , "Нурсултан" , "Талгат" , "Талгат"

if votes.count("Аман") >= votes.count("Талгат"):
    print("Аман выйграл")
elif votes.count("Аман") == votes.count("Талгат"):
    print("Ничья")
else:
    print("Талгат выйграл")
    
    
# email = 'sadyr.japarov@mbank.kg'
# at_index = email.find("@")#Ищет если не находит выводит -1
# print(email[at_index+1:])