from .config import WELCOME_MESSAGE, RESULT_PHRASE, TG_TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import random

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


def gen_account(length: int) -> str:
    return ("".join(random.sample(RESULT_PHRASE, length)) for _ in range(2))


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(WELCOME_MESSAGE)


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer("/generate - generate password with your length\n/random_generate - generate password with random length")


@dp.message_handler(commands=["generate"])
async def generate(message: types.Message):
    await message.answer("Choose the length")


@dp.message_handler(commands=["random_generate"])
async def random_generate(message: types.Message):
    login, password = gen_account(random.randint(8, 15))

    await message.answer(f"Your login: {login}\nYour password: {password}")


@dp.message_handler()
async def get_number(message: types.Message):
    if not message.text.isdigit():
        return await message.reply("Unknown command. Please, enter a number.")

    num_len = int(message.text)

    if num_len > 15:
        return await message.reply("The maximum length is 15")

    login, password = gen_account(num_len)

    await message.answer(f"Your login: {login}\nYour password: {password}")
