import asyncio
import logging
import uuid
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# ВСТАВЬ СЮДА СВОЙ ТОКЕН ОТ BotFather
TOKEN = "8881957857:AAF18C4DfRDYiDmlnCIXq9--Sx0-ZdaVLI4"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler(timezone="Europe/Moscow") # Время по Москве

# --- СОСТОЯНИЯ ---
class ReminderState(StatesGroup):
    waiting_for_time = State()
    waiting_for_text = State()
    waiting_for_continue = State()

# --- КЛАВИАТУРЫ ---
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать напоминалку 📝")],
        [KeyboardButton(text="Мои напоминания 📋")]
    ],
    resize_keyboard=True
)

time_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Через 1 минуту ⏱"), KeyboardButton(text="Через 1 час ⏳")],
        [KeyboardButton(text="Завтра в это же время 🌅")],
        [KeyboardButton(text="Отмена ❌")]
    ],
    resize_keyboard=True
)

yes_no_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да ✅"), KeyboardButton(text="Нет ❌")]
    ],
    resize_keyboard=True
)

# --- 1. ФУНКЦИЯ ДЛЯ ОТПРАВКИ НАПОМИНАНИЯ ---
async def send_reminder(chat_id: int, text: str):
    # Убрал всю воду! Приходит ТОЛЬКО твой текст.
    await bot.send_message(chat_id, text)

# --- ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ДЛЯ СПИСКА НАПОМИНАНИЙ ---
def get_reminders_ui(chat_id: int):
    jobs = scheduler.get_jobs()
    # Ищем только твои напоминания
    user_jobs = [job for job in jobs if job.kwargs.get('chat_id') == chat_id]
    
    if not user_jobs:
        return "У вас нет активных напоминаний.", None

    builder = InlineKeyboardBuilder()
    text_list = "📅 **Ваши активные напоминания:**\n\n"

    for i, job in enumerate(user_jobs, 1):
        run_date = job.next_run_time.strftime('%d.%m.%Y %H:%M')
        remind_text = job.kwargs.get('text')
        
        # Если текст очень длинный, в меню обрезаем его для красоты (в самом напоминании он будет полным)
        short_text = remind_text[:20] + "..." if len(remind_text) > 20 else remind_text
        text_list += f"{i}. {run_date} — {short_text}\n"

        # Создаем кнопку для удаления (привязываем к ней уникальный ID задачи)
        builder.button(text=f"Удалить №{i} ❌", callback_data=f"del_{job.id}")

    # Размещаем по 2 кнопки в ряд
    builder.adjust(2)
    return text_list, builder.as_markup()

# --- ОБРАБОТЧИКИ СООБЩЕНИЙ ---

@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Привет! Выбери действие:", reply_markup=main_kb)

@dp.message(F.text == "Создать напоминалку 📝")
async def start_reminder_creation(message: Message, state: FSMContext):
    await message.answer(
        "Укажите дату и время (ДД.ММ.ГГГГ ЧЧ:ММ) или выберите кнопку:",
        reply_markup=time_kb
    )
    await state.set_state(ReminderState.waiting_for_time)

@dp.message(F.text == "Отмена ❌")
async def cancel_action(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Отменено.", reply_markup=main_kb)

@dp.message(ReminderState.waiting_for_time)
async def process_time(message: Message, state: FSMContext):
    text = message.text
    now = datetime.now()
    remind_time = None

    if text == "Через 1 минуту ⏱": remind_time = now + timedelta(minutes=1)
    elif text == "Через 1 час ⏳": remind_time = now + timedelta(hours=1)
    elif text == "Завтра в это же время 🌅": remind_time = now + timedelta(days=1)
    else:
        try:
            remind_time = datetime.strptime(text, "%d.%m.%Y %H:%M")
            if remind_time < now:
                await message.answer("Это время в прошлом! Введи будущее.")
                return
        except ValueError:
            await message.answer("Неверный формат! Напиши как в примере или нажми кнопку.")
            return

    await state.update_data(remind_time=remind_time)
    await message.answer(
        f"Время установлено: {remind_time.strftime('%d.%m.%Y %H:%M')}\nТеперь напишите сам текст напоминания:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(ReminderState.waiting_for_text)

@dp.message(ReminderState.waiting_for_text)
async def process_text(message: Message, state: FSMContext):
    reminder_text = message.text
    user_data = await state.get_data()
    remind_time = user_data['remind_time']

    # Генерируем уникальный ID для напоминания (чтобы его можно было удалить)
    job_id = str(uuid.uuid4().hex[:10])

    # Добавляем в планировщик точнейшее выполнение
    scheduler.add_job(
        send_reminder, 
        trigger='date', 
        run_date=remind_time, 
        id=job_id, # Присваиваем ID
        kwargs={'chat_id': message.chat.id, 'text': reminder_text}
    )

    await message.answer(
        "✅ Записано!\nХотите создать еще одно?",
        reply_markup=yes_no_kb
    )
    await state.set_state(ReminderState.waiting_for_continue)

@dp.message(ReminderState.waiting_for_continue)
async def process_continue(message: Message, state: FSMContext):
    if message.text == "Да ✅":
        await start_reminder_creation(message, state)
    elif message.text == "Нет ❌":
        await state.clear()
        await message.answer("Счастливого дня! Уведомление придет точно в срок.", reply_markup=main_kb)
    else:
        await message.answer("Нажми 'Да' или 'Нет'.", reply_markup=yes_no_kb)

# --- МЕНЮ УПРАВЛЕНИЯ НАПОМИНАНИЯМИ ---

# 1. Показать список с кнопками удаления
@dp.message(F.text == "Мои напоминания 📋")
async def show_reminders(message: Message):
    text, keyboard = get_reminders_ui(message.chat.id)
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

# 2. Обработка нажатия на прозрачную кнопку "Удалить"
@dp.callback_query(F.data.startswith("del_"))
async def delete_reminder(callback: CallbackQuery):
    # Получаем ID задачи из кнопки
    job_id = callback.data.split("_")[1]
    
    try:
        # Удаляем из планировщика
        scheduler.remove_job(job_id)
        # Всплывающее уведомление
        await callback.answer("Напоминание успешно удалено!", show_alert=True)
        
        # Обновляем сообщение (чтобы удаленное исчезло из списка)
        text, keyboard = get_reminders_ui(callback.message.chat.id)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
        
    except Exception:
        # Если такого ID уже нет (например, время уже пришло и оно само удалилось)
        await callback.answer("Ошибка! Возможно, это напоминание уже сработало.", show_alert=True)


async def main():
    scheduler.start()
    print("Бот успешно запущен! Можно писать ему в Телеграме.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())