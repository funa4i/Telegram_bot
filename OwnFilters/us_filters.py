from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message


class OwnFilter(Filter):
    def __init__(self, my_types: list[str]) -> None:
        self.my_types = my_types

    async def __call__(self, message: Message) -> bool:
        return message.chat.type in self.my_types
