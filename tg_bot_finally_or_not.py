from aiogram import Bot, Dispatcher, types, executor
import logging
from env import TOKEN
from aiogram.types import Message

<<<<<<< HEAD
token = TOKEN #вставить сюда свой токен
=======
token = TOKEN
>>>>>>> origin/main

logging.basicConfig(level=logging.INFO)

bot = Bot(token)
dp = Dispatcher(bot)  # осдержит все обработчике и ответчики


@dp.message_handler(commands=['start', 'help'])  # содержит команды на которые он будет отвечать
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply("Hi! \nI'm a meow_catty_bot!")


@dp.message_handler()
async def echo(message: Message):
    await message.answer(message.text + f' meow, {message.from_user["first_name"]}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
