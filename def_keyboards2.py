from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


tel_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon nomer jo'natish 📞", request_contact=True)
        ]
    ], resize_keyboard=True
)


# lang_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Rus"),
#             KeyboardButton(text="Uzb")
#         ]
#     ], resize_keyboard=True
# )

asos_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
            KeyboardButton(text="Kontakt ☎️")
        ],
        [
            KeyboardButton(text="O'zingni sina"),
            KeyboardButton(text="Til o'zgartirish")
        ],
        [
            KeyboardButton(text="Institutlar")
        ]
    ], resize_keyboard=True
)

orqa = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asosiy menu")
        ]
    ], resize_keyboard=True
)

kursla_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sinov: birinchi bosqich"),
            KeyboardButton(text="Azbuka IT"),
        ],
        [
            KeyboardButton(text="Mobil ilovalar avtomatlantirish"),
            KeyboardButton(text="SQL: Tester asboblari")
        ],
        [
            KeyboardButton(text="Asosiy menu"),
            KeyboardButton(text="Ikkinchi bet >"),
        ]
    ], resize_keyboard=True
)


kursla_menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mobil ilovalarni qo'lda sinovdan o'tkazish"),
            KeyboardButton(text="Docker: sinov vositalari"),
        ],
        [
            KeyboardButton(text="Xavfsizlik sinovi"),
            KeyboardButton(text="Bash: Tester asboblari")
        ],
        [
            KeyboardButton(text="< Birinchi bet"),
            KeyboardButton(text="Asosiy menu"),
        ]
    ], resize_keyboard=True
)


register_qilish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yozilish!")
        ],
        [
            KeyboardButton(text="Asosiy menu"),
            KeyboardButton(text="Kurslar")
        ]
    ], resize_keyboard=True
)

testla_testla = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Git."),
            KeyboardButton(text="Bash.")
        ],
        [
            KeyboardButton(text="SQL."),
            KeyboardButton(text="Java.")
        ],
        [
            KeyboardButton(text="Azbuka IT"),
            KeyboardButton(text="Asosiy menu")
        ]
    ], resize_keyboard=True
)

testla_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asosiy menu"),
            KeyboardButton(text="Testlar menusi")
        ]
    ], resize_keyboard=True
)


sotib_course = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurs sotib olish")
        ],
        [
            KeyboardButton(text="Asosiy menu"),
            KeyboardButton(text="Testlar menusi")
        ]
    ], resize_keyboard=True
)


uzb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sinovdan o'tish")
        ],
        [
            KeyboardButton(text="Sinovni o'tkazib yuborish")
        ]
    ], resize_keyboard=True
)

bosh_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Institutlar")
        ],
        [
            KeyboardButton(text="Asosiy menu"),
            KeyboardButton(text="Testlar menusi")
        ]
    ], resize_keyboard=True
)


in_uzb_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti"),
            KeyboardButton(text="MISIS universiteti")
        ],
        [
            KeyboardButton(text="Buyuk Pyotr Sankt-Peterburg politexnika universiteti"),
            KeyboardButton(text="Asosiy menu")
        ]
    ], resize_keyboard=True
)


otish_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Institutlar")
        ],
        [
            KeyboardButton(text="Asosiy menu")
        ]
    ],  resize_keyboard=True
)

uzb_adress_inst = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rasm"),
            KeyboardButton(text="Aloqa uchun kontaktlar")
        ],
        [
            KeyboardButton(text="Institutlar"),
            KeyboardButton(text="Asosiy menu")
        ]
    ], resize_keyboard=True
)