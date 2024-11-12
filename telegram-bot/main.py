import os
import toml

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

# ====================== DATA =======================================
with open('message.toml', 'r', encoding='utf-8') as config_file:
    text_messages = toml.load(config_file)

load_dotenv()
# ====================================================================


# ====================== COST =======================================
balls = 0
flags = [1, 1, 1]
# ====================================================================


# ====================== BOT SETTINGS ==============================
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ====================================================================


# ====================== BOT KEYBOARDS ==============================
start_markup = types.InlineKeyboardMarkup()
button_1 = types.InlineKeyboardButton('Начать тест!', callback_data='start')
start_markup.add(button_1)

q1_markup = types.InlineKeyboardMarkup()
button_1 = types.InlineKeyboardButton('Да', callback_data='1-t')
button_2 = types.InlineKeyboardButton('Нет', callback_data='1-f')
button_3 = types.InlineKeyboardButton('Ошибку', callback_data='1-f')
q1_markup.add(button_1, button_2, button_3)

q2_markup = types.InlineKeyboardMarkup()
button_1 = types.InlineKeyboardButton('5', callback_data='2-f')
button_2 = types.InlineKeyboardButton('10', callback_data='2-t')
button_3 = types.InlineKeyboardButton('Ошибку', callback_data='2-f')
q2_markup.add(button_1, button_2, button_3)

q3_markup = types.InlineKeyboardMarkup()
button_1 = types.InlineKeyboardButton('True', callback_data='3-f')
button_2 = types.InlineKeyboardButton('34', callback_data='3-f')
button_3 = types.InlineKeyboardButton('45', callback_data='3-t')
button_4 = types.InlineKeyboardButton('Весь список', callback_data='3-f')
q3_markup.add(button_1, button_2, button_3, button_4)


# ====================================================================


# ====================== BOT ROUTER ==============================
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text_messages['start_message']['hello_msg'], reply_markup=start_markup)


@dp.callback_query_handler()
async def callback_query(callback: types.CallbackQuery):
    global balls
    if callback.data == 'start':
        await callback.answer('Старт')
        balls = 0
        for i in range(3):
            flags[i] = 1
        await bot.send_message(callback.message.chat.id,
                               text_messages['questions']['question1'],
                               reply_markup=q1_markup,
                               parse_mode='HTML')
    elif callback.data[0] == '1':
        print(callback.data, flags)


# ====================================================================


executor.start_polling(dp, skip_updates=True)
