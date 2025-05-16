from telebot import TeleBot, types
from src.telegram.app.keyboards.inline import start_keyboard
from src.telegram.app.utils.phrases import greet_phrase
from src.telegram.app.сommon.handler import BaseHandler


class BasicCommandsHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)

    def start(self, message: types.Message):
        self.bot.send_message(message.chat.id, greet_phrase, reply_markup=start_keyboard)

    def menu(self, message: types.Message):
        self.bot.send_message(message.chat.id, "Главное меню 👇👇👇", reply_markup=start_keyboard)

    def register_command_handlers(self):
        self.bot.message_handler(commands=["start"])(self.start)
        self.bot.message_handler(commands=["menu"])(self.menu)
