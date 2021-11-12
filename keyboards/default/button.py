from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#Меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Записаться на бесплатный урок"),
        ],
        [
            KeyboardButton(text="Расписание"),

            KeyboardButton(text="Договор")
        ],
        [
            KeyboardButton(text="Стоимость образовательных услуг")
        ],
        [
            KeyboardButton(text="Учебные принадлежности")
        ],
        [
            KeyboardButton(text="Психологическая помощь родителям")
        ],
        [
            KeyboardButton(text="Государственные требования к развитию детей раннего и дошкольного возраста РУз")

        ],
        [
            KeyboardButton(text="Консультация психолога"),

            KeyboardButton(text="О нас"),
        ]
    ],
    resize_keyboard=True
)
# Клавиатура для расписание
timetable = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Расписание для 5-6-леток"),
        ],
        [
            KeyboardButton(text="Расписание для 6-7-леток"),
        ],
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True
)
#Клавиатура с кнопокой админа
adminb = ReplyKeyboardMarkup(
keyboard=[
        [
            KeyboardButton(text="Записаться на бесплатный урок"),
        ],
        [
            KeyboardButton(text="Расписание"),

            KeyboardButton(text="Договор")
        ],
        [
            KeyboardButton(text="Стоимость образовательных услуг")
        ],
        [
            KeyboardButton(text="Учебные принадлежности")
        ],
        [
            KeyboardButton(text="Психологическая помощь родителям")
        ],
        [
            KeyboardButton(text="Государственные требования к развитию детей раннего и дошкольного возраста РУз")
        ],
        [
            KeyboardButton(text="Консультация психолога"),

            KeyboardButton(text="О нас"),
        ],
        [
            KeyboardButton(text="Панель администратора")
        ],

    ],
    resize_keyboard=True
)

#Понель администратора
adminpanel= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассылка"),
        ],
        [
            KeyboardButton(text="Количество пользователей"),
        ],
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True
)
back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить контактные данные",request_contact=True),
        ]
    ],
    resize_keyboard=True
)



