from aiogram import Bot, Dispatcher, executor, types
from env import TOKEN2
import logging
from keyboards import keyboard, keyboard2, inlinekeyboard
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from random import choices, choice
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)

TOKEN = TOKEN2

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

all_users = set()
connected_users = set()  # вычитать connected_users из all_users чтобы не было проблем при нескольких пользователях


@dp.message_handler(commands=['start', 'help'], state='*')  # '*' - принимаем любое состояние на вход
async def send_welcome(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    await message.reply("Hi!\nI'm EchoBot!\nSay ur name", reply_markup=inlinekeyboard)
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
            all_users.add(message.from_user.id)
        elif int(age) < 18:
            await state.set_state('bye')
            await message.answer("sorry, i don't work with kids")
    else:
        data = await state.get_data()
        await message.answer(f"ur age isn't a number, try again, {data['name']}")


@dp.message_handler(commands=['find'], state='echo')
async def echo(message: Message, state: FSMContext):
    await message.answer(f'@{message.from_user.username}: waiting', reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id

    for user in all_users:
        if user == user_id:
            if len(all_users) > 1:
                # targets = set(all_users) - set(connected_users) - {message.from_user.id}
                targets = set(connected_users) - {message.from_user.id}

                await bot.send_message(user, f'waiting users: {targets}')
                await bot.send_message(user, f"to select user enter his id")
                await state.set_state('user_selecting')

            else:
                await bot.send_message(user, f"waiting users: there's no connected users now, please wait,"
                                             f"\nfor reload user enter cmd find again")

        await bot.send_message(user, f'new user is here! send cmd find to see id')
    # user2_id = choice(tuple(connected_users - {message.from_user.id}))
    # # await message.answer(f"{user2_id}")
    #
    # if user2_id:
    #     await state.set_data({"target": user2_id})
    #     await state.set_state("chat")


@dp.message_handler(state='user_selecting')
async def echo(message: Message, state: FSMContext):
    if message.text.isdigit():
        user_id = message.from_user.id

        target = int(message.text)
        targets = set(all_users) - {message.from_user.id, }
        if target in targets:
            target_state: FSMContext = dp.current_state(chat=target, user=target)
            # connected_users.add(target)
            # connected_users.add(user_id)
            await message.answer(f"Вы связаны с {target_state.user}")
            await bot.send_message(target, f"Вы связаны с {user_id}")
            await state.set_state("chat")
            await target_state.set_state("chat")
            await state.update_data({"target": target})
            await target_state.update_data({"target": user_id})
    else:
        await message.answer('enter correct id only')
    # data = await state.get_data()
    # user2_id = data.get("target")
    # await bot.send_message(user2_id, f'@{message.from_user.username}: {message.text}')


@dp.message_handler(state='chat')
async def echo(message: Message, state: FSMContext):
    data = await state.get_data()
    user2_id = data.get("target")
    name = data.get('name')
    await bot.send_message(user2_id, f'msg from {name}: {message.text}')


@dp.message_handler(state='bye')
async def echo(message: Message, state: FSMContext):
    await message.answer('bye')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
