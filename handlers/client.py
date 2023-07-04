from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from hw_1.config import bot
from hw_1.handlers.hw7 import get


async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "сколько хокаге в деревне скрытого листа"
    answers = [
        "7",
        "8",
        "2",
        "4",
        "3",
        "5",
    ]

    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="ты не смотрел наруто?",
        open_period=10,
        reply_markup=markup
    )


async def start_command_1(message: types.Message):
    photo = open('media/detail_dad9dde83048e2a200dfecf4355dbc5e.jpg', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


async def get_find(message: types.Message):
    await message.answer(get(message))


def register_client_callback(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(start_command_1, commands=['mems'])
    dp.register_message_handler(get_find, commands=['get'])
