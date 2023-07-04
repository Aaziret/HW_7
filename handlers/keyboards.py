from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,

)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
mems_button = KeyboardButton("/mems")


start_markup.add(
    start_button,
    quiz_button,
    mems_button
)
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
cancel_button = KeyboardButton("Отмена")
cancel_markup.add(cancel_button)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("да"),
    KeyboardButton("заново"),
    cancel_button
)

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("Женщина"),
    KeyboardButton("Мужчина"),
    KeyboardButton("Незнаю"),
    cancel_button
)
