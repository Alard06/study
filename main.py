import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# АПИ ТОКЕН С БОТА BOT FATHER
api_token = '8194121363:AAFe0q8x5TCabeThoDrB1tDSbAgcmJm5jpQ'

# Создаем объект бота, который связывается с Telegram

bot = Bot(token=api_token)

# Обработка сообщений. В наличии 1 штука
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет!')
    # ДЛЯ СТИКЕРОВ
    await message.answer_sticker('CAACAgIAAxkBAAENE0xnKifsiwH5dxH70cSJyLfKjUNOXgAC2RYAAvwQaUicXPKwXVVIWTYE')

@dp.message()
async def echo(message: types.Message):
    print(message)
    await message.answer(f'{message.from_user.first_name}, ты написал: {message.text}')
    if message.text == 'Как дела?':
        await message.answer('Хорошо')

async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
