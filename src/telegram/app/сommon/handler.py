from telebot import TeleBot


class BaseHandler:
    def __init__(self, bot: TeleBot):
        self.bot = bot
