import asyncio
import logging
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token

connection = sqlite3.connect("orders.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
        id INT, 
        user_name VARCHAR(100),
        articul_phone TEXT
);
""")


bot = Bot(token=token)
dp = Dispatcher()

start_buttons_icg = [
    [KeyboardButton(text="О НАС"), KeyboardButton(text="Товары")],
    [KeyboardButton(text="Заказать"), KeyboardButton(text="Контакты")],
]
start_keyboard_inboard = ReplyKeyboardMarkup(keyboard=start_buttons_icg, resize_keyboard=True)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=start_keyboard_inboard)

@dp.message(F.text == "О НАС")
async def napravlenia(message: types.Message):
    await message.answer("Tehno-shop - Здравствуйте, дорогие друзья! Меня зовут Ольга Лебедь, я основатель магазина Техника Здоровья, рада приветствовать вас на моем сайте! Являюсь Членом Международной Ассоциации нутрициологов и коучей по здоровью. Я очень хочу, чтобы у каждого из вас было легкое решение для приготовления здоровой еды в условиях мегаполиса.", reply_markup=start_keyboard_inboard)

@dp.message(F.text == "Товары")
async def napravlenia(message: types.Message):
    await message.answer_photo("https://static.daru-dar.org/s-w250/00.dd/03/f1/7f/f17f5ce24383bf2df55e5490386d940be4d3ce0a.jpg", caption="Сгоревшая материнская плата: \n Цена: 1000 \n Артикул товара: 1 \n")
    await message.answer_photo("https://optim.tildacdn.com/tild6132-3762-4832-b262-333162663965/-/resize/744x/-/format/webp/image.png",caption="Расплаленная материнская плата: \n Цена: 2000 \n Артикул товара: 3")
    await message.answer_photo("https://avatars.mds.yandex.net/get-ydo/1449941/2a0000016d9eeaa758ff4b0d1c42d896570f/diploma", caption="Пыльная материнская плата: \n Цена: 2000 \n Артикул товара: 2")
    await message.answer_photo("https://cdn.mos.cms.futurecdn.net/G6gp68NaixQCHMYaJGRuEj-1200-80.jpg", caption="Процессор AMD RYZEN 9 9950x: \n Цена: 120000 \n Артикул товара: 4")
        
        
        
@dp.message(F.text == "Заказать")
async def napravlenia(message: types.Message):
    await message.answer("Введите Артикул товара и номер телефона(+996...)")

@dp.message() 
async def start(message: types.Message):
    cursor.execute("INSERT INTO orders (id, user_name, articul_phone) VALUES (?, ?, ?)", (message.from_user.id, message.from_user.username, message.text))
    connection.commit()
    await message.answer(f"Заказ оформлен на имя {message.from_user.username}")



@dp.message(F.text == "Контакты")
async def napravlenia(message: types.Message):
    await message.answer("+996 504 07 77 00, \n +996 501 01 61 99 \n tg: @bnshiro \n inst: @bnshiro")

async def main():
    logging.basicConfig(level="INFO")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
