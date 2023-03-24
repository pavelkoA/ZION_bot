import asyncio
import logging

from aiogram import Bot, Dispatcher, Router

from config_data.config import load_config, Config
from handlers import other_handlers, user_handlers

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
                    u'[%(asctime)s] - %(name)s - %(message)s')

async def main():

    config: Config = load_config()

    logger.info('Starting Bot')

    bot: Bot = Bot(token=config.tgbot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')




