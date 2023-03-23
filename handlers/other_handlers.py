from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Text
from filters.language_filter import forbid_wrds, sbor_wrds
from keyboards.keyboards import kb_opros

router: Router = Router()

@router.message(F.text)
async def other_message(message: Message):
    if forbid_wrds(message):
        await message.delete()
    elif sbor_wrds(message):
        await message.answer(text='Ну наконец здравое предложение!!!🥳🥳🥳')
        await message.answer_poll(question='Пиво пить будем?',
                                  options=['ДА', 'НЕТ', 'Я Влад'],
                                  type='regular',
                                  is_anonymous=False)
