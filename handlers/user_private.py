from aiogram import types, Router
from aiogram.filters import Command, CommandStart, or_f
from aiogram import F
from aiogram import Bot
from aiogram.utils.formatting import as_list, as_marked_section, Bold

import os

from keyboards.reply import create_keyboard
from OwnFilters.us_filters import OwnFilter

user_private_router = Router()
user_private_router.message.filter(OwnFilter(["private"]))


# Старт
@user_private_router.message(F.text.lower().contains("старт"))
@user_private_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Здравствуйте, <b>{message.from_user.first_name}!</b>")
    await message.answer(f"Что вас интересует?", reply_markup=create_keyboard("Каталог",  "Продавец", size=(1,1,1,1)))


# Описание бота
@user_private_router.message(Command('about'))
async def descrip(message: types.Message):
    mark_up_text = as_list(
        as_marked_section(
            Bold("Для чего нужен бот?\n"),
            "Для выбора цветков",
            marker="✅ "
        ),
        as_marked_section(
            Bold("Для чего бот не подходит\n"),
            "Для покупки столов",
            marker="❌ "

        ),
        sep='\n-------------\n'
    )

    await message.reply(mark_up_text.as_html())


# Описать возможности бота
@user_private_router.message(Command('possibilities'))
async def possibilities(message: types.Message):
    await message.reply("Благодаря боту вы можете совершить операции с доступным каталогом 😘")


@user_private_router.message(Command("menu"))
@user_private_router.message(F.text.lower().contains("каталог"))
async def possibilities(message: types.Message):
    await message.reply("меню")


