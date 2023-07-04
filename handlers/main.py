from aiogram import executor
import logging
from hw_1.config import dp
from hw_1.handlers import client, callback, extra, admin, fsm_mentor

client.register_client_callback(dp)
callback.register_callback(dp)
fsm_mentor.register_hanlers_fsm_anketa(dp)
admin.register_admin(dp)
extra.register_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

