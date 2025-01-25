import os, asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: types.Message):
    photo = FSInputFile('qr.jpg')
    await message.answer_photo(photo, caption='Приветствую! Для перехода в основной канал произведите оплату по qr коду, после оплаты напишите админу @killativ201, просьба прислать чек об оплате!!! (Добавление в канал произведётся в течении 24 часов😁)')

async def on_shutdown():
    print('bot disconnected')

async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    
asyncio.run(main())