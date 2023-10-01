import asyncio

from django.core.management.base import BaseCommand
from decouple import config as env
from telegram import Bot, Update
from telegram.ext import CallbackContext, MessageHandler, Updater

BOT_KEY = env("API_KEY")


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f"Произошло ошибка: {e}"
            print(error_message)
            raise e

    return inner


@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    reply_text = "Ваг ID = {}\n\n{}".format(chat_id, text)
    update.message.reply_text(
        text=reply_text
    )


class Command(BaseCommand):
    help = "Телеграмм бот"

    def handle(self, *args, **options):
        bot = Bot(
            token=BOT_KEY,
        )
        me = asyncio.run(self.get_bot_username(bot))
        print(me)

        updater = Updater(
            bot=bot,

        )
        message_handler = MessageHandler(None, do_echo)
        updater.dispather.add_handler(message_handler)

        updater.start_polling()

    async def get_bot_username(self, bot):
        me = await bot.get_me()
        return me
