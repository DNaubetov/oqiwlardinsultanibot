from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from keyboards.default import button
from file.default import file
from loader import dp



@dp.message_handler(Text(equals=["Расписание"]))
async def time_table(message: Message):
    await message.answer("Выберите группу", reply_markup=button.timetable)

@dp.message_handler(Text(equals=["Расписание для 5-6-леток"]))
async def timetable1 (message: Message):
    await message.answer_photo(file.timetable_1)

@dp.message_handler(Text(equals=["Расписание для 6-7-леток"]))
async def timetable2 (message: Message):
    await message.answer_photo(file.timetable_2)
