from aiogram.types import Message
from lexicon.lexicon_ru import forbidden_words

def forbid_wrds(message: Message) -> bool:
    for word in forbidden_words:
        if word in message.text:
            return True
    return False


