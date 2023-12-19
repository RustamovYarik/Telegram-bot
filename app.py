from aiogram import types, executor, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from notify_admins import on_startup_notify
from set_bot_commands import set_default_commands
from states import RegisterState, RegisterStateUz
# from states.mahsulot import AddProduct
from aiogram.dispatcher import FSMContext
from default_keyboards import *
from def_keyboards2 import *
from inline_keyboards import *
# from keyboards.inline.aloqa import admin_aloqa
from database import DatabaseManager
from aiogram.types import ReplyKeyboardRemove
from config import ADMINS
from adress_state import *


db_manager = DatabaseManager("learning.db")
# db_manager.create_tables()
# db_manager.delete_table()
async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)

# @dp.message_handler(commands="start")
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
        text = "🇷🇺 Привет, выберите язык.\n🇺🇿 Salom, til tanlang."
        await message.answer(text=text, reply_markup=lang_keyboard)



@dp.message_handler(text="Rus")
async def get_handler(message: types.Message):
    # await state.update_data(kirish="1")
    text = 'Здравствуйте, это бот сайта "LearnQA" который, рекомендует вам множество курсов и институтов для программистов.\nНаучитесь тестировать с нуля или повышайте свою квалификацию под руководством опытных тренеров.\n\nДля начала, пройдите тест что бы определить свой уровень знания'
    await message.answer(text=text, reply_markup=rus_test)

@dp.message_handler(text="rus")
async def get_handler(message: types.Message):
    text = "Язык изменён на русский"
    await message.answer(text=text, reply_markup=main_menu)

@dp.message_handler(text="uzb")
async def get_handler(message: types.Message):
    text = "Tilni o'zbek tiliga ozgartirildi"
    await message.answer(text=text, reply_markup=asos_menu)

@dp.message_handler(text="Uzb")
async def get_handler(message: types.Message):
    # await state.update_data(kirish="1")
    text = "Salom, bu 'LearnQA' veb-saytidagi bot bo'lib, sizga ko'plab kurslar va dasturchilar uchun institularni tavsiya qiladi.\nTajribali murabbiylar rahbarligida noldan sinab ko'rishni yoki mahoratingizni oshirishni o'rganing.\n\nBirinchidan, bilim darajangizni aniqlash uchun testdan o'ting."
    await message.answer(text=text, reply_markup=uzb_test)

# @dp.message_handler(text="Rus")
# async def get_handler(message: types.Message, state: FSMContext):
#     await state.update_data(kirish="1")
#     text = ""
#     data = await state.get_data()
#     kirish_name = data.get("kirish")
#     if kirish_name == 1:
#         text = "Язык изменён на русский"
#         await message.answer(text=text, reply_markup=main_menu)
#     else:
#         text = "Salom, bu 'LearnQA' veb-saytidagi bot bo'lib, sizga ko'plab kurslar va dasturchilar uchun institularni tavsiya qiladi.\nTajribali murabbiylar rahbarligida noldan sinab ko'rishni yoki mahoratingizni oshirishni o'rganing.\n\nBirinchidan, bilim darajangizni aniqlash uchun testdan o'ting."
#         await message.answer(text=text, reply_markup=uzb_test)
#
#
#
# @dp.message_handler(text="Rus")
# async def get_handler(message: types.Message):
#     await state.update_data(kirish="1")
#     text = ""
#     await message.answer(text=text, reply_markup=uzb_test)



@dp.message_handler(text="Пропустить тест")
async def get_handler(message: types.Message):
    text = "Вы пропустили тест"
    await message.answer(text=text, reply_markup=propusk_test)

@dp.message_handler(text="Университет ИТМО")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(inst="Университет ИТМО")
    photo = "https://upload.wikimedia.org/wikipedia/commons/c/cc/ITMO_University%27s_main_building%2C_August_2016.jpg"
    text = """Университет ИТМО\n\n
российское федеральное государственное учебное заведение заведение
высшего и послевузовского образования, с 2009 года — национальный
исследовательский университет (НИУ).Приоритетные направления вуза — информационные
технологии, искусственный интеллект, фотоника, робототехника, квантовые коммуникации,
трансляционная медицина, науки о жизни (Life Sciences), Art&Science, научная коммуникация.
Команда ИТМО по спортивному программированию — единственный в мире семикратный чемпион
крупнейшей международной студенческой олимпиады ICPC.Вуз входит в топ-5 российских вузов
по качеству бюджетного приёма, один из лидеров по уровню зарплат IT-выпускников.
Учебное заведение ведёт историю от 26 марта 1900 года, когда в Ремесленном училище цесаревича
Николая было открыто Механико-оптическое и часовое отделение. После революции в 1917 году
отделение выделилось в самостоятельное учебное заведение — Петроградское техническое училище
по механико-оптическому и часовому делу и в 1920 году было преобразовано в Петроградский техникум
точной механики и оптики (позже — Ленинградский); в 1920-х годах техникуму было
предоставлено здание в Демидовом переулке (переулок Гривцова), современное главное здание
на Саблинской улице (фасадом на Кронверкский проспект) было построено в 1970-е.
    """
    await message.answer(text=text, reply_markup=rus_adress_inst)

@dp.message_handler(text="Фото")
async def plus_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # await state.update_data(inst="Photo")
    product_name = data.get("inst")
    photo = ""
    text = ""
    if product_name == "Университет ИТМО":
        photo = "https://upload.wikimedia.org/wikipedia/commons/c/cc/ITMO_University%27s_main_building%2C_August_2016.jpg"
        text = "Университет ИТМО"

    elif product_name == "Университет МИСИС":
        photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Korpus_b.jpg/1200px-Korpus_b.jpg"
        text = "Университет МИСИС"

    elif product_name == "Санкт-Петербургский политехнический университет Петра Великого":
        photo = "https://alfakom.uz/images/img/partners/spbstu_1.jpg"
        text = "Санкт-Петербургский политехнический университет Петра Великого"

    elif product_name == "Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti":
        photo = "https://upload.wikimedia.org/wikipedia/commons/c/cc/ITMO_University%27s_main_building%2C_August_2016.jpg"
        text = "Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti"

    elif product_name == "MISIS universiteti":
        photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Korpus_b.jpg/1200px-Korpus_b.jpg"
        text = "MISIS universiteti"

    elif product_name == "Buyuk Pyotr Sankt-Peterburg politexnika universiteti":
        photo = "https://alfakom.uz/images/img/partners/spbstu_1.jpg"
        text = "Buyuk Pyotr Sankt-Peterburg politexnika universiteti"

    await message.answer_photo(photo=photo, caption=text)


@dp.message_handler(text="Контакты для связи")
async def plus_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # await state.update_data(inst="Photo")
    product_name = data.get("inst")
    photo = ""
    text = ""
    if product_name == "Университет ИТМО":
        text = """
КАНЦЕЛЯРИЯ
+7 (812) 480-00-00
Факс: +7 (812) 232-23-07
od@itmo.ru
ПРИЁМНАЯ КОМИССИЯ
+7 (812) 480-04-80
abit@itmo.ru
ЦЕНТР РЕКРУТИНГА
job@itmo.ru
СТУДЕНЧЕСКИЙ ОФИС
+7 (812) 607-04-74
so@itmo.ru
ОФИС ПОДДЕРЖКИ СОТРУДНИКОВ
+7 (812) 607-02-50
faculty@itmo.ru
ПРЕСС-СЛУЖБА
+7 (900) 630-00-10
pressa@itmo.ru
        """
    elif product_name == "Университет МИСИС":
        text = """
Юридический и фактический адрес: 119049, Москва, Ленинский пр-кт, д. 4, стр. 1.
Телефон: +7 495 955-00-32
Факс: +7 499 236-21-05
График работы административных подразделений: пн.-пт. 9:00-18:00.
График обучения студентов: пн.-пт. с 9:00-21:00, сб. 9:00-18:00.
        """
    elif product_name == "Санкт-Петербургский политехнический университет Петра Великого":
        text = """
+7 (812) 775-05-30
- для звонков из Санкт-Петербурга
 8 (800) 707-18-99
- для звонков из любого региона РФ (звонок бесплатный)
        """
    elif product_name == "Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti":
        text = """
IDORA
+7 (812) 480-00-00
Faks: +7 (812) 232-23-07
od@itmo.ru
TANLOV QO'MITI
+7 (812) 480-04-80
abit@itmo.ru
ISHLASH MARKAZI
job@itmo.ru
Talabalar idorasi
+7 (812) 607-04-74
so@itmo.ru
XODIMLARNI QO'LLAB-QUVVAT BO'LISHI
+7 (812) 607-02-50
faculty@itmo.ru
MATBUOT XIZMATI
+7 (900) 630-00-10
pressa@itmo.ru
        """
    elif product_name == "MISIS universiteti":
        text = """
Yuridik va haqiqiy manzil: 119049, Moskva, Leninskiy prospekti, 4, 1-bino.
Telefon: +7 495 955-00-32
Faks: +7 499 236-21-05
Ma'muriy bo'limlarning ish vaqti: Dus.-Jum. 9:00-18:00.
Talabalar dars jadvali: dushanba-juma. 9:00 dan 21:00 gacha, shanba. 9:00-18:00.
        """
    elif product_name == "Buyuk Pyotr Sankt-Peterburg politexnika universiteti":
        text = """
+7 (812) 775-05-30
- Sankt-Peterburgdan qo'ng'iroqlar uchun
 8 (800) 707-18-99
- Rossiya Federatsiyasining istalgan mintaqasidan qo'ng'iroqlar uchun (qo'ng'iroq bepul)
        """

    await message.answer(text=text)


@dp.message_handler(text="Университет МИСИС")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(inst="Университет МИСИС")
    text = """
Университет специализируется на создании, внедрении и применении новых
технологий и материалов. Институт компьютерных наук выпускает IT-специалистов
с профилем в искусственном интеллекте, исследованиях Big Data и Computer Science,
разработке программ и приложений. Интересные для программистов факультеты: информатика
и вычислительная техника, информационные системы и технологии.\n
Национальный исследовательский технологический университет МИСиС — российский технический 
университет.. В состав НИТУ МИСиС входит 8 институтов и 6 филиалов – четыре в России и
два за рубежом. В университете около 22 000 обучающихся, 25% студентов – это граждане
из 85 стран мира.Один из ведущих российских вузов в сфере материаловедения, металлургии
и горного дела. В рэнкинге национального мониторинга по качеству приёма, который составляет
ВШЭ, в 2021 году занял 13-е место (средний балл ЕГЭ вырос до 88,8), пять лет подряд занимает
четвёртое место среди лучших технических вузов страны.В основе образовательной модели
вуза — интеграция образования и науки. Университет сочетает фундаментальную подготовку студентов
с проектно- и практико- ориентированным подходом к обучению, активно привлекая к сотрудничеству
академических и бизнес-партнеров НИТУ «МИСиС».

Университет сотрудничает более чем с 1600 крупнейшими компаниями России и мира.
Благодаря комплексной программе профессиональной навигации средний балл ЕГЭ поступающих в
университет вырос с 67,3 в 2012 году до 88,8 баллов в 2021 году
    """
    await message.answer(text=text, reply_markup=rus_adress_inst)


@dp.message_handler(text="Санкт-Петербургский политехнический университет Петра Великого")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(inst="Санкт-Петербургский политехнический университет Петра Великого")
    text = """
Санкт-Петербургский политехнический университет Петра Великого – крупнейший
технический вуз страны с исторически сложившимися сильнейшими научными школами,
имеющий неоспоримые результаты и достижения в научной, образовательной и
инновационной деятельности. Основываясь на ключевых мировых тенденциях развития
сферы исследований, разработок, технологий и образования, к 2030 году стремится войти
в сотню лучших университетов мира, встав в один ряд с лидерами мирового образования.
В этом году СПбПУ Петра Великого обновил концепцию приема. Концепция приема 2022/2023 -
Мы знаем, что надо делать. Так, Политех показывает своим абитуриентам, что мы находимся
в потоке информации и знаем, что нужно делать, чтобы стать успешным, добиться цели,
готовы направлять студентов для того, чтобы быть в тренде.Санкт-Петербургский политехнический
университет Петра Великого – крупнейший технический вуз страны с исторически сложившимися
сильнейшими научными школами, имеющий неоспоримые результаты и достижения в научной,
образовательной и инновационной деятельности. Основываясь на ключевых мировых тенденциях
развития сферы исследований, разработок, технологий и образования, к 2030 году стремится
войти в сотню лучших университетов мира, встав в один ряд с лидерами мирового образования.
В этом году СПбПУ Петра Великого обновил концепцию приема. Концепция приема 2022/2023 -
Мы знаем, что надо делать. Так, Политех показывает своим абитуриентам, что мы находимся
в потоке информации и знаем, что нужно делать, чтобы стать успешным, добиться цели,
готовы направлять студентов для того, чтобы быть в тренде.
    """
    await message.answer(text=text, reply_markup=rus_adress_inst)


@dp.message_handler(text="Пройти тест")
async def get_handler(message: types.Message):
    text = "Нажмите на ссылку ниже и пройдите тест\nhttps://www.learnqa.ru/abc_test\n\n\nА так же мы рекомендуем вам посмотреть список институтов нажав на кнопку ниже"
    await message.answer(text=text, reply_markup=nachalo_test)


@dp.message_handler(text="Институты")
async def get_handler(message: types.Message):
    text = "Мы рекомендуем вам три института"
    await message.answer(text=text, reply_markup=in_rus_list)

# @dp.message_handler(text="Пройти тест")
# async def get_handler(message: types.Message):
#     text = "А так же мы рекомендуем вам посмотреть список институтов нажав на кнопку ниже"
#     await message.answer(text=text)

@dp.message_handler(text="Til o'zgartirish")
async def get_handler(message: types.Message):
    text = "Tilni o'zgartiring"
    await message.answer(text=text, reply_markup=new_lang_keyboard)

@dp.message_handler(text="Изменить язык")
async def get_handler(message: types.Message):
    text = "Выберите язык"
    await message.answer(text=text, reply_markup=new_lang_keyboard)


@dp.message_handler(text="Курсы")
async def get_handler(message: types.Message):
    text = "Выберите курс"
    await message.answer(text=text, reply_markup=curs_menu)

@dp.message_handler(text="Контакты ☎️")
async def get_handler(message: types.Message):
    text = """Арсений Батыров\n
Почта: arsbatyrov@gmail.com
Telegram: @arsbatyrov\n
Виталий Котов\n
Почта: vinkotov@gmail.com
Telegram: @vinkotov\n

    """
    await message.answer(text=text, reply_markup=back)

@dp.message_handler(text="Проверь себя")
async def get_handler(message: types.Message):
    text = "Тесты и тренажеры для тестировщиков"
    await message.answer(text=text, reply_markup=test_test)

@dp.message_handler(text="Главное меню")
async def get_handler(message: types.Message):
    text = "назад в главное меню"
    await message.answer(text=text, reply_markup=main_menu)

@dp.message_handler(text="Вторая страница >")
async def get_handler(message: types.Message):
    text = "Страница 2"
    await message.answer(text=text, reply_markup=curs_menu2)

@dp.message_handler(text="< Первая страница")
async def get_handler(message: types.Message):
    text = "Страница 1"
    await message.answer(text=text, reply_markup=curs_menu)

@dp.message_handler(text="Тестирование: первая ступень")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Тестирование: первая ступень")
    text = """Тестирование — востребованная профессия\n\n
Тестировщик — специалист, занимающийся обеспечением качества программ, которые
разрабатывают программисты: вебсайтов, десктопных и мобильных приложений. Для этого он ищет
проблемы в приложениях, оформляет их и сообщает разработчикам. Именно благодаря
тестированию продукт, попадающий к конечному пользователю, идеально работает и имеет все
конкурентные преимущества.\n\n
На этом курсе мы рассмотрим базовую теорию, необходимую для того, чтобы стать тестировщиком и
начать свой пусть в IT. Мы на практике покажем важные для тестировщика техники и инструменты:\n
Тест-кейсы и чек-листы
Тест-дизайн
Багтрекеры и багрепорты
Классификацию тестирования
Системы управления тестированием
Инструменты тестирования: SQL, Git, Bash, Postman, Selenium, Appium и другие\n\n
Мы много времени уделим именно практике. Специально для этого курса мы
подготовили:\n
тестовую песочницу, на которой можно будет поупражняться в поиске багов и составлению тест-кейсов.
багтрекер, который можно будет посмотреть на практике
тестовую базу данных для демонстрации ее работы\n
Все это будет доступно как в течение курса, так и после его прохождения.\n
Формат курса - более 20 видеозаписей с подробным разбором заявленных в
программе тем. Суммарно все видео занимают час, но они довольно плотно
смонтированы по информации, без воды, так что на изучение и осознание скорее
всего потребуется больше времени.\n
Курс не ограничен по срокам, так что можно купить и проходить в том темпе и в то
время, когда удобно.\n
Посмотрите пример занятия
https://youtu.be/e0cHqx5cRPo
    """
    await message.answer(text=text, reply_markup=register)

@dp.message_handler(text="Азбука IT")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Азбука IT")
    text = """Базовые навыки IT-специалиста\n\n
Начинающему тестировщику нужно обладать широким кругозором: сфера IT
развивается очень быстро, и оставаться в курсе всех инноваций непросто. Но
именно такие специалисты особенно ценятся на рынке труда. С этой задачей
справиться проще всего тем, кто уже достаточно опытен в использовании
компьютера. Именно понимание азов позволяет получать актуальные знания
без особых усилий.\n
Как ни странно, получить такую базу в структурированном виде достаточно
сложно. IT-курсы чаще всего рассчитаны на тех, кто уже работает в этой сфере и
обладает большим количеством навыков. Опытные тренеры не могут
представить, что их ученики могут не знать самых простых вещей.\n
Чтобы начать работать в IT, неплохо бы разбираться в операционных системах
и их особенностях, уметь работать с файловой системой и консолью, знать про
устройство и принципы работы сети, понимать, что такое клиент-серверная
архитектура приложения, а также владеть множеством других подобных
базовых тем.\n
Курс Азбука IT раскрывает основные моменты из самых разнообразных
областей мира информационных технологий. Вы получите ту самую базу, с
которой сможете проходить почти любые IT-курсы без особых проблем и даже
начать работать на позиции Junior. Мы сделали программу максимально
доступной для тех, кто не сталкивается с информационными технологиями
каждый день.\n
Посмотрите пример занятия
https://youtu.be/zLAieW59fgs
    """
    await message.answer(text=text, reply_markup=register)

@dp.message_handler(text="Автоматизатор мобильных приложений")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Автоматизатор мобильных приложений")
    text = """Навыки мобильной автоматизации\n\n
Автоматизатор мобильных приложений — одна из самых высокооплачиваемых
профессий на рынке IT. Однако, из-за дефицита кадров, многие компании сталкиваются с
проблемой поиска специалистов в этой области. Поэтому, если вы хотите стать
востребованным тестировщиком, вам необходимо освоить навыки автоматизации.\n
Наш курс предоставляет все необходимые знания для самостоятельной настройки полного
стека автоматизации тестирования мобильных приложений с нуля. Мы не просто учим, как
писать тесты или настраивать среду тестирования, так как этого недостаточно в работе. Мы
учим создавать автоматизацию тестирования на проекте с самого начала, а также
развивать и поддерживать ее на всех этапах разработки и тестирования продукта.\n
На наших занятиях вы:\n
Освоите работу с обеими платформами — iOS и Android;
Изучите автоматизацию Web на примере Mobile Web приложения;
Освоите правильные инструменты, которые подходят именно под вашу работу;
Настроите среду автоматизации с нуля на Windows, MacOS или Linux;
Узнаете, как поднимать Jenkins и запускать тесты в CI-системе;
Разработаете собственный тестовый фреймворк;
Добавите удобные и понятные отчеты о прохождении тестов на Allure;
Создадите большой проект по автоматизации, который будет у вас на Github и который можно
смело добавить в свое резюме.\n
Закончив курс, вы сможете добавить итоговый проект в свое резюме, а также
использовать полученные знания на практике, как это делают многие наши выпускники.
    """
    await message.answer(text=text, reply_markup=register)

@dp.message_handler(text="SQL: инструменты тестировщика")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="SQL: инструменты тестировщика")
    text = """SQL — инструмент тестировщика\n\n
Вы хотите устроиться на работу, но на каждом втором собеседовании просят
написать SQL-запрос? Или вам нужно получить тестовые данные из базы?
Или у вас баг в веб-форме, и вы проверяете наличие значений в БД?\n
Для всего этого — и многого другого — достаточно будет овладеть работой с
реляционными базами данных и SQL. С помощью SQL можно создавать и
удалять базы, вносить значения, и самое главное для тестировщика —
получать данные в нужном виде.\n
Приходите на курс, и всего за 2 недели научитесь:\n
Получать и сортировать данные из БД;
Настраивать фильтры;
Проводить вычисления;
Группировать данные и таблицы;
Работать с подзапросами и комбинированными запросами;
Добавлять и менять данные в БД;
Создавать таблицы и базы данных.\n
Посмотрите пример занятия
https://youtu.be/PTAkqURmI0s
    """
    await message.answer(text=text, reply_markup=register)

@dp.message_handler(text="Ручное тестирование мобильных приложений")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Ручное тестирование мобильных приложений")
    text = """Мобильное тестирование — новая отрасль\n\n
Часто пользуетесь мобильным телефоном, и хотите пойти в мобильные
тестировщики? Или уже работаете в веб-тестировании, но хочется чего-то
нового? А может, вы уже тестируете мобилки, но хотите прокачать свои
навыки?\n
Популярность мобильных телефонов растет: каждый год выходят более 5 000
новых моделей, а мобильный трафик составляет 58% от всеобщей доли
пользования интернетом. Естественно, приложений становится больше, а
значит — есть запрос на мобильных тестировщиков.\n
На этом курсе мы не будем рассматривать теорию тестирования — в
мобильном тестировании она не отличается от обычной. Мы
сконцентрируемся на специфичных для отрасли моментах:\n
Особенностях мобильного тестирования
Эмуляторах и симуляторах
IDE и инструментах для Android и iOS
Мобильных девайсах
Мобильных приложениях и их видах\n
Посмотрите пример занятия
https://youtu.be/sPPWOZxEl9w
    """
    await message.answer(text=text, reply_markup=register)

@dp.message_handler(text="Docker: инструменты тестировщика")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Docker: инструменты тестировщика")
    text = """Docker — инструмент тестировщика\n\n
Вы хотите устроиться на работу, но там требуют умение работать с
контейнерами? А может хотите научиться запускать в Docker свои тесты на
Selenium? Или хотите легко использовать нужный в работе софт, не разбираясь
с его установкой?\n
Для всего этого (и многого другого) достаточно будет научиться работать с
инструментом контейнеризации Docker. С его помощью можно создавать,
запускать и распространять контейнеры с нужным вам софтом, настраивать
взаимодействие тестов и CI, добавлять различные версии языков
программирования для проверки ваших программ, держать вашу машину
чистой и делать еще десяток задач, с которыми тестировщик сталкивается
каждый день.\n
Приходите на курс, и всего за 2 недели научитесь:\n
Настраивать Docker на любой современной ОС
Создавать, подключать и удалять контейнеры
Делать собственные образы и тома
Настраивать взаимодействие программ через бинды и тома
Запускать в контейнерах тесты и любые программы
Подключать контейнеры к сети\n
Посмотрите пример занятия
https://youtu.be/GsnXl87lYzg
    """
    await message.answer(text=text, reply_markup=register)


@dp.message_handler(text="Тестирование безопасности")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Тестирование безопасности")
    text= """Тестирование безопасности\n\n
Никогда не пробовали тестировать безопасность? Думаете, что это сложно,
долго и только для избранных? Кончились идеи для тестирования вашего
приложения?\n
Видимо, самое время наконец-то освоить тестирование безопасности. Это
совсем не так сложно, как кажется, достаточно просто понять основные
принципы работы приложений и использования приемов поиска популярных
уязвимостей. Отработайте их на практике — и сразу сможете улучшить
тестирование на своем проекте.\n
Приходите на курс, и всего за 4 недели научитесь:\n
Находить уязвимости в формах
Работать с HTML, JS и XSS инъекциями
Искать SQL-инъекции в разных запросах
Использовать бекдоры и перехватывать shell
Применять социальную инженерию и защищаться от нее
Выбирать сканеры для автоматической проверки\n
Посмотрите пример занятия
https://youtu.be/6cumnXMijbQ
    """
    await message.answer(text=text, reply_markup=register)

@dp.message_handler(text="Bash: Инструменты тестировщика")
async def get_nadler(message: types.Message, state: FSMContext):
    await state.update_data(course="Bash: Инструменты тестировщика")
    text = """Bash — инструмент тестировщика\n\n
Вы хотите устроиться на работу, но там требуют знания Linux? А может, вам
нужно каждый день работать с объемными файлами? Или вы хотите
снимать логи с устройств? Научиться видеть женщин в красном платье в
строках кода?\n
Для всего этого (и многого другого) достаточно будет овладеть работой с
командной оболочкой Bash. С ее помощью можно создавать, искать и менять
файлы, отслеживать процессы, логиниться на удаленные машины и делать еще
сотни задач, с которыми тестировщик сталкивается каждый день.\n
Приходите на курс, и всего за 2 недели научитесь:\n
Работать с файлами и папками через консоль;
Искать внутри файлов, директорий и дерева процессов;
Выделять и обрабатывать запущенные в системе программы;
Записывать любую информацию в файлы;
Настраивать удобную и информативную консоль.\n
Посмотрите пример занятия
https://youtu.be/JQXM4ArzyU4
    """
    await message.answer(text=text, reply_markup=register)


@dp.message_handler(text="Записаться!")
async def products_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(course="Записаться!")
    course_name = data.get("course")
    text = ""
    if course_name == "Тестирование: первая ступень":
        text = "Цена курса: 2 000 ₽"
    elif course_name == "Азбука IT":
        text = "Цена курса: 3 500 ₽"
    elif course_name == "Автоматизатор мобильных приложений":
        text = "Цена курса: 18 500 ₽"
    elif course_name == "SQL: инструменты тестировщика":
        text = "Цена курса: 4 500 ₽"
    elif course_name == "Ручное тестирование мобильных приложений":
        text = "Цена курса: 6 800 ₽"
    elif course_name == "Docker: инструменты тестировщика":
        text = "Цена курса: 4 500 ₽"
    elif course_name == "Тестирование безопасности":
        text = "Цена курса: 9 500 ₽"
    elif course_name == "Bash: Инструменты тестировщика":
        text = "Цена курса: 4 500 ₽"

    await message.answer(text=text, reply_markup=buy_course)


@dp.message_handler(text="Git")
async def get_handler(message: types.Message):
    text = "Нажмите на ссылку ниже и пройдите тест\nhttps://www.learnqa.ru/gittest"
    await message.answer(text=text, reply_markup=test_menu)

@dp.message_handler(text="Bash")
async def get_handler(message: types.Message):
    text = "Нажмите на ссылку ниже и пройдите тест\nhttps://www.learnqa.ru/bash_test"
    await message.answer(text=text, reply_markup=test_menu)

@dp.message_handler(text="SQL")
async def get_handler(message: types.Message):
    text = "Нажмите на ссылку ниже и пройдите тест\nhttps://www.learnqa.ru/sql_test"
    await message.answer(text=text, reply_markup=test_menu)

@dp.message_handler(text="Java")
async def get_handler(message: types.Message):
    text = "Нажмите на ссылку ниже и пройдите тест\nhttps://www.learnqa.ru/java_test"
    await message.answer(text=text, reply_markup=test_menu)

@dp.message_handler(text="Азбука IT")
async def get_handler(message: types.Message):
    text = "Нажмите на ссылку ниже и пройдите тест\nhttps://www.learnqa.ru/abc_test"
    await message.answer(text=text, reply_markup=test_menu)

@dp.message_handler(text="Меню тестов")
async def get_handler(message: types.Message):
    text = "назад в меню тестов"
    await message.answer(text=text, reply_markup=test_test)


@dp.message_handler(text="Купить курс")
async def get_handler(message: types.Message, state: FSMContext):
    text = "Введите имя"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterState.first_name.set()

@dp.message_handler(state=RegisterState.first_name)
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    text = "Введите адрес электронной почты:"
    await message.answer(text=text)
    await RegisterState.email.set()

@dp.message_handler(state=RegisterState.email)
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text, chat_id=message.chat.id)
    text = "Введите данные карты для оплаты:"
    await message.answer(text=text)
    await RegisterState.card_info.set()

@dp.message_handler(state=RegisterState.card_info)
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    text = "Введите номер телефона:"
    await message.answer(text=text, reply_markup=phone_number)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    if db_manager.add_user(data):
        text = "Вы успешно записались на курс ✅"
        await message.answer(text=text, reply_markup=main_menu)

    else:
        text = "Произошла ошибка!"
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.finish()

# UZBEKCHA ------------------------------------------



@dp.message_handler(text="Sinovni o'tkazib yuborish")
async def get_handler(message: types.Message):
    text = "Siz testni o'tkazib yubordingiz"
    await message.answer(text=text, reply_markup=asos_menu)


@dp.message_handler(text="Sinovdan o'ting")
async def get_handler(message: types.Message):
    text = "Quyidagi havolani bosing va testdan o'ting\nhttps://www.learnqa.ru/abc_test"
    await message.answer(text=text, reply_markup=testla_menu)


@dp.message_handler(text="Kurslar")
async def get_handler(message: types.Message):
    text = "Kurs tanlang"
    await message.answer(text=text, reply_markup=kursla_menu)

@dp.message_handler(text="Kontakt ☎️")
async def get_handler(message: types.Message):
    text = """Arseniy Batirov\n
Pochta: arsbatyrov@gmail.com
Telegram: @arsbatyrov\n
Vitaliy Kotov\n
Pochta: vinkotov@gmail.com
Telegram: @vinkotov\n

    """
    await message.answer(text=text, reply_markup=orqa)


@dp.message_handler(text="O'zingni sina")
async def get_handler(message: types.Message):
    text = "Sinovchilar uchun testlar va simulyatorlar"
    await message.answer(text=text, reply_markup=testla_testla)

@dp.message_handler(text="Asosiy menu")
async def get_handler(message: types.Message):
    text = "asosiy menyuga"
    await message.answer(text=text, reply_markup=asos_menu)

@dp.message_handler(text="Ikkinchi bet >")
async def get_handler(message: types.Message):
    text = "Bet 2"
    await message.answer(text=text, reply_markup=kursla_menu2)

@dp.message_handler(text="< Birinchi bet")
async def get_handler(message: types.Message):
    text = "Bet 1"
    await message.answer(text=text, reply_markup=kursla_menu)


@dp.message_handler(text="Sinov: birinchi bosqich")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Sinov: birinchi bosqich")
    text = """Sinov - talab qilinadigan kasb\n\n
Tester - bu dasturlarning sifatini ta'minlash bilan shug'ullanadigan mutaxassis
dasturchilar tomonidan ishlab chiqilgan: veb-saytlar, ish stoli va mobil ilovalar. Buning uchun u qidirmoqda
ilovalardagi muammolar, ularni fayllarga joylashtiradi va ishlab chiquvchilarga xabar beradi. Rahmat
sinovdan o'tgandan so'ng, mahsulot oxirgi foydalanuvchiga etib boradi, mukammal ishlaydi va hamma narsaga ega
raqobat afzalliklari.\n\n
Ushbu kursda biz tester bo'lish uchun zarur bo'lgan asosiy nazariyani yoritamiz va
karerasini IT sohasida boshlasin. Biz sinovchi uchun muhim bo'lgan texnika va vositalarni amalda ko'rsatamiz:\n
Test holatlari va nazorat ro'yxatlari
Test dizayni
Xato kuzatuvchilari va xato hisobotlari
Test tasnifi
Testlarni boshqarish tizimlari
Sinov vositalari: SQL, Git, Bash, Postman, Selenium, Appium va boshqalar\n\n
Biz mashg'ulotlarga ko'p vaqt ajratamiz. Ayniqsa, bu kurs uchun biz
tayyorlangan:\n
xatolarni topish va test holatlarini yaratishni mashq qilishingiz mumkin bo'lgan sinov muhiti.
amalda ko'rish mumkin bo'lgan xato kuzatuvchisi
uning ishlashini ko'rsatish uchun ma'lumotlar bazasini sinovdan o'tkazish\n
Bularning barchasi kurs davomida ham, tugaganidan keyin ham mavjud bo‘ladi.\n
Kurs formati - batafsil tahlil qilingan 20 dan ortiq videolar
mavzu dasturi. Hammasi bo'lib, barcha videolar bir soat davom etadi, ammo ular juda zich
ma'lumotlarga ko'ra, kerakmas malumotsiz, shuning uchun uni o'rganish va tushunish tezroq
hamma narsa ko'proq vaqt talab etadi.\n
Kursda vaqt chegarasi yo'q, shuning uchun siz uni o'z tezligingiz va o'z tezligingizda sotib olishingiz va yakunlashingiz mumkin.
qulay bo'lgan vaqt.\n
Misol darsini ko'ring
https://youtu.be/e0cHqx5cRPo
    """
    await message.answer(text=text, reply_markup=register_qilish)


@dp.message_handler(text="Azbuka IT")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Azbuka IT")
    text = """IT mutaxassisining asosiy ko'nikmalari\n\n
Ajam tester keng dunyoqarashga ega bo'lishi kerak: IT sohasi
U juda tez rivojlanmoqda va barcha yangiliklardan xabardor bo‘lish oson emas. Lekin
Aynan shunday mutaxassislar mehnat bozorida ayniqsa qadrlanadi. Bu vazifa bilan
Bu foydalanishda ancha tajribaga ega bo'lganlar uchun eng oson
kompyuter. Bu sizga eng yangi bilimlarni olish imkonini beradigan asoslarni tushunishdir
ko'p harakat qilmasdan.\n
Ajabo, bunday ma'lumotlar bazasini tuzilgan shaklda olish kifoya
qiyin. IT kurslari ko'pincha ushbu sohada ishlayotganlar uchun mo'ljallangan va
ko'p mahoratga ega. Tajribali murabbiylar qila olmaydi
Tasavvur qiling, ularning talabalari eng oddiy narsalarni bilmasligi mumkin.\n
IT sohasida ishlashni boshlash uchun operatsion tizimlarni tushunish yaxshi bo'lardi
va ularning xususiyatlari, fayl tizimi va konsol bilan ishlay olish, bilish
tarmoq ishining tuzilishi va tamoyillari, mijoz-server tizimi nima ekanligini tushunish
ilovalar arxitekturasi, shuningdek, boshqa ko'plab shunga o'xshashlarga ega
asosiy mavzular.\n
Azbuka IT kursi turli xildagi asosiy fikrlarni ochib beradi
axborot texnologiyalari dunyosining sohalari. Siz bilan bir xil bazani olasiz
siz deyarli har qanday IT kurslarini muammosiz va hattoki olishingiz mumkin
Junior sifatida ishlashni boshlang. Biz dasturni iloji boricha tuzdik
axborot texnologiyalari bilan tanish bo'lmaganlar uchun ochiq
har kuni.\n
Misol darsini ko'ring
https://youtu.be/zLAieW59fgs
    """
    await message.answer(text=text, reply_markup=register_qilish)



@dp.message_handler(text="Mobil ilovalar avtomatlantirish")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Mobil ilovalar avtomatlantirish")
    text = """Mobil avtomatlashtirish qobiliyatlari\n\n
Mobile Application Automator eng ko'p maosh oladiganlardan biridir
IT bozoridagi kasblar. Biroq, kadrlar etishmasligi tufayli ko'plab kompaniyalar duch kelmoqda
ushbu sohada mutaxassislarni topish muammosi. Shunday qilib, agar siz bo'lishni istasangiz
Talab qilingan tester, siz avtomatlashtirish ko'nikmalarini egallashingiz kerak.\n
Bizning kursimiz mustaqil ravishda to'liq o'rnatish uchun barcha kerakli bilimlarni beradi
noldan mobil ilovalarni sinovdan o'tkazish uchun avtomatlashtirish to'plami. Biz shunchaki qanday qilishni o'rgatmaymiz
testlarni yozing yoki sinov muhitini o'rnating, chunki bu ishda etarli emas. Biz
biz boshidanoq loyihada test avtomatizatsiyasini yaratishni o'rgatamiz
mahsulotni ishlab chiqish va sinovdan o'tkazishning barcha bosqichlarida uni ishlab chiqish va qo'llab-quvvatlash.\n
Bizning darslarimizda siz:\n
Ikkala platforma - iOS va Android bilan ishlash ustasi;
Misol sifatida mobil veb-ilovasidan foydalangan holda veb-avtomatlashtirishni o'rganing;
Sizning ishingizga mos keladigan to'g'ri vositalarni o'rganing;
Windows, MacOS yoki Linuxda noldan avtomatlashtirish muhitini o'rnating;
Siz Jenkinsni qanday o'rnatishni va CI tizimida testlarni o'tkazishni o'rganasiz;
O'zingizning test tizimingizni ishlab chiqing;
Allure-ga qulay va tushunarli test hisobotlarini qo'shing;
Github-da bo'ladigan va o'zingiz qilishingiz mumkin bo'lgan katta avtomatlashtirish loyihasini yarating
Uni rezyumeingizga qo'shishingiz mumkin.\n
Kursni tugatganingizdan so'ng siz yakuniy loyihani rezyumeingizga qo'shishingiz mumkin, shuningdek
ko‘plab bitiruvchilarimiz kabi olingan bilimlarni amalda qo‘llash.
    """
    await message.answer(text=text, reply_markup=register_qilish)

@dp.message_handler(text="SQL: Tester asboblari")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="SQL: Tester asboblari")
    text = """SQL - Tester vositasi\n\n
Siz ish topmoqchisiz, lekin har ikkinchi suhbatda ular so'rashadi
SQL so'rovini yozingmi? Yoki ma'lumotlar bazasidan test ma'lumotlarini olishingiz kerakmi?
Yoki veb-shaklingizda xatolik bormi va siz ma'lumotlar bazasidagi qiymatlarni tekshiryapsizmi?\n
Bularning barchasi uchun - va yana ko'p narsalar - u bilan ishlashni o'zlashtirish etarli bo'ladi
relyatsion ma'lumotlar bazalari va SQL. SQL yordamida siz yaratishingiz mumkin va
ma'lumotlar bazalarini o'chirish, qiymatlarni kiritish va eng muhimi tester uchun -
kerakli shaklda ma'lumotlarni olish.\n
Kursga keling va atigi 2 hafta ichida quyidagilarni bilib olasiz:\n
Ma'lumotlar bazasidan ma'lumotlarni qabul qilish va saralash;
Filtrlarni o'rnatish;
Hisob-kitoblarni amalga oshirish;
Ma'lumotlar va jadvallarni guruhlash;
Quyi so'rovlar va birlashtirilgan so'rovlar bilan ishlash;
Ma'lumotlar bazasiga ma'lumotlarni qo'shish va o'zgartirish;
Jadvallar va ma'lumotlar bazalarini yaratish.\n
Misol darsini ko'ring
https://youtu.be/PTAkqURmI0s
    """
    await message.answer(text=text, reply_markup=register_qilish)

@dp.message_handler(text="Mobil ilovalarni qo'lda sinovdan o'tkazish")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Mobil ilovalarni qo'lda sinovdan o'tkazish")
    text = """Mobil test - bu yangi sanoat\n\n
Siz tez-tez mobil telefoningizdan foydalanasizmi va mobil telefonga o'tishni xohlaysizmi?
sinovchilar? Yoki siz allaqachon veb-testda ishlayapsizmi, lekin biror narsani xohlaysizmi?
yangi? Yoki siz allaqachon mobil telefonlarni sinab ko'ryapsiz, lekin o'zingiznikini yangilashni xohlaysiz
mahorat?\n
Mobil telefonlarning mashhurligi ortib bormoqda: har yili 5000 dan ortiq dona chiqariladi
yangi modellar va mobil trafik umumiy ulushning 58% ni tashkil qiladi
Internetdan foydalanish. Tabiiyki, ko'proq ilovalar mavjud va
Bu mobil testerlar uchun so'rov borligini anglatadi.\n
Ushbu kursda biz test nazariyasini ko'rib chiqmaymiz - in
Mobil testda u oddiy testdan farq qilmaydi. Biz
Keling, sohaga oid fikrlarga e'tibor qarataylik:\n
Mobil testning xususiyatlari
Emulyatorlar va simulyatorlar
Android va iOS uchun IDE va asboblar
Mobil qurilmalar
Mobil ilovalar va ularning turlari\n
Misol darsini ko'ring
https://youtu.be/sPPWOZxEl9w
    """
    await message.answer(text=text, reply_markup=register_qilish)

@dp.message_handler(text="Docker: sinov vositalari")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Docker: sinov vositalari")
    text = """Docker - tester vositasi\n\n
Siz ish topmoqchisiz, lekin ular bilan ishlash qobiliyati talab qilinadi
konteynerlar? Yoki siz Docker-da Selenium-dagi testlarni qanday bajarishni o'rganishni xohlaysiz?
Yoki ishingiz uchun kerakli dasturni tushunmasdan bemalol ishlatmoqchimisiz
uning o'rnatilishi bilan?\n
Bularning barchasi (va yana ko'p narsalar) uchun qanday ishlashni o'rganish kifoya qiladi
Docker konteynerlashtirish vositasi. Uning yordami bilan siz yaratishingiz mumkin
kerakli dasturiy ta'minot bilan konteynerlarni ishga tushirish va tarqatish, sozlash
testlar va CI o'rtasidagi o'zaro ta'sir, turli til versiyalarini qo'shing
dasturlaringizni sinab ko'rish uchun dasturlash, mashinangizni saqlang
tozalang va sinovchi duch keladigan o'nlab boshqa vazifalarni bajaring
har kuni.\n
Kursga keling va atigi 2 hafta ichida quyidagilarni bilib olasiz:\n
Docker-ni har qanday zamonaviy operatsion tizimda sozlang
Konteynerlarni yaratish, ulash va o'chirish
O'zingizning rasmlaringiz va hajmlaringizni yarating
Bog'lanish va hajmlar orqali dastur o'zaro ta'sirini sozlang
Konteynerlarda testlarni va har qanday dasturlarni ishga tushiring
Konteynerlarni tarmoqqa ulang\n
Misol darsini ko'ring
https://youtu.be/GsnXl87lYzg
    """
    await message.answer(text=text, reply_markup=register_qilish)


@dp.message_handler(text="Xavfsizlik sinovi")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(course="Xavfsizlik sinovi")
    text= """Xavfsizlik sinovi\n\n
Hech qachon xavfsizlik testini sinab ko'rmadingizmi? Siz buni qiyin deb o'ylaysiz
uzoq va faqat elita uchunmi? Sinash uchun g'oyalar tugaydi
ilovalar?\n
Ko'rinib turibdiki, nihoyat xavfsizlik testlarini o'zlashtirish vaqti keldi. Bu
Bu ko'rinadigan darajada qiyin emas, shunchaki asosiy narsalarni tushunish kifoya
dasturning ishlash tamoyillari va mashhur qidiruv usullaridan foydalanish
zaifliklar. Ularni mashq qiling va siz darhol yaxshilanishingiz mumkin.
loyihangizda sinov.\n
Kursga keling va atigi 4 hafta ichida siz quyidagilarni bilib olasiz:\n
Shakllardagi zaifliklarni toping
HTML, JS va XSS inyeksiyalari bilan ishlash
Turli so'rovlarda SQL in'ektsiyalarini qidiring
Orqa eshiklardan foydalaning va qobiqni o'g'irlang
Ijtimoiy muhandislikdan foydalaning va himoya qiling
Avtomatik skanerlash uchun skanerlarni tanlang\n
Misol darsini ko'ring
https://youtu.be/6cumnXMijbQ
    """
    await message.answer(text=text, reply_markup=register_qilish)

@dp.message_handler(text="Bash: Tester asboblari")
async def get_nadler(message: types.Message, state: FSMContext):
    await state.update_data(course="Bash: Tester asboblari")
    text = """Bash - Tester vositasi\n\n
Ish topmoqchimisiz, lekin ular Linuxni bilishni talab qiladimi? Yoki ehtimol siz
Har kuni katta hajmdagi fayllar bilan ishlashingiz kerakmi? Yoki xohlaysizmi
jurnallar qurilmalardan olib tashlansinmi? Qizil libosdagi ayollarni ko'rishni o'rganing
kod satrlari?\n
Bularning barchasi uchun (va yana ko'p narsalar), u bilan ishlashni o'zlashtirish kifoya qiladi
Bash buyruq qobig'i. Uning yordami bilan siz yaratishingiz, qidirishingiz va o'zgartirishingiz mumkin
fayllar, jarayonlarni kuzatish, masofaviy mashinalarga kirish va boshqalar
sinovchi har kuni duch keladigan yuzlab vazifalar.\n
Kursga keling va atigi 2 hafta ichida quyidagilarni bilib olasiz:\n
Konsol orqali fayl va papkalar bilan ishlash;
Fayllar, kataloglar va jarayonlar daraxtlari ichidan qidirish;
Tizimda ishlaydigan dasturlarni tanlash va qayta ishlash;
Har qanday ma'lumotni fayllarga yozing;
Qulay va ma'lumot beruvchi konsolni o'rnating.\n
Misol darsini ko'ring
https://youtu.be/JQXM4ArzyU4
    """
    await message.answer(text=text, reply_markup=register_qilish)


@dp.message_handler(text="Yozilish!")
async def products_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(course="Yozilish!")
    course_name = data.get("course")
    text = ""
    if course_name == "Sinov: birinchi bosqich":
        text = "Kurs narxi: 2 000 ₽"
    elif course_name == "Azbuka IT":
        text = "Kurs narxi: 3 500 ₽"
    elif course_name == "Mobil ilovalar avtomatlantirish":
        text = "Kurs narxi: 18 500 ₽"
    elif course_name == "SQL: Tester asboblari":
        text = "Kurs narxi: 4 500 ₽"
    elif course_name == "Mobil ilovalarni qo'lda sinovdan o'tkazish":
        text = "Kurs narxi: 6 800 ₽"
    elif course_name == "Docker: sinov vositalari":
        text = "Kurs narxi: 4 500 ₽"
    elif course_name == "Xavfsizlik sinovi":
        text = "Kurs narxi: 9 500 ₽"
    elif course_name == "Bash: Tester asboblari":
        text = "Kurs narxi: 4 500 ₽"

    await message.answer(text=text, reply_markup=sotib_course)


@dp.message_handler(text="Git.")
async def get_handler(message: types.Message):
    text = "Quyidagi havolani bosing va testdan o'ting\nhttps://www.learnqa.ru/gittest"
    await message.answer(text=text, reply_markup=testla_menu)

@dp.message_handler(text="Bash.")
async def get_handler(message: types.Message):
    text = "Quyidagi havolani bosing va testdan o'ting\nhttps://www.learnqa.ru/bash_test"
    await message.answer(text=text, reply_markup=testla_menu)

@dp.message_handler(text="SQL.")
async def get_handler(message: types.Message):
    text = "Quyidagi havolani bosing va testdan o'ting\nhttps://www.learnqa.ru/sql_test"
    await message.answer(text=text, reply_markup=testla_menu)

@dp.message_handler(text="Java.")
async def get_handler(message: types.Message):
    text = "Quyidagi havolani bosing va testdan o'ting\nhttps://www.learnqa.ru/java_test"
    await message.answer(text=text, reply_markup=testla_menu)

@dp.message_handler(text="Azbuka IT")
async def get_handler(message: types.Message):
    text = "Quyidagi havolani bosing va testdan o'ting\nhttps://www.learnqa.ru/abc_test"
    await message.answer(text=text, reply_markup=testla_menu)

@dp.message_handler(text="Testlar menusi")
async def get_handler(message: types.Message):
    text = "sinov menyusiga qaytish"
    await message.answer(text=text, reply_markup=testla_testla)


@dp.message_handler(text="Kurs sotib olish")
async def get_handler(message: types.Message, state: FSMContext):
    text = "Ismingizni kiriting"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterStateUz.full_name.set()

@dp.message_handler(state=RegisterStateUz.full_name)
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "E-mail manzilingizni kiriting:"
    await message.answer(text=text)
    await RegisterStateUz.gmail.set()

@dp.message_handler(state=RegisterStateUz.gmail)
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(gmail=message.text, chat_id=message.chat.id)
    text = "To'lov uchun karta ma'lumotlarini kiriting:"
    await message.answer(text=text)
    await RegisterStateUz.karta_info.set()

@dp.message_handler(state=RegisterStateUz.karta_info)
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(karta_info=message.text)
    text = "Telefon raqamingizni kiriting:"
    await message.answer(text=text, reply_markup=tel_number)
    await RegisterStateUz.tel_number.set()


@dp.message_handler(state=RegisterStateUz.tel_number, content_types=types.ContentType.CONTACT)
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(tel_number=message.contact.phone_number)
    data = await state.get_data()
    if db_manager.add_user(data):
        text = "Siz kursga muvaffaqiyatli ro'yxatdan o'tdingiz ✅"
        await message.answer(text=text, reply_markup=asos_menu)

    else:
        text = "Xato ro'y berdi!"
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(text="Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(inst="Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti")
    text = """Университет ИТМО\n\n
Rossiya federal davlat ta'lim muassasasi
oliy va oliy o'quv yurtidan keyingi ta'lim, 2009 yildan - milliy
tadqiqot universiteti (NRU).Universitetning ustuvor yo'nalishlari axborotdir
texnologiya, sun'iy intellekt, fotonika, robototexnika, kvant aloqasi,
tarjima tibbiyoti, hayot fanlari, san'at va fan, ilmiy aloqa.
ITMO ning sport dasturlash jamoasi dunyoda yagona yetti karra chempion hisoblanadi
eng yirik xalqaro talabalar olimpiadasi ICPC.Universitet Rossiyaning eng yaxshi 5 universitetlari qatoriga kiradi
byudjetni qabul qilish sifati bo'yicha, IT bitiruvchilari ish haqi bo'yicha yetakchilardan biri.
Ta'lim muassasasi o'z tarixini 1900 yil 26 martda, Tsarevich kasb-hunar maktabi tashkil etilgan paytdan boshlab o'z ichiga oladi.
Nikolay, mexanik-optik va soat bo'limi ochildi. 1917 yilgi inqilobdan keyin
kafedra mustaqil o'quv muassasasi - Petrograd texnik maktabiga ajratildi
mexanik-optik va soat ishlab chiqarishda o'qidi va 1920 yilda Petrograd texnikumiga aylantirildi.
nozik mexanika va optika (keyinchalik - Leningradskiy); 1920-yillarda texnikum edi
zamonaviy asosiy bino Demidov ko'chasida (Grivtsova ko'chasi) bino taqdim etildi
Sablinskaya ko'chasida (Kronverkskiy prospektiga qaragan) 1970-yillarda qurilgan.
    """
    await message.answer(text=text, reply_markup=uzb_adress_inst)


@dp.message_handler(text="MISIS universiteti")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(inst="MISIS universiteti")
    text = """
Universitet yangi narsalarni yaratish, amalga oshirish va qo'llashga ixtisoslashgan
texnologiyalar va materiallar. Kompyuter fanlari instituti IT-mutaxassislarini tamomlaydi
sun'iy intellekt, katta ma'lumotlar va kompyuter fanlari bo'yicha tadqiqotlar bo'yicha profilga ega,
dasturlar va ilovalarni ishlab chiqish. Dasturchilarni qiziqtirgan fakultetlar: informatika
va Kompyuter fanlari, axborot tizimlari va texnologiyalari.\n
Milliy tadqiqot texnologik universiteti MISiS - Rossiya texnik
universitet.. NUST MISIS o'z ichiga oladi 8 institutlari va 6 filiallari - Rossiyada to'rt va
ikkitasi chet elda. Universitetda 22 mingga yaqin talaba bor, talabalarning 25 foizi fuqarolardir
dunyoning 85 mamlakatidan. Materialshunoslik va metallurgiya sohasidagi etakchi Rossiya universitetlaridan biri
va konchilik. Qabul qilish sifati bo'yicha milliy monitoring reytingida, ya'ni
HSE, 2021 yilda 13-o'rinni egalladi (Yagona davlat imtihonining o'rtacha balli 88,8 ga ko'tarildi), besh yil ketma-ket reytingda.
mamlakatning eng yaxshi texnik universitetlari orasida to'rtinchi o'rin. Ta'lim modelining markazida
universitet - ta'lim va fan integratsiyasi. Universitet talabalar uchun fundamental ta'limni birlashtiradi
o'rganishga loyiha va amaliyotga yo'naltirilgan yondashuv bilan, hamkorlikda faol ishtirok etadi
NUST MISIS akademik va biznes hamkorlari.

Universitet Rossiya va dunyoning 1600 dan ortiq yirik kompaniyalari bilan hamkorlik qiladi.
Keng qamrovli professional navigatsiya dasturi tufayli kirganlarning Yagona davlat imtihonining o'rtacha balli
universitet 2012 yilda 67,3 dan 2021 yilda 88,8 gacha o'sdi.
    """
    await message.answer(text=text, reply_markup=uzb_adress_inst)


@dp.message_handler(text="Buyuk Pyotr Sankt-Peterburg politexnika universiteti")
async def get_handler(message: types.Message, state: FSMContext):
    await state.update_data(inst="Buyuk Pyotr Sankt-Peterburg politexnika universiteti")
    text = """
Buyuk Pyotr Sankt-Peterburg politexnika universiteti eng yirik hisoblanadi
tarixan kuchli ilmiy maktablarga ega mamlakatdagi texnik universitet,
ilmiy, ta'lim va sohalarda inkor etib bo'lmaydigan natijalar va yutuqlarga ega
innovatsion faoliyat. Asosiy global rivojlanish tendentsiyalari asosida
tadqiqot, ishlanmalar, texnologiya va ta'lim sohalariga 2030 yilgacha kirishni maqsad qilgan
dunyoning eng yaxshi yuzta universitetlari qatoriga kirib, jahon taʼlimi yetakchilari bilan bir qatorda.
Bu yil Buyuk Pyotr Sankt-Peterburg politexnika universiteti qabul konsepsiyasini yangiladi. Qabul qilish konsepsiyasi 2022/2023 -
Biz nima qilishni bilamiz. Shunday qilib, Politexnika Universiteti o'z abituriyentlariga biz ekanligimizni ko'rsatadi
axborot oqimida va biz muvaffaqiyatga erishish, maqsadga erishish uchun nima qilish kerakligini bilamiz,
trendda bo'lish uchun talabalarga rahbarlik qilishga tayyor. Sankt-Peterburg politexnika
Buyuk Pyotr universiteti tarixan tashkil etilgan mamlakatdagi eng yirik texnik universitetdir
ilm-fan sohasida inkor etib bo'lmaydigan natijalar va yutuqlarga ega bo'lgan eng kuchli ilmiy maktablar,
ta'lim va innovatsion faoliyat. Asosiy global tendentsiyalar asosida
tadqiqot, ishlanma, texnologiya va ta'limni rivojlantirish, erishishni maqsad qiladi
jahon ta'lim yetakchilari bilan teng bo'lib, dunyodagi eng yaxshi yuzta universitetlar qatoriga kirish.
Bu yil Buyuk Pyotr Sankt-Peterburg politexnika universiteti qabul konsepsiyasini yangiladi. Qabul qilish konsepsiyasi 2022/2023 -
Biz nima qilishni bilamiz. Shunday qilib, Politexnika Universiteti o'z abituriyentlariga biz ekanligimizni ko'rsatadi
axborot oqimida va biz muvaffaqiyatga erishish, maqsadga erishish uchun nima qilish kerakligini bilamiz,
trendda bo'lish uchun talabalarga rahbarlik qilishga tayyor.
    """
    await message.answer(text=text, reply_markup=uzb_adress_inst)


@dp.message_handler(text="Sinovdan o'tish")
async def get_handler(message: types.Message):
    text = "Quyidagi havolani bosing va testdan o'ting\nhttps://www.learnqa.ru/abc_test\n\n\nShuningdek, quyida joylashgan tugmani bosish orqali institutlar roʻyxatini koʻrishni tavsiya qilamiz"
    await message.answer(text=text, reply_markup=bosh_test)


@dp.message_handler(text="Institutlar")
async def get_handler(message: types.Message):
    text = "Sizga uchta institutni tavsiya qilamiz"
    await message.answer(text=text, reply_markup=in_uzb_list)



@dp.message_handler(text="Rasm")
async def plus_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # await state.update_data(inst="Photo")
    product_name = data.get("inst")
    photo = ""
    text = ""
    if product_name == "Университет ИТМО":
        photo = "https://upload.wikimedia.org/wikipedia/commons/c/cc/ITMO_University%27s_main_building%2C_August_2016.jpg"
        text = "Университет ИТМО"

    elif product_name == "Университет МИСИС":
        photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Korpus_b.jpg/1200px-Korpus_b.jpg"
        text = "Университет МИСИС"

    elif product_name == "Санкт-Петербургский политехнический университет Петра Великого":
        photo = "https://alfakom.uz/images/img/partners/spbstu_1.jpg"
        text = "Санкт-Петербургский политехнический университет Петра Великого"

    elif product_name == "Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti":
        photo = "https://upload.wikimedia.org/wikipedia/commons/c/cc/ITMO_University%27s_main_building%2C_August_2016.jpg"
        text = "Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti"

    elif product_name == "MISIS universiteti":
        photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Korpus_b.jpg/1200px-Korpus_b.jpg"
        text = "MISIS universiteti"

    elif product_name == "Buyuk Pyotr Sankt-Peterburg politexnika universiteti":
        photo = "https://alfakom.uz/images/img/partners/spbstu_1.jpg"
        text = "Buyuk Pyotr Sankt-Peterburg politexnika universiteti"

    await message.answer_photo(photo=photo, caption=text)


@dp.message_handler(text="Aloqa uchun kontaktlar")
async def plus_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # await state.update_data(inst="Photo")
    product_name = data.get("inst")
    photo = ""
    text = ""
    if product_name == "Университет ИТМО":
        text = """
КАНЦЕЛЯРИЯ
+7 (812) 480-00-00
Факс: +7 (812) 232-23-07
od@itmo.ru
ПРИЁМНАЯ КОМИССИЯ
+7 (812) 480-04-80
abit@itmo.ru
ЦЕНТР РЕКРУТИНГА
job@itmo.ru
СТУДЕНЧЕСКИЙ ОФИС
+7 (812) 607-04-74
so@itmo.ru
ОФИС ПОДДЕРЖКИ СОТРУДНИКОВ
+7 (812) 607-02-50
faculty@itmo.ru
ПРЕСС-СЛУЖБА
+7 (900) 630-00-10
pressa@itmo.ru
        """
    elif product_name == "Университет МИСИС":
        text = """
Юридический и фактический адрес: 119049, Москва, Ленинский пр-кт, д. 4, стр. 1.
Телефон: +7 495 955-00-32
Факс: +7 499 236-21-05
График работы административных подразделений: пн.-пт. 9:00-18:00.
График обучения студентов: пн.-пт. с 9:00-21:00, сб. 9:00-18:00.
        """
    elif product_name == "Санкт-Петербургский политехнический университет Петра Великого":
        text = """
+7 (812) 775-05-30
- для звонков из Санкт-Петербурга
 8 (800) 707-18-99
- для звонков из любого региона РФ (звонок бесплатный)
        """
    elif product_name == "Sankt-Peterburg davlat axborot texnologiyalari, mexanika va optika universiteti":
        text = """
IDORA
+7 (812) 480-00-00
Faks: +7 (812) 232-23-07
od@itmo.ru
TANLOV QO'MITI
+7 (812) 480-04-80
abit@itmo.ru
ISHLASH MARKAZI
job@itmo.ru
Talabalar idorasi
+7 (812) 607-04-74
so@itmo.ru
XODIMLARNI QO'LLAB-QUVVAT BO'LISHI
+7 (812) 607-02-50
faculty@itmo.ru
MATBUOT XIZMATI
+7 (900) 630-00-10
pressa@itmo.ru
        """
    elif product_name == "MISIS universiteti":
        text = """
Yuridik va haqiqiy manzil: 119049, Moskva, Leninskiy prospekti, 4, 1-bino.
Telefon: +7 495 955-00-32
Faks: +7 499 236-21-05
Ma'muriy bo'limlarning ish vaqti: Dus.-Jum. 9:00-18:00.
Talabalar dars jadvali: dushanba-juma. 9:00 dan 21:00 gacha, shanba. 9:00-18:00.
        """
    elif product_name == "Buyuk Pyotr Sankt-Peterburg politexnika universiteti":
        text = """
+7 (812) 775-05-30
- Sankt-Peterburgdan qo'ng'iroqlar uchun
 8 (800) 707-18-99
- Rossiya Federatsiyasining istalgan mintaqasidan qo'ng'iroqlar uchun (qo'ng'iroq bepul)
        """

    await message.answer(text=text)





if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)