import telebot

TOKEN = "8902350134:AAEhi-HEnk0sAEOk06iYKNt_iNlLLkY5Gy4" # Вставь свой новый токен!
bot = telebot.TeleBot(TOKEN)

user_data = {}

# Умная функция, которая достает 3 числа из твоего сообщения
# Ей неважно, напишешь ты "3, 12, 50" или "3 12 50", она всё поймет.
def parse_numbers(text):
    clean_text = text.replace(',', ' ')
    return clean_text.split()

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет! Какой сегодня день недели? (Вторник, Четверг, Суббота)")
    
@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    user_text = message.text.capitalize()
    
    user_data[chat_id] = {}

    if user_text == "Вторник":
        msg = bot.send_message(chat_id, "Введите все упражнения для предплечий через пробел (например: Эспандер Штанга):")
        bot.register_next_step_handler(msg, process_tuesday_exercises)

    elif user_text == "Четверг":
        msg = bot.send_message(chat_id, "Введите результаты для СПИНЫ (подходы, повторения, вес):")
        bot.register_next_step_handler(msg, process_thursday_back)

    elif user_text == "Суббота":
        msg = bot.send_message(chat_id, "Введите результаты для НОГ (подходы, повторения, вес):")
        bot.register_next_step_handler(msg, process_saturday_legs)
        
    else:
        bot.send_message(chat_id, "Пожалуйста, введите: Вторник, Четверг или Суббота.")

# ================= ВТОРНИК =================
def process_tuesday_exercises(message):
    chat_id = message.chat.id
    user_data[chat_id]['exercises'] = message.text.split()
    user_data[chat_id]['current_index'] = 0
    user_data[chat_id]['results'] = {}
    ask_next_tuesday_exercise(chat_id)

def ask_next_tuesday_exercise(chat_id):
    data = user_data[chat_id]
    index = data['current_index']
    exercises_list = data['exercises']
    
    if index < len(exercises_list):
        current_ex = exercises_list[index]
        msg = bot.send_message(chat_id, f"Упражнение: {current_ex}\nВведите результаты (подходы, повторения, вес):")
        bot.register_next_step_handler(msg, save_tuesday_stats)
    else:
        # ГЕНЕРАЦИЯ СТРОГОГО ШАБЛОНА ДЛЯ ВТОРНИКА
        final_text = "Вторник\n"
        for name, stats in data['results'].items():
            final_text += f"{name} - {stats[0]} подходов , {stats[1]} - раз, {stats[2]} - килограммов\n"
        
        bot.send_message(chat_id, final_text)

def save_tuesday_stats(message):
    chat_id = message.chat.id
    stats = parse_numbers(message.text)
    
    if len(stats) < 3:
        msg = bot.send_message(chat_id, "Нужно 3 числа! Введите заново (подходы, повторения, вес):")
        bot.register_next_step_handler(msg, save_tuesday_stats)
        return
        
    index = user_data[chat_id]['current_index']
    current_ex = user_data[chat_id]['exercises'][index]
    
    user_data[chat_id]['results'][current_ex] = stats
    user_data[chat_id]['current_index'] += 1
    
    ask_next_tuesday_exercise(chat_id)

# ================= ЧЕТВЕРГ =================
def process_thursday_back(message):
    chat_id = message.chat.id
    user_data[chat_id]['back'] = parse_numbers(message.text)
    msg = bot.send_message(chat_id, "Теперь введите результаты на ТРИЦЕПС (подходы, повторения, вес):")
    bot.register_next_step_handler(msg, process_thursday_triceps)

def process_thursday_triceps(message):
    chat_id = message.chat.id
    back = user_data[chat_id]['back']
    triceps = parse_numbers(message.text)
    
    # ГЕНЕРАЦИЯ СТРОГОГО ШАБЛОНА ДЛЯ ЧЕТВЕРГА
    final_text = "Четверг\n"
    if len(back) >= 3 and len(triceps) >= 3:
        final_text += f"Спина - {back[0]} подходов , {back[1]} - раз, {back[2]} - килограммов\n"
        final_text += f"Трицепс - {triceps[0]} подходов , {triceps[1]} - раз, {triceps[2]} - килограммов"
    else:
        final_text = "Ошибка: вы ввели меньше трех чисел. Начните заново."
        
    bot.send_message(chat_id, final_text)

# ================= СУББОТА =================
def process_saturday_legs(message):
    chat_id = message.chat.id
    user_data[chat_id]['legs'] = parse_numbers(message.text)
    msg = bot.send_message(chat_id, "Теперь введите результаты на ПЛЕЧИ (подходы, повторения, вес):")
    bot.register_next_step_handler(msg, process_saturday_shoulders)

def process_saturday_shoulders(message):
    chat_id = message.chat.id
    legs = user_data[chat_id]['legs']
    shoulders = parse_numbers(message.text)
    
    # ГЕНЕРАЦИЯ СТРОГОГО ШАБЛОНА ДЛЯ СУББОТЫ
    final_text = "Суббота\n"
    if len(legs) >= 3 and len(shoulders) >= 3:
        final_text += f"Ноги - {legs[0]} подходов , {legs[1]} - раз, {legs[2]} - килограммов\n"
        final_text += f"Плечи - {shoulders[0]} подходов , {shoulders[1]} - раз, {shoulders[2]} - килограммов"
    else:
        final_text = "Ошибка: вы ввели меньше трех чисел. Начните заново."
        
    bot.send_message(chat_id, final_text)

# ============================================
print("Бот запущен и готов к работе!")
bot.infinity_polling()