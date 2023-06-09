import matplotlib
from aiogram import Bot, Dispatcher, types, executor
import logging
from env import TOKEN
from aiogram.types import Message
from numexpr import evaluate
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use("Agg")
import io
from PIL import Image
import io
plt.ioff()
pi = np.pi
e = np.e

token = TOKEN  # вставить сюда свой токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token)
dp = Dispatcher(bot)  # осдержит все обработчике и ответчики


def fig2buf(fig):
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return buf


def plot_formula(formula: str, bounds: tuple[float, float], estimations: int):
    x = np.linspace(*bounds, estimations)
    y = evaluate(formula)
    fig, ax = plt.subplots()
    ax.grid()
    ax.axis()
    ax.plot(x, y, label=formula)
    ax.legend()
    img = fig2buf(fig)
    return img


@dp.message_handler(commands=['start', 'help'])  # содержит команды на которые он будет отвечать
async def _(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply("Hi! \nI'm a meow_catty_bot!")


@dp.message_handler()
async def _(message: Message):
    img = plot_formula(message.text, (-5, 5), 100) # FSM
    await message.answer_photo(img)
    img.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
