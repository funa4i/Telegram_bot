from aiogram import types, Router
from aiogram.filters import Command, CommandStart, or_f
from aiogram import F
from aiogram import Bot
from aiogram.utils.formatting import as_list, as_marked_section, Bold

import os

from keyboards import reply
from OwnFilters.us_filters import OwnFilter
user_private_router = Router()
user_private_router.message.filter(OwnFilter(["private"]))


# Старт
@user_private_router.message(F.text.lower() == "старт")
@user_private_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        text=f"Здравствуйте, <b>{message.from_user.first_name}</b>!\nПожалуйста, выбрете нужную вам команду😉",
        reply_markup=reply.menu_kbrd)


# Описание бота
@user_private_router.message(Command('about'))
async def descrip(message: types.Message):
    mark_up_text = as_list(
        as_marked_section(
            Bold("Для чего нужен бот?\n"),
            "Для выбора цветков",
            marker="✔ "
        ),
        as_marked_section(
            Bold("Для чего бот не подходит\n"),
            "\nДля покупки столов",
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
@user_private_router.message(F.text.lower().contains("меню"))
async def possibilities(message: types.Message):
    await message.reply("меню")


@user_private_router.message(F.photo)
async def an_ph(message: types.Message, bot: Bot):
    await bot.download(message.photo[-1].file_id, destination=f"data\\{message.photo[-1].file_unique_id}.jpg")
    user_phot = types.FSInputFile(f"data\\{message.photo[-1].file_unique_id}.jpg")
    await message.answer_photo(user_phot)
    os.remove(f"data\\{message.photo[-1].file_unique_id}.jpg")


@user_private_router.message(F.location)
async def handlLocation(message: types.Message):
    await message.reply(text="Ваше местоположение: " + str(message.location))


@user_private_router.message(F.contact)
async def handlLocation(message: types.Message):
    await message.reply(text="Ваш номер телефона: " + str(message.contact.phone_number))

