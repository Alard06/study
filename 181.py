import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import (ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           KeyboardButton, InlineKeyboardMarkup,
                           InlineKeyboardButton, CallbackQuery)

def inline_keys_board():
    inline_keys = [
        [InlineKeyboardButton(text='Hello World', url='yandex.ru')],
        [InlineKeyboardButton(text='Как меня зовут? ', callback_data='my_name')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keys)


def test_kbs():
    kb_list = [
        [KeyboardButton(text='Помогите'), KeyboardButton(text='Нет')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb_list)


# АПИ ТОКЕН С БОТА BOT FATHER
api_token = '8194121363:AAFe0q8x5TCabeThoDrB1tDSbAgcmJm5jpQ'

# Создаем объект бота, который связывается с Telegram

bot = Bot(token=api_token)

# Обработка сообщений. В наличии 1 штука
dp = Dispatcher()


@dp.callback_query(F.data == 'my_name')
async def my_name(call: CallbackQuery):
    await call.message.answer(f'Твоё имя: {call.message.chat.first_name}')


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('<b>Привет!</b>', reply_markup=test_kbs(), parse_mode='HTML')
    # ДЛЯ СТИКЕРОВ
    await message.answer_sticker('CAACAgIAAxkBAAENE0xnKifsiwH5dxH70cSJyLfKjUNOXgAC2RYAAvwQaUicXPKwXVVIWTYE')


@dp.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer('Great photo')


@dp.message()
async def echo(message: types.Message):
    print(message)
    await message.answer(f'{message.from_user.first_name}, ты написал: {message.text}')
    if message.text == 'Как дела?':
        await message.answer('Хорошо')
    if message.text == 'Помогите':
        await message.answer('Не помогу')


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
