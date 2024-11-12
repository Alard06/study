import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton  # Novoe

# АПИ ТОКЕН С БОТА BOT FATHER
api_token = '8194121363:AAGX9fj9TbSprXMaEiv5J6S2aQGmh9_mlKY'

# Создаем объект бота, который связывается с Telegram

bot = Bot(token=api_token)

# Обработка сообщений. В наличии 1 штука
dp = Dispatcher()


def start_btn():
    kb = [
        [KeyboardButton(text='Начать')],
        [KeyboardButton(text='Выйти'), KeyboardButton(text='Что тут такое?')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb)


def youtube_kbs():
    kb = [
        [InlineKeyboardButton(text='Открыть ютуб', url='https://www.youtube.com')],
        # [KeyboardButton(text='Выйти'), KeyboardButton(text='Что тут такое?')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def start_inline_keyboard():
    kb = [
        [InlineKeyboardButton(text='ЮТУЮ ', url='https://www.youtube.com')],
        [InlineKeyboardButton(text='VK', url='https://vk.com')],
        [InlineKeyboardButton(text='Rutube', url='https://rutube.ru')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


def callback_data_kbs():
    kb = [
        [InlineKeyboardButton(text='ЮТУЮ ', callback_data='yotoue')],
        [InlineKeyboardButton(text='VK', callback_data='vk')],
        [InlineKeyboardButton(text='Rutube', callback_data='rutube')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


""" ОТРАБОТКА CALLBACK DATA """


@dp.callback_query()
async def callback_data(call: types.CallbackQuery):
    if call.data == 'yotoue':
        await call.message.answer('ЮТУБ', reply_markup=youtube_kbs())  # НЕ ЗАБЫВАЕМ CAALLLL
    print(call.data)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет!', reply_markup=start_btn())
    # ДЛЯ СТИКЕРОВ
    await message.answer_sticker('CAACAgIAAxkBAAENE0xnKifsiwH5dxH70cSJyLfKjUNOXgAC2RYAAvwQaUicXPKwXVVIWTYE')


@dp.message()
async def echo(message: types.Message):
    print(message)
    await message.answer(f'{message.from_user.first_name}, ты написал: {message.text}')
    if (message.text).lower() in 'начать':
        await message.answer('Начинаем', reply_markup=start_inline_keyboard())
    elif (message.text).lower() in 'что тут такое?':
        await message.answer('Тут что то происходит', reply_markup=callback_data_kbs())


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
