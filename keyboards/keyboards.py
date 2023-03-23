from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup

kb_popivu: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ДАААА', callback_data='yes')],
                                                                        [InlineKeyboardButton(text='Я душнила', callback_data='no')]])

poll_btn_2: KeyboardButton = KeyboardButton(
                                text='Опросить жителей сего чата???',
                                request_poll=KeyboardButtonPollType(
                                                        type='regular', ))

kb_opros: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[poll_btn_2]],
                                                    resize_keyboard=True)

