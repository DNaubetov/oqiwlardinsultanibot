from aiogram.types import Message, ReplyKeyboardRemove
from app import bot
from keyboards.default import button
from loader import dp
from config import admin_id

@dp.message_handler()
async def echo(message: Message):

    user_id =message.from_user.id
    mes=message
    mest=message.text
    print(mes)
    print(user_id, mest)
    text = f"Вы написали: {message.text}!" \
           f"\nВведи /menu если что то нужно!" \
           f"\nПо всем вопросам пишите:@miyirgulnaubetovna" \
           f"\nСорауларыныз болса, @miyirgulnaubetovna, хабарласын" \
           f"\nЕсли что-то не исправно пишите:@DNaubetov"
    await bot.forward_message(admin_id, message.chat.id, message.message_id)
    await bot.send_message(admin_id, text='Новое сообщение', reply_markup=button.adminpanel)
    await message.reply(text=text, reply_markup=button.menu)
