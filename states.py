from aiogram.dispatcher.filters.state import StatesGroup, State

class RegisterState(StatesGroup):
    first_name = State()
    phone_number = State()
    email = State()
    card_info = State()
    chat_id = State()

class RegisterStateUz(StatesGroup):
    full_name = State()
    tel_number = State()
    gmail = State()
    karta_info = State()
    chat_id = State()