from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

menu_kbrd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню")
        ],
        [
            KeyboardButton(text="Ваше местоположение", request_location=True)
        ],
        [
            KeyboardButton(text="Как с вами можно связаться?", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?")
