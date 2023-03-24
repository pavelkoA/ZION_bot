from aiogram import F
from aiogram.types import Message
from lexicon.lexicon_ru import words

#Функция возвращает True если в сообщениях встречается запрещенное в чате слово
def forbid_wrds(message: Message) -> bool:
    for word in words['forbidden_words']:
        if word in message.text.lower():
            return True
    return False

#Функция возвращает True если в сообщение встречается призыв собраться
def sbor_wrds(message: Message) -> bool:
    for word in words['sbor']:
        if word in message.text.lower():
            return True
    return False

