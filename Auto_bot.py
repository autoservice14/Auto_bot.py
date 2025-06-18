from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = '7790254852:AAEqUBEauTTxcQzFzGOAtb_e1LfPv9aLDsQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ustalar")],
        [KeyboardButton(text="Lokatsiya")]
    ],
    resize_keyboard=True
)

# Подменю Ustalar
ustalar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Hodavoy")],
        [KeyboardButton(text="Elektrik")],
        [KeyboardButton(text="Gazovik")],
        [KeyboardButton(text="Avto zapchast")],
        [KeyboardButton(text="Himchistka")],
        [KeyboardButton(text="Palirovka")],
        [KeyboardButton(text="⬅️ Ortga")]
    ],
    resize_keyboard=True
)

# Локация сервиса
latitude = 41.3621521
longitude = 69.2296312

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Kerakli bo‘limni tanlang:", reply_markup=main_menu)

@dp.message(lambda message: message.text == "Ustalar")
async def show_ustalar_menu(message: types.Message):
    await message.answer("Ustalar bo‘limidan birini tanlang:", reply_markup=ustalar_menu)

@dp.message(lambda message: message.text == "Lokatsiya")
async def send_location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id, latitude=41.3621521, longitude=69.2296312)

# Hodavoy
@dp.message(lambda message: message.text == "Hodavoy")
async def hodavoy_info(message: types.Message):
    await message.answer("📞  977020105  Dilmurod\n📞  974403441 Hojiakbar")
    await bot.send_location(chat_id=message.chat.id, latitude=41.3621521, longitude=69.2296312)

# Elektrik
@dp.message(lambda message: message.text == "Elektrik")
async def elektrik_info(message: types.Message):
    await message.answer("📞  970004081  Diyor")
    await bot.send_location(chat_id=message.chat.id, latitude=41.3621521, longitude=69.2296312)

# Gazovik
@dp.message(lambda message: message.text == "Gazovik")
async def gazovik_info(message: types.Message):
    await message.answer("📞  971234040  Sherzod")
    await bot.send_location(chat_id=message.chat.id, latitude=41.3621521, longitude=69.2296312)

# Kostoprav
@dp.message(lambda message: message.text == "Kostoprav")
async def kostoprav_info(message: types.Message):
    await message.answer("📞  909128646 Abdusamad")
    await bot.send_location(chat_id=message.chat.id, latitude=41.3621521, longitude=69.2296312)  

# Avto zapchast
@dp.message(lambda message: message.text == "Avto zapchast")
async def zapchast_info(message: types.Message):
    await message.answer("📞  770010407  Abror")
    await bot.send_location(chat_id=message.chat.id, latitude=41.3621521, longitude=69.2296312)

# Himchistka
@dp.message(lambda message: message.text == "Himchistka")
async def himchistka_info(message: types.Message):
    await message.answer("📞  936809508  Yusuf")
    await bot.send_location(chat_id=message.chat.id, latitude=41.3621521, longitude=69.2296312)

# Palirovka
@dp.message(lambda message: message.text == "Palirovka")
async def palirovka_info(message: types.Message):
    await message.answer("📞  936809508  Yusuf")
    await bot.send_location(chat_id=message.chat.id, latitude=41.3621521, longitude=69.2296312)

# Возврат в главное меню
@dp.message(lambda message: message.text == "⬅️ Ortga")
async def back_to_main_menu(message: types.Message):
    await message.answer("Asosiy menyu:", reply_markup=main_menu)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
