import io

from aiogram import Bot, Dispatcher, executor, types
from env import MV_TOKEN
import logging
import requests
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InputFile
from dataclasses import dataclass, field
from mw_keyboard import inlineKeyboardGreeting, inlineKeyboardWeekSchedule, weekday_cd, inlineShowCat

# @dataclass
# class Schedule:
#     ...


logging.basicConfig(level=logging.INFO)

# Инициализировать бота и задать диспетчера
bot = Bot(token=MV_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state="*")
async def _(message: Message, state: FSMContext):
    await message.answer(
        f'Hi, {message.from_user.username}! Welcome to Motivation and Study Bot!'
        '\nYou can set your schedule and homework here'
        '\n(or get a motivation pic ;)'
        '\nUse buttons below to choose the mode'
        '\nStay motivated and do your homework <3', reply_markup=inlineKeyboardGreeting)


# callback для кнопки "посмотреть расписани" - выводится лист кнопок - список дней недели
@dp.callback_query_handler(text='show_schedule', state="*")
async def show_schedule(callback_query: types.CallbackQuery, state: FSMContext):
    # await bot.answer_callback_query(callback_query.id, 'Callback Answered!')  # это всплывающее окно
    await bot.send_message(callback_query.from_user.id, 'Вот твое расписание: ',
                           reply_markup=inlineKeyboardWeekSchedule)
    # спросить у руслана лучше сделать еще одну клаву чтобы редактировать расписание или использовать state
    await state.set_state('choose_weekday_to_show')


# callback для кнопки дней недели (показ)
@dp.callback_query_handler(weekday_cd.filter(), state='choose_weekday_to_show')
async def _(call: types.CallbackQuery, callback_data: dict):
    weekday = callback_data.get("weekday")
    print(weekday, 'just showing')
    # data = await state.get_data()
    # day_schedule = data.get(f'{weekday}')
    # await message.answer(f'Вот твое расписание на день: {day_schedule}')
    # await bot.send_message(call.from_user.id, f'Вот твое расписание на день: {day_schedule}')


# callback для кнопки "посмотреть дз" - выводится лист кнопок - список дней недели
@dp.callback_query_handler(text='show_homework', state='*')
async def show_homework(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, 'Вот твое домашнее задание: ',
                           reply_markup=inlineKeyboardWeekSchedule)
    await state.set_state('choose_weekday_to_show_homework')


# callback для кнопки дней недели (показ домашнего задания)
@dp.callback_query_handler(weekday_cd.filter(), state='choose_weekday_to_show_homework')
async def _(call: types.CallbackQuery, callback_data: dict):
    weekday = callback_data.get("weekday")
    print(weekday, 'just showing hw')


# callback для кнопки изменения расписания
@dp.callback_query_handler(text='edit_homework', state="*")
async def edit_homework(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, 'Выбери день, для которго хочешь изменить домашнее задание: ',
                           reply_markup=inlineKeyboardWeekSchedule)
    await state.set_state('choose_weekday_to_edit_homework')


# callback для кнопки дней недели (изменение домашнего задания)
@dp.callback_query_handler(weekday_cd.filter(), state='choose_weekday_to_edit_homework')
async def _(call: types.CallbackQuery, callback_data: dict):
    weekday = callback_data.get("weekday")
    print(weekday, 'ready to change the schedule hw')


# callback для кнопки изменения расписания
@dp.callback_query_handler(text='edit_schedule', state="*")
async def edit_schedule(callback_query: types.CallbackQuery, state: FSMContext):
    # await bot.answer_callback_query(callback_query.id, 'Callback Answered!')  # это всплывающее окно
    await bot.send_message(callback_query.from_user.id, 'Выбери день, который хочешь изменить: ',
                           reply_markup=inlineKeyboardWeekSchedule)
    await state.set_state('choose_weekday_to_edit')


# callback для кнопки дней недели (изменение расписания)
@dp.callback_query_handler(weekday_cd.filter(), state='choose_weekday_to_edit')
async def _(call: types.CallbackQuery, callback_data: dict):
    weekday = callback_data.get("weekday")
    # # await bot.send_message(call.from_user.id, 'Введи свои предметы списком. Вот так:\nclass 1\nclass 2\nclass 3\n... ')
    # await message.answer('Введи свои предметы списком. Вот так:\nclass 1\nclass 2\nclass 3\n... ')
    # await state.update_data({f'{weekday}': message.text})
    print(weekday, "ready to change the schedule")


# callback для котиков
@dp.callback_query_handler(text='show_a_cat', state="*")
async def show_a_cat(callback_query: types.CallbackQuery):
    img = get_cat()
    if img:
        # надо еще добавить всякие милости для подписей к картинкам
        await bot.send_photo(callback_query.from_user.id, img, caption='котик', reply_markup=inlineKeyboardGreeting)


def get_cat() -> InputFile:
    link = 'https://api.thecatapi.com/v1/images/search'
    answer: list[dict: str | int] = requests.get(link).json()
    url_s = []
    for i in answer:
        url_s.append(i.get('url'))

    for url in url_s:
        data = requests.get(url).content
        buf = io.BytesIO(data)
        # buf.seek(0)
        img = InputFile(buf)
        return img


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
