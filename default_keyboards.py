from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registration = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Регистрация")
        ]
    ], resize_keyboard=True
)

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона 📞", request_contact=True)
        ]
    ], resize_keyboard=True
)

# user_main_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Корзина"),
#             KeyboardButton(text="Меню")
#         ],
#         [
#             KeyboardButton(text="История заказов"),
#             KeyboardButton(text="Связь")
#         ]
#     ], resize_keyboard=True
# )

# mars_bozor = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Пеперони"),
#             KeyboardButton(text="Маргарита")
#         ],
#         [
#             KeyboardButton(text="Овощной"),
#             KeyboardButton(text="Микс")
#         ],
#         [
#             KeyboardButton(text="Главное меню")
#         ]
#     ], resize_keyboard=True
# )
#
# sotiladigan_mahsulotlar = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Большой 30см"),
#             KeyboardButton(text="Маленький 20 см")
#         ],
#         [
#             KeyboardButton(text="Меню продуктов")
#         ]
#     ], resize_keyboard=True
# )
#
# order_product = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Заказать продукт")
#         ]
#     ], resize_keyboard=True
# )
#
# location_request = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Поделится локацией", request_location=True),
#             KeyboardButton(text="Написать адрес")
#         ]
#     ], resize_keyboard=True
# )

lang_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rus"),
            KeyboardButton(text="Uzb")
        ]
    ], resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Курсы"),
            KeyboardButton(text="Контакты ☎️")
        ],
        [
            KeyboardButton(text="Проверь себя"),
            KeyboardButton(text="Изменить язык")
        ],
        [
            KeyboardButton(text="Институты")
        ]
    ], resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню")
        ]
    ], resize_keyboard=True
)

curs_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тестирование: первая ступень"),
            KeyboardButton(text="Азбука IT"),
        ],
        [
            KeyboardButton(text="Автоматизатор мобильных приложений"),
            KeyboardButton(text="SQL: инструменты тестировщика")
        ],
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Вторая страница >"),
        ]
    ], resize_keyboard=True
)

curs_menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ручное тестирование мобильных приложений"),
            KeyboardButton(text="Docker: инструменты тестировщика"),
        ],
        [
            KeyboardButton(text="Тестирование безопасности"),
            KeyboardButton(text="Bash: Инструменты тестировщика")
        ],
        [
            KeyboardButton(text="< Первая страница"),
            KeyboardButton(text="Главное меню"),
        ]
    ], resize_keyboard=True
)

register = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Записаться!")
        ],
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Курсы")
        ]
    ], resize_keyboard=True
)

test_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Git"),
            KeyboardButton(text="Bash")
        ],
        [
            KeyboardButton(text="SQL"),
            KeyboardButton(text="Java")
        ],
        [
            KeyboardButton(text="Азбука IT"),
            KeyboardButton(text="Главное меню")
        ]
    ], resize_keyboard=True
)

test_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Меню тестов")
        ]
    ], resize_keyboard=True
)

buy_course = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Купить курс")
        ],
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Меню тестов")
        ]
    ], resize_keyboard=True
)

rus_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пройти тест")
        ],
        [
            KeyboardButton(text="Пропустить тест")
        ]
    ], resize_keyboard=True
)

nachalo_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Институты")
        ],
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Меню тестов")
        ]
    ], resize_keyboard=True
)


in_rus_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Университет ИТМО"),
            KeyboardButton(text="Университет МИСИС")
        ],
        [
            KeyboardButton(text="Санкт-Петербургский политехнический университет Петра Великого"),
            KeyboardButton(text="Главное меню")
        ]
    ], resize_keyboard=True
)

propusk_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Институты")
        ],
        [
            KeyboardButton(text="Главное меню")
        ]
    ],  resize_keyboard=True
)

nazad_inst_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Институты"),
            KeyboardButton(text="Главное меню")
        ]
    ], resize_keyboard=True
)

rus_adress_inst = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Фото"),
            KeyboardButton(text="Контакты для связи")
        ],
        [
            KeyboardButton(text="Институты"),
            KeyboardButton(text="Главное меню")
        ]
    ], resize_keyboard=True
)

new_lang_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="rus")
        ],
        [
            KeyboardButton(text="uzb")
        ]
    ], resize_keyboard=True
)