"""Telegram-бот для фитнес-трекера Synchromatica.

Выдаёт персональную ссылку пользователю и открывает WebApp.
Стек: Python 3.11+, aiogram 3.x.
"""

import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_BASE_URL = os.getenv(
    "WEBAPP_BASE_URL",
    "https://juzoo9.github.io/synchromatica-fitness/"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message) -> None:
    """Обработчик команды /start.

    Приветствует пользователя, формирует персональную ссылку на основе его ID
    и отправляет клавиатуру с WebApp и прямой ссылкой.
    """
    user = message.from_user
    user_id = user.id if user else 0
    first_name = user.first_name if user else "Атлет"

    # Формируем персональную ссылку
    clean_base = WEBAPP_BASE_URL.rstrip("/") + "/"
    personal_url = f"{clean_base}?uid={user_id}"

    text = (
        f"👋 <b>Привет, {first_name}!</b>\n\n"
        f"Добро пожаловать в <b>Synchromatica Fitness</b> — твой персональный "
        f"трекер прогресса в зале с умной аналитикой перегрузки весов.\n\n"
        f"🔒 <b>Твой Telegram ID:</b> <code>{user_id}</code>\n"
        f"Все твои тренировки, рекорды и программы изолированы и привязаны только к тебе.\n\n"
        f"🔗 <b>Твоя персональная ссылка для браузера на ПК:</b>\n"
        f"<code>{personal_url}</code>\n\n"
        f"<i>(Открывай её на компьютере или ноутбуке — данные будут общими с этим ботом!)</i>"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🏋️ Открыть трекер в Telegram",
                    web_app=WebAppInfo(url=personal_url)
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌐 Открыть в браузере (ПК)",
                    url=personal_url
                )
            ]
        ]
    )

    await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.HTML)


async def main() -> None:
    """Точка входа запуска бота."""
    if not BOT_TOKEN:
        logger.error(
            "BOT_TOKEN не задан! Создайте файл .env с BOT_TOKEN=ваш_токен_из_BotFather"
        )
        print("\n[!] ОШИБКА: Задайте BOT_TOKEN в файле .env")
        print("Пример содержимого .env:\nBOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ\n")
        return

    bot = Bot(token=BOT_TOKEN)
    logger.info("Запуск бота Synchromatica...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
