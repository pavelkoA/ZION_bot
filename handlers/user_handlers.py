from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Text, Command
from external_services.bithday import happy_bd

from keyboards.keyboards import kb_popivu, kb_opros
from lexicon.lexicon_ru import words

router: Router = Router()

@router.message(Command(commands=['help']))
async def process_start_command(message: Message):
    await message.answer(text=words['help'])

@router.message(Command(commands=['popivy']))
async def process_popivu_commands(message: Message):
    await message.answer(text='Ну наконец здравое предложение!!!🥳🥳🥳')
    await message.answer_poll(question='Пиво пить будем?',
                              options=['ДА', 'НЕТ', 'Я Влад'],
                              type='regular',
                              is_anonymous=False)

#Хендлер для команды hb, поздравляет пользователя с днем рождения
@router.message(Command(commands='hb'))
async def command_happy_bd(message: Message):
    hb = str(happy_bd())
    try:
        await message.answer(text=f'Дорогой {message.text.split()[1]} {hb}')
    except IndexError:
        await message.answer(text=f'Дорогой, кто там сегодня? {hb}')
