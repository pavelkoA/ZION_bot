from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Text
from filters.language_filter import forbid_wrds

router: Router = Router()

@router.message()
async def other_message(message: Message):
    if forbid_wrds(message):
        await message.delete()