from aiogram.dispatcher.filters.state import StatesGroup, State

class AdressState(StatesGroup):
    rayon = State()
    street = State()
    house = State()
