from aiogram.types import Message
import requests
from bs4 import BeautifulSoup

def happy_bd():
    link = 'https://e79.ru/gen/birthday'
    req = requests.get(link)
    bs = BeautifulSoup(req.text, 'lxml').find('span', class_='span-area')
    return bs.text

