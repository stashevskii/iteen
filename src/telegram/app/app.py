from telebot import TeleBot

from src.telegram.app.handlers.basic_commands import BasicCommandsHandler
from src.telegram.app.handlers.create_quizz import CreateQuizzHandler
from src.telegram.app.utils.env import config


def init_handlers(b: TeleBot):
    BasicCommandsHandler(b).register_command_handlers()
    CreateQuizzHandler(b).register_command_handlers()

def create_bot() -> TeleBot:
    b = TeleBot(config.tg_token)
    init_handlers(b)
    return b


bot = create_bot()
