from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.types import MediaGroup
from keyboards.default import button,inline
from app import bot
from database.base import sqlighter
from file.default import file
from loader import dp



admin_id=330102092

@dp.message_handler(Text(equals=["Договор"]))
async def contract (message: Message):
    #отправка договора для ДО
    # album_online_contract=MediaGroup()
    # g='AgACAgIAAxkBAAIWqF897dnTPoK5QLh0OUEETw4jLWChAALRrTEbjKPwSfnkTNBk04NQcqFMli4AAwEAAwIAA20AAz7nAAIbBA'
    # album_online_contract.attach_photo(g,caption=f'ДОГОВОР НОУ для дистанционного обучения')
    # for i in file.Contract:
    #     album_online_contract.attach_photo(i)
    #
    # # await bot.send_media_group(user_id,media=album)
    # await message.answer_media_group(media=album_online_contract)
    #
    # #отправка договра
    # album_offline_contract = MediaGroup()
    # g = 'AgACAgIAAxkBAAIWqF897dnTPoK5QLh0OUEETw4jLWChAALRrTEbjKPwSfnkTNBk04NQcqFMli4AAwEAAwIAA20AAz7nAAIbBA'
    # album_offline_contract.attach_photo(g, caption=f'ДОГОВОР НОУ')
    # for i in file.Contractoff:
    #     album_offline_contract.attach_photo(i)
    #
    # # await bot.send_media_group(user_id,media=album)
    # await message.answer_media_group(media=album_offline_contract)


    # user_id = message.from_user.id
    # #отпраква договора для ДО
    # number_file_0=0
    # for i in file.Contract:
    #     number_file_0+=1
    #     await bot.send_photo(user_id, i,caption=f'ДОГОВОР НОУ для дистанционного обучения'
    #                                             f'\nСтраница №=\'{number_file_0}\' из \'{len(file.Contract)}\'')
    #
    # #отправка офлайн догвора
    # user_id = message.from_user.id
    # number_file_1=0
    # for i in file.Contractoff:
    #     number_file_1+=1
    #     await bot.send_photo(user_id, i,caption=f'ДОГОВОР НОУ'
    #                                             f'\nСтраница №=\'{number_file_1}\'из\'{len(file.Contractoff)}\'')

    # text = f'{file.price}\n'
    await message.answer_document(file.contractoff)
    await message.answer_document(file.contract)
    await message.answer(file.price)
    await message.answer(text='⬇Форма для заполнения⬇', reply_markup=inline.contract_button)
    await message.answer(text='Вы можете оплатить за обучение через клик \nПо номеру телефона\n+998 97 7887944')

