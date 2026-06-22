# BASIC

# """
# /tp Timur123_ 900 800 700
# """
# """
# Action: tp
# User: Timur123_
# Coordinates: X: 900, Y: 800, Z:700
# """ + 10




# PRO
# # "/give Timur123_ minecraft:golden_apple 64"

# # """
# # Action: give
# # User: Timur123_
# # Item: Golden Apple
# # Quantity: 64
# # """



# command = "/tp Timur123_ 900 800 700"
# command_list = command.split()
# print(command_list)

# print(f"Action: {command_list[0].title()}")
# print(f"User: {command_list[1]}")
# print(f"Coordinates: X: {command_list[2]} , Y: {command_list[3]} , Z: {command_list[4]}")


# command2 = "/give Timur123_ minecraft:golden_apple 64"
# command2_list = command2.split()
# print(command2_list)
# tp = command2_list[0]
# item = command2_list[2]
# print(f"Action: {tp}")
# print(f"User: {command2_list[1]}")
# print(f"Item: {item.title()}")
# print(f"Quanity: {command2_list[3]}")

# while True:
#     word = str(input("Введите слово: "))
#     word1 = "тупой"
#     if word == word1.lower or word == word.upper or word == word.capitalize or word == word1.strip:
#        print("Вы ввели слово:")
#     else:
#        print(f"Вы ввели слово: {word}")
       
       
ban_list = ["тупой", "лоускилл", "черт", "козел", "зеленский"]
ban_list[0] = "*****"     
ban_list[1] = "********"  
ban_list[2] = "****"      
ban_list[3] = "*****"    
ban_list[4] = "*********" 

print(ban_list)