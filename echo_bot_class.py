from aiogram import Bot, Dispatcher, executor, types
from env import TOKEN2
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from random import choices, choice
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)

TOKEN = TOKEN2

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

connected_users = set()

@dp.message_handler(commands=['start', 'help'], state='*')  # '*' - принимаем любое состояние на вход
async def send_welcome(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    await message.reply("Hi!\nI'm EchoBot!\nSay ur name")
    await state.set_state('q1')  # изменение состояния


@dp.message_handler(state='q1')
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await state.set_state('q2')
    await message.answer('Say ur age')


@dp.message_handler(state='q2')
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isdigit():
        if int(age) >= 16:
            await state.update_data({"age": int(age)})
            await state.set_state('echo')
            await message.answer('now i know ur name and age')
            connected_users.add(message.from_user.id)
        elif int(age) < 18:
            await state.set_state('bye')
            await message.answer("sorry, i don't work with kids")
    else:
        data = await state.get_data()
        await message.answer(f"ur age isn't a number, try again, {data['name']}")


@dp.message_handler(commands = ['find'], state='echo')
async def echo(message: Message, state: FSMContext):
    await message.answer(f'@{message.from_user.username}: waiting')
    for user in connected_users:
        if len(connected_users) > 1:
            await bot.send_message(user, f'waiting users: {connected_users - {message.from_user.id}}')
        else:
            await bot.send_message(user, f"waiting users: there's no connected users now, please wait")

    user2_id = choice(tuple(connected_users - {message.from_user.id}))
    # await message.answer(f"{user2_id}")

    if user2_id:
        await state.set_data({"target": user2_id})
        await state.set_state("chat")



@dp.message_handler(state='chat')
async def echo(message: Message, state: FSMContext):
    data = await state.get_data()
    user2_id = data.get("target")
    await bot.send_message(user2_id, f'@{message.from_user.username}: {message.text}')


@dp.message_handler(state='bye')
async def echo(message: Message, state: FSMContext):
    await message.answer('bye')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)