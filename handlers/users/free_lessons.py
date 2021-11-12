from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentType

from keyboards.default import button
from app import bot
from file.default import file
from loader import dp
from states.test import Test
from aiogram.dispatcher import FSMContext
from config import admin_id



@dp.message_handler(Text(equals=["Записаться на бесплатный урок"]), state=None)
async def free_lessons(message: types.Message):
    await message.answer(file.free_lesson_text)
    await message.answer(text='Для записи на бесплатный урок, Вам нужно написать:\
\n\n👫ФИО ребёнка\
\n🎉Год, число и месяц рождения \
\n📱 Ваш номер телефона',reply_markup=button.back)
    await Test.E1.set()



@dp.message_handler(state=Test.E1)
async def message_e1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer=='Назад':
        await state.finish()
        await message.answer(f"Главное меню!", reply_markup=button.menu)
    else:
        await state.update_data(answer1=answer)
        await message.answer(text='📱 Ваш номер телефона\nНажмите отправить контактные данные',reply_markup=button.contact)
        await Test.E2.set()


@dp.message_handler(content_types=ContentType.ANY,state=Test.E2)
async def message_e2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    if message.content_type=='text':
        await message.answer_document(file.free_lesson,caption='Спасибо за ответы, Вам перезвонят и сообщат дату бесплатного занятия.',reply_markup=button.menu)
        await bot.send_message(admin_id, text=f'Ответы на вопросы👇🏻👇🏻👇🏻'
                                              f'\n    {answer1} \n    {message.text}')
        await state.finish()
    elif message.contact.user_id!=message.from_user.id:
       await message.answer(text='Вы пытаетесь отправить чужой номер, просим вас выслать свой!'
                                 '\nНажав на кнопку:\n✅\'Отправить контактные данные\'✅')
       await Test.E2.set()
    else:
        await message.answer_document(file.free_lesson,caption='Спасибо за ответы, Вам перезвонят и сообщат дату бесплатного занятия.',reply_markup=button.menu)
        await bot.send_message(admin_id,text=f'Ответы на вопросы 👇🏻👇🏻👇🏻'
                                             f'\n{answer1}')
        await bot.send_contact(admin_id,message.contact.phone_number,message.contact.first_name,message.contact.last_name,message.contact.user_id)
        await state.finish()