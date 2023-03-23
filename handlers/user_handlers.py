from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Text, Command
from aiogram.handlers import PollHandler
from aiogram.methods.get_chat_administrators import GetChatAdministrators
import bot

from keyboards.keyboards import kb_popivu, kb_opros

router: Router = Router()

# @router.message(Command(commands=['admins']))
# async def process_start_command(message: Message):
#     await message.answer(text=str(get_chat_admins(bot, message.chat.id)))

@router.message(Command(commands=['popivy']))
async def process_popivu_commands(message: Message):
    await message.answer(text='Ну наконец здравое предложение!!!🥳🥳🥳')
    await message.answer_poll(question='Пиво пить будем?',
                              options=['ДА', 'НЕТ', 'Я Влад'],
                              type='regular',
                              is_anonymous=False)
