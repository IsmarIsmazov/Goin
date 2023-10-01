from aiogram import Bot
from decouple import config as env

API_KEY = env("API_KEY")
bot = Bot(token=API_KEY)


async def send_notification(chat_id, message_text):
    await bot.send_message(chat_id, message_text)
