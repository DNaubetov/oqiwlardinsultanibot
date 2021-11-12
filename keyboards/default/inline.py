from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import URL_GROUP, URL_CHANNEL, URL_CONTRACT

group_button= InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Нажми тут ✅", url=URL_GROUP)
    ],
])

channel_button= InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Нажми тут ✅", url=URL_CHANNEL)
    ],
])

contract_button= InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Нажми тут ✅", url=URL_CONTRACT)
    ],
])

