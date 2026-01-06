import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)


TOKEN = os.getenv("API_TOKEN")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start(message: types.Message):
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text="Открыть кпокак",
                        web_app=WebAppInfo(url="https://cid1228.github.io/MyFirstRepository/")
                    )
                ]
            ],
            resize_keyboard=True
        )

        await message.answer(
            "зомби блять выживание скачать без смс и регистрации",
            reply_markup=markup
        )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
