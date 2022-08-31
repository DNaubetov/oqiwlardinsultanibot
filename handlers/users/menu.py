from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.types import MediaGroup
from keyboards.default import button,inline
from app import bot
from database.base import sqlighter
from file.default import file
from loader import dp
from config import admin_id

from aiogram.utils.markdown import hlink

db = sqlighter.SQLighter('database/base/db.db')
user_admin_id=765032644,635986455,330102092

# мой 635986455

url_instagram = "\n".join([hlink("📷 Инстаграмм", "https://instagram.com/oqiwlardin_sultani")])
url_telegramm = "\n".join([hlink("📲 Телеграмм", "https://t.me/oqiwlardinsultani")])


#Нажатие меню
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    user_id = message.from_user.id
    if  user_id == admin_id:
        await message.answer("Главное меню", reply_markup=button.adminb)
    else:
        await message.answer("Главное меню", reply_markup=button.menu)


@dp.message_handler(Text(equals=["Назад"]))
async def back_menu(message: Message):
    user_id = message.from_user.id
    if  user_id == admin_id:
        await message.answer("Главное меню", reply_markup=button.adminb)
    else:
        await message.answer("Главное меню", reply_markup=button.menu)


@dp.message_handler(Text(equals=["Государственные требования к развитию детей раннего и дошкольного возраста РУз"]))
async def button0(message: Message):
    user_id = message.from_user.id
    await bot.send_document(user_id, file.demand)


@dp.message_handler(Text(equals=["Психологическая помощь родителям"]))
async def button1(message: Message):
    await message.answer(text='⬇Ссылка на канал⬇', reply_markup=inline.channel_button)


@dp.message_handler(Text(equals=["О нас"]))
async def button2(message: Message):
    album=MediaGroup()
    for i in file.license:
        album.attach_photo(i)
    await message.answer_media_group(media=album)
    TEXT=f"\nНаш адрес🗺 "\
         f"\nг.Нукус, 27 мкр. Ориентир: Набережная канала «Дослык» "\
         f"\nМәнзил🗺" \
         f"\nНөкис қаласы, 27-киши район. Бағдар: «Дослық» каналы бойы" \
         f"\nМы в социальных сетях📱" \
         f"\n\n {url_instagram}" \
         f"\n {url_telegramm}" \
         f"\n\nКонтактный номер:" \
         f"\n+998 97 7887944"
    await message.answer_photo(file.director, caption="Информация о директоре")
    await message.answer_photo(file.certificate, caption=TEXT)


@dp.message_handler(Text(equals=["Учебные принадлежности"]))
async def button3(message: Message):
    user_id = message.from_user.id
    await message.answer(file.educational_supplies)
    await bot.send_document(user_id, file.study_supplies)


@dp.message_handler(Text(equals=["Стоимость образовательных услуг"]))
async def button4(message: Message):
    user_id = message.from_user.id
    await message.answer(file.price)
    await message.answer(text='Вы можете оплатить за обучение: '
                              '\n1) Через клик по номеру телефона (+998 97 7888 79 44) '
                              '\n2) Через бухгалтера (р/с 20212000100735995001- '
                              'в данном случае возможен возврат денег с подоходного налога)')


@dp.message_handler(Text(equals=["Консультация психолога"]))
async def echo(message: Message):
    await message.answer(text='Консультация родителей по психо-эмоциональному  состоянию и развитию '
                              'ребенка являются бесплатными. Для получения индивидуальной  психологической '
                              'помощи отправьте сообщение на номер или отправь свои контактные данные нажав на кнопку'
                              '\n+998 97 7888 79 44'
                              '\n\'Отправить контактные данные\'', reply_markup=button.contact)


@dp.message_handler(Text(equals=["Панель администратора"]), user_id=admin_id)
async def button5(message: Message):
    await message.answer(text='Что хотите сделать?', reply_markup=button.adminpanel)


@dp.message_handler(Text(equals=["Количество пользователей"]), user_id=admin_id)
async def button4(message: Message):
    info=db.get_userlist()
    info = [number_of_users[0] for number_of_users in info]
    number_of_users=len(info)
    await bot.send_message(admin_id, number_of_users)




#Работал сдесь, смог получить файл и переотправить его по ид document и photo
@dp.message_handler(content_types=['document'])
async def documen(message:Message):
    print(message)
    user_id=message.from_user.id
    # file_id = message.photo[-1].file_id
    file_id = message.document.file_id
    print(user_id)
    print(file_id)

    handle = open("l.txt", "a")
    handle.write(str(f'расписание\n{3}  {file_id}'))
    handle.close()
    # q='AgACAgIAAxkBAAIWPF891Gvlu10SUQL8cObaRo-58p_-AALprzEbbvToSYBxXuPQY1Jei0wSlS4AAwEAAwIAA3kAA1IpAwABGwQ'
    # d = 'AgACAgIAAxkBAAIS4l829R5Mi08-sgXyWfLEJXsk0Y2iAAIarjEb3zK4SZNZJq8Bcst1UoPuki4AAwEAAwIAA20ABCcFAAEaBA'
    # await bot.send_photo(user_id, file_id)
    # await bot.send_photo(user_id, q)


@dp.message_handler(content_types=types.ContentType.STICKER)
async def admin(message: Message):
    TO_CHAT_ID3 = 635986455
    user_id =message.from_user.id
    mes = message
    mest = message.sticker.file_id
    print(mes)
    print(mest)
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAIV_189tLyJT_buUC4FYJQ1hu2BQft8AAImVAACns4LAAGgo10P151lvxsE')
    print(message.bot.id)
    # print(reply_to_message_id)
    # 1234217208
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message:Message):
    print(message)
    # await message.answer(text='Спасибо!'
    #                           '\nНаш психолог свяжется с вами',reply_markup=button.menu)
    # await bot.send_contact(admin_id, message.contact.phone_number, message.contact.first_name,
    #                        message.contact.last_name, message.contact.user_id)