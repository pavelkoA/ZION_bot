from aiogram.types import Message
from lexicon.lexicon_ru import forbidden_words

def forbid_wrds(message: Message) -> bool:
    msg = message.text.split()
    for word in msg:
        if word.lower() in forbidden_words:
            return True
    return False