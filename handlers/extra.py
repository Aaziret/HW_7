from hw_1.config import dp, bot, ADMIN
import random
from aiogram import Dispatcher


async def hendler_echo(message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    elif message.text.startswith('game') and message.from_user.id in ADMIN:
        emojis = ['🎯', '🎳', '🎰', '🎲', '⚽️', '🏀']
        dice = random.choice(emojis)
        await bot.send_dice(message.chat.id, emoji=dice)


def register_extra(dp: Dispatcher):
    dp.register_message_handler(hendler_echo)
