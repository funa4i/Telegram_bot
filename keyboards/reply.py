from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_keyboard(*buttons: str,
                    placeholder: str = None,
                    size: tuple = None,
                    req_contact: int = None,
                    req_location: int = None):
    keyboard = ReplyKeyboardBuilder()
    for index, text in enumerate(buttons, start=0):
        if req_contact and req_contact == index:

            keyboard.add(KeyboardButton(text=text, request_contact=True))
        elif req_location and req_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:
            keyboard.add(KeyboardButton(text=text, request_location=True))
    return keyboard.adjust(*size).as_markup(resize_keyboard=True,
                                            input_field_placeholder=placeholder)
