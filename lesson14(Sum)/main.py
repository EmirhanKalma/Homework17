ort = [245 , 217 , 115 , 115 , 213 , 123]

# for i in ort:
#     highest_number = max(ort)
#     print(highest_number)


print(f"Sum ORT: {sum(ort)}")
print(f"Highest score in ORT: {max(ort)}")
print(f"Lowest score in ORT: {min(ort)}")

ort = [145 , 170 , 212]
names = ["Айбек" , "Байбек" , "Жоодарбек"]

print(f"Айбек: {145}")

for name, ort in zip(names , ort):
    print(f"Name: {name} , ORT: {ort}")