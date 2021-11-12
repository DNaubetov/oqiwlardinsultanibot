from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.default import button
from app import bot
from database.base import sqlighter

from file.default import file
from loader import dp
from config import admin_id


db = sqlighter.SQLighter('database/base/db.db')


#Запуск
@dp.message_handler(Command("start"))
async def hello(message: Message):
    dastan_id = 635986455
    user_id = message.from_user.id
    mes=message
    await message.answer_sticker(file.Hello)

    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его
        db.add_users(message.from_user.full_name,message.from_user.id)
    else:
        await bot.send_message(admin_id,text=f'Пользователь \"{message.from_user.full_name}\" перезапустил бота')
        await message.forward(admin_id)
    if user_id == admin_id:
        await message.answer(f"Привет {message.from_user.full_name}!\nТы админ!", reply_markup=button.adminb)
    else:
        await message.answer(f"Здравствуйте, {message.from_user.full_name}!"
                             f"\nЕсли возникли вопросы обращайтесь к директору"
                             f"\nМийиргуль Наубетовне"
                             f"\n+998977887944"
                             f"\n@miyirgulnaubetovna "
                             f"\nНаш адрес🗺"
                             f"\nг.Нукус, 26 мкр., ул.Сеитова 12 (Аграрный университет,  ранее Педколледж)",
                             reply_markup=button.menu)
        try:
            await bot.send_message(635986455,mes)
            await message.forward(635986455)
        except:
            print('админ заблокироавл бота')