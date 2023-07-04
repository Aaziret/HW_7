from aiogram import types, Dispatcher


async def pin_message_handle(message: types.Message):
    if message.text.startswith('!pin') and message.reply_to_message:
        await message.pin()


def register_admin(dp: Dispatcher):
    dp.register_message_handler(pin_message_handle, commands=['pin'], commands_prefix=['!'])
