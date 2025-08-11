import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command


TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    raise ValueError("Переменная окружения TOKEN не установлена")


bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, filename = "mylog.log", format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")


@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Я бот, который переводит ФИО с кириллицы на латиницу. Напиши, пожалуйста, своё полное ФИО.'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


@dp.message()
async def name_trans(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: ответ на запрос: {text}')
    await message.answer(text=name_transformation(text))


def name_transformation(name):
    d= {'А':'A', 'Б':'B', 'В':'V', 'Г':'G',	'Д':'D', 'Е':'E', 'Ё':'E', 'Ж':'ZH', 'З':'Z',
        'И':'I', 'Й':'I', 'К':'K', 'Л':'L',	'М':'M', 'Н':'N', 'О':'O', 'П':'P',	'Р':'R', 
        'С':'S', 'Т':'T', 'У':'U', 'Ф':'F',	'Х':'KH', 'Ц':'TS',	'Ч':'CH', 'Ш':'SH',	'Щ':'SHCH',	
        'Ы':'Y', 'Ъ':'IE', 'Э':'E',	'Ю':'IU', 'Я':'IA', 'Ь':'', ' ':' ', '-':'-', "'":"'"}
    latin_name = ''
    for i in name.upper():
        if i in d:
            latin_name += d[i]
        else:
            return 'Похоже в ФИО есть недопустимые знаки или латинские буквы. Пожалуйста, укажи корректное имя киррилицей.'
    return latin_name


if __name__ == '__main__':  
    dp.run_polling(bot)

 