max_score = 0
top_student = ""

with open('results.txt', 'r', encoding='utf-8') as file:
    for line in file:

        parts = line.split(':')
        

        name = parts[0].strip()
        score = int(parts[1].strip())
        

        if score > max_score:
            max_score = score
            top_student = name

print(f"Ученик с самым высоким ОРТ: {top_student} ({max_score} баллов)")