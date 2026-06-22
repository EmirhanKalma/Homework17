# 1)
regions = ["Чуйская", "Нарынская", "Ысык-Кульская", "Таласская", "Ошская", "Баткенская", "Джалал-Абадская"]
print(regions[0])
print(regions[-1])

# 2)
grades = [100, 85, 20, 95]
grades[2] = 90
print(grades)

# 3)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[5:7])

# 4)
numbers = [10, 20, 30, 40, 50, 60]
print(sum(numbers))

# 5)
cart = ["Apple", "Bread", "Milk", "Tea"]
print(f"У вас есть {len(cart)} предметов в корзине")

# 6)
backpack = []
backpack.append("карта")
backpack.append("вода")
print(backpack)

# 7)
line = ["Эрмек", "Адиль", "Амир"]
line.insert(0, "Айбек")
print(line)

# 8)
colors = ["Red", "Green", "Blue", "Green"]
colors.remove("Green")
print(colors)
print("Был удален первый Green (по середине)")

# 9)
tasks = ["Homework", "Clean room", "Sleep"]
tasks.pop()
print(tasks)

# 10)
scores = [45, 92, 12, 88, 100]
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)