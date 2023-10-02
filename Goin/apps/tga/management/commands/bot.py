import asyncio
import logging

from aiogram.utils import executor
from django.core.management.base import BaseCommand

from .handlers.Login import dp, register_login

register_login(dp)


class Command(BaseCommand):
    help = "Телеграмм бот"

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO)
        executor.start_polling(dp, skip_updates=True)
