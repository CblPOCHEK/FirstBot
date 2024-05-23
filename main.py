from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboard import get_keyboard_1, get_keyboard_2
from aiogram. types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot (token= TELEGRAM_TOKEN)
dp = Dispatcher (bot)

keyboard_inline = InlineKeyboardMarkup(row_width= 1)
but_inline = InlineKeyboardButton (text = 'Посмотреть', url= 'https://www.purina.ru/cats/breed-Library')
but_inline2 = InlineKeyboardButton( text = 'Посмотреть', url= 'https://www.purina.ru/cats/breed-library')
keyboard_inline.add (but_inline, but_inline2)

async def set_commands (bot: Bot) :
    commands = [
        types.BotCommand (command= '/start', description= 'Команда для того, чтобы запустить бота'),
        types.BotCommand (command='/help', description='Команда для того, чтобы узнать с чем может помочь наш бот ')
    ]

    await bot. set_my_commands (commands)

@dp.message_handler (commands= 'start')
async def start(message: types.Message) :
    await message.answer('Привет, я твой первый ЭХО бот!',reply_markup=get_keyboard_1())

@dp.message_handler (lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message) :
    await bot.send_photo(message.chat.id, photo= 'https://resizer.mail.ru/p/2f81f3fd-0006-57b5-9d32-2d8bf7c7ec0e/AQAOx65FyDa9iDIYPFhSnYHmdA4pH465zkyC-J8e7nVPBTNfQfD23VpakzWwMDql0zY5DbsrLZTBVZzFKie8w-69bLw.jpg',caption='Вот тебе кот', reply_markup=keyboard_inline)

@dp.message_handler (lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message) :
    await message.answer(text = 'Тут ты можешь попросить бота отправить фото собаки', reply_markup= get_keyboard_2())

@dp.message_handler (lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message) :
    await bot.send_photo(message.chat.id, photo= 'https://s0.rbk.ru/v6_top_pics/media/img/3/28/346820872290283.webp',caption='Вот тебе пес')

@dp.message_handler (lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_4_click(message: types.Message) :
    await message.answer(text = 'Тут ты можешь попросить бота отправить фото кота', reply_markup= get_keyboard_1())

@dp.message_handler (commands= 'help')
async def start(message: types.Message) :
    await message.answer('Я могу помочь тебе с....')

@dp.message_handler ()
async def echo(message: types.Message) :
    await message.answer(message.text)

async def on_startup (dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor. start_polling(dp, skip_updates= True)