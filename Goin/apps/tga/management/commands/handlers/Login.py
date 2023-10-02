from asgiref.sync import sync_to_async
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from decouple import config as env
from aiogram import Bot, Dispatcher, types

from .backend import create_or_get_admin, check_chat_id_exists, remove_chat_id

PASSWORD_ADMIN = env("PASSWORD")
BOT_KEY = env("API_KEY")
storage = MemoryStorage()
bot = Bot(BOT_KEY)
dp = Dispatcher(bot=bot, storage=storage)


class LoginAdmin(StatesGroup):
    password = State()


async def start(message: types.Message):
    if message.chat.type == 'private':
        await LoginAdmin.password.set()
        await message.answer("Введите пароль от админ панели")

    else:
        await message.answer('Данная команда не доступна в группе')


async def wait_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
    print(f"Введенный пароль: {data['password']}")

    if data['password'] == PASSWORD_ADMIN:
        chat_id = message.chat.id
        username = message.from_user.username
        admin, created = await create_or_get_admin(chat_id, username)
        if created:
            await message.answer("Вы успешно вошли и вас добавили в базу данных!")
        else:
            chat_id_exists = await check_chat_id_exists(chat_id)

            if chat_id_exists:
                await message.answer("Вы уже вошли ранее!")
                await state.finish()
            else:
                await message.answer("Вы не смогли войти!")
                await state.finish()
    else:
        await state.finish()
        await message.answer("Не правильный пароль")


async def handle_exit_command(message: types.Message):
    chat_id = message.chat.id

    removed = await remove_chat_id(chat_id)

    if removed:
        await message.answer("Вы успешно вышли и ваш chat_id удален!")
    else:
        await message.answer("ваш chat_id не существует в базе данных!")


def register_login(dp: Dispatcher):
    dp.register_message_handler(start, commands=['admin'])
    dp.register_message_handler(wait_password, state=LoginAdmin.password)
    dp.register_message_handler(handle_exit_command, commands=['exit'])
