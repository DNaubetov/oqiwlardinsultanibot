from aiogram import types
from aiogram.dispatcher.filters import Text
from database.base import sqlighter
from keyboards.default import button
from app import bot
import time
from loader import dp
from states.test import Test
from aiogram.dispatcher import FSMContext
from config import admin_id

db = sqlighter.SQLighter('database/base/db.db')

@dp.message_handler(Text(equals=["Рассылка"]),user_id=admin_id, state=None)
async def enter_test(message: types.Message):
    await message.answer("Введите текст",reply_markup=button.back)
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1,user_id=admin_id)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer=='Назад':
        await state.finish()
        await message.answer(f"Вы отменили рассылку!",reply_markup=button.adminpanel)
    else:
        await message.answer(f"Ваш текст отправлен всем! \n{answer}")
        TO_CHAT_ID = db.get_userlist()
        TO_CHAT_ID = [i[2] for i in TO_CHAT_ID]
        for i in range(len(TO_CHAT_ID)):
            try:
                await bot.send_message(TO_CHAT_ID[i], answer,reply_markup=button.menu)
                await bot.send_message(admin_id, f'{TO_CHAT_ID[i]}-Получил')

            except:
                db.delete_users(TO_CHAT_ID[i])
            if i % 25 == 0:
                time.sleep(2)
        await state.finish()

