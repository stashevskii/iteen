from telebot import TeleBot

from src.telegram.app.handlers.filter import FiltersHandler
from src.telegram.app.handlers.format import FormatChangeHandler
from src.telegram.app.handlers.resize import ResizeHandler
from src.telegram.app.handlers.root import RootHandler
from src.telegram.app.utils.env import config


def init_handlers(bot: TeleBot) -> None:
    handlers = [RootHandler, ResizeHandler, FormatChangeHandler, FiltersHandler]
    for handler in handlers:
        handler(bot).register_command_handlers()


def create_bot() -> TeleBot:
    bot = TeleBot(config.tg_token)
    init_handlers(bot)
    return bot


def polling(bot: TeleBot) -> None:
    bot.polling(interval=0, none_stop=True)


bot = create_bot()
