import logging
import os

from database import accounts
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import dotenv

dotenv.load_dotenv()
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.environ.get("TELEGRAM_BOT")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard_code = types.ReplyKeyboardMarkup(resize_keyboard=True)
code_btn = types.KeyboardButton("Код")
keyboard_code.add(code_btn)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    name = f"{message.chat.first_name} {message.chat.last_name}".replace(
        "None", ""
    ).strip()
    if not accounts.is_user_registered(chat_id):
        accounts.register_user(chat_id, name)
    await message.answer(
        "Привет!\n\nЯ бот для уведомлений и доступа к площадке ErosCRM.\n\n"
        "Если тебе нужно будет авторизоваться - пиши.\nОтвечу на команды /code или `Код`."
        "\n\nПомни, для каждой авторизации нужен новый код!\n\nМоя главная задача - информирование."
        "\n\nДо встречи!",
        reply_markup=keyboard_code,
    )


@dp.message_handler(lambda m: m.text == "/code" or m.text.lower() == "код")
async def send_code(message: types.Message):
    code = accounts.get_new_code(message.chat.id)
    await message.answer(
        "С возвращением!\n\nТвой новый код: ```" + str(code) + "```\n\nУдачи!",
        parse_mode=types.ParseMode.MARKDOWN,
        reply_markup=keyboard_code,
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
