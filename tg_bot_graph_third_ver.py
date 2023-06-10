import matplotlib
from aiogram import Bot, Dispatcher, types, executor
import logging
from env import TOKEN
from aiogram.types import Message
from numexpr import evaluate
from numpy import tan, cos, sin
import numpy as np
import matplotlib.pyplot as plt
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

matplotlib.use("Agg")
import io
from PIL import Image
import io

plt.ioff()
pi = np.pi
e = np.e


def cotan(x):
    return cos(x) / sin(x)


token = TOKEN  # вставить сюда свой токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())  # осдержит все обработчике и ответчики

TOO_BIG_DIFFERENTIAL = 100

def fig2buf(fig):
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return buf


def plot_formula(formula: str, bounds: tuple[float, float], estimation: int):
    x = np.linspace(*bounds, estimation)
    formula = formula.replace("cotan(x)", "(cos(x)/sin(x))")
    y = evaluate(formula)
    print(y)
    y[:-1][np.abs(np.diff(y)) > TOO_BIG_DIFFERENTIAL] = np.nan

    fig, ax = plt.subplots()
    ax.set_xbound(*bounds)
    ax.grid()
    ax.axis()
    ax.plot(x, y, label=formula)
    ax.legend()
    img = fig2buf(fig)
    return img


@dp.message_handler(commands=['start', 'help'], state='*')  # содержит команды на которые он будет отвечать
async def _(message: types.Message, state: FSMContext):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply("Hi! \nI'm a meow_catty_bot!\nSend me the formula")
    await state.set_state("waiting_formula")


@dp.message_handler(state='waiting_formula')
async def take_formula(message: types.Message, state: FSMContext):
    formula = message.text
    await state.update_data({'formula': formula})
    await message.reply(f"Your formula is {formula} \n Send me the bounds\nFrmt: a, b")
    await state.set_state("waiting_bounds")


@dp.message_handler(state='waiting_bounds')
async def take_bounds(message: types.Message, state: FSMContext):
    bounds = tuple(map(int, message.text.split(', ')))
    await state.update_data({'bounds': bounds})
    data = await state.get_data()
    await message.reply(f"Your formula is {data['formula']} \nYour bounds are {data['bounds']}\nSend me estimation")
    await state.set_state("waiting_estimation")


@dp.message_handler(state='waiting_estimation')
async def take_bounds(message: types.Message, state: FSMContext):
    estimation = int(message.text)
    await state.update_data({'estimation': estimation})
    data = await state.get_data()
    await message.reply(
        f"Your formula is {data['formula']} \nYour bounds are {data['bounds']}\nYour estimation is {data['estimation']}")
    # await state.set_state("ready_to_make")
    # img = plot_formula(data['formula'], data['bounds'], data['estimation'])
    # await message.answer_photo(img)
    # img.close()
    img = await the_graph(state)
    await message.answer_photo(img)
    img.close()


async def the_graph(state: FSMContext):
    data = await state.get_data()
    img = plot_formula(data['formula'], data['bounds'], data['estimation'])  # FSM
    return img


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
