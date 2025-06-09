from telebot import TeleBot, types
from src.telegram.app.keyboards.inline import start_keyboard
from src.telegram.app.utils.phrases import greet_phrase, menu_phrase, help_phrase
from src.telegram.app.common.handler import BaseHandler


class RootHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)

    def start(self, message: types.Message) -> None:
        self.bot.send_message(message.chat.id, greet_phrase, reply_markup=start_keyboard)

    def menu(self, message: types.Message) -> None:
        self.bot.send_message(message.chat.id, menu_phrase, reply_markup=start_keyboard)

    def help(self, message: types.Message) -> None:
        self.bot.send_message(message.chat.id, help_phrase)

    def register_command_handlers(self) -> None:
        self.bot.message_handler(commands=["start"])(self.start)
        self.bot.message_handler(commands=["menu"])(self.menu)
        self.bot.message_handler(commands=["help"])(self.help)
