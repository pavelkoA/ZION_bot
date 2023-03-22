from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Text, Command
from aiogram.methods.get_chat_administrators import GetChatAdministrators
import bot

router: Router = Router()

@router.message(Command(commands=['admins']))
async def process_start_command(message: Message):
    await message.answer(text=str(get_chat_admins(bot, message.chat.id)))