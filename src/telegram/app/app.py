from telebot import TeleBot

from src.telegram.app.handlers.root import BasicCommandsHandler
from src.telegram.app.handlers.resize import ImageHandler
from src.telegram.app.utils.env import config


def init_handlers(bot: TeleBot) -> None:
    BasicCommandsHandler(bot).register_command_handlers()
    ImageHandler(bot).register_command_handlers()


def create_bot() -> TeleBot:
    bot = TeleBot(config.tg_token)
    init_handlers(bot)
    return bot


def polling(bot: TeleBot) -> None:
    bot.polling(interval=0, none_stop=True)


bot = create_bot()
