from aiogram2 import Bot, Dispatcher, executor, types
from aiogram2.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import babel

api = "7542992530:AAGHsS_u-5wgRFFxJdERHoMVzLsS6uCoS1k"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)