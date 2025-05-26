from telebot import TeleBot, types
from src.images.qr import QR
from src.telegram.app.utils.bot import delete_message
from src.telegram.app.utils.phrases import send_me_url_phrase, qr_code_phrase
from src.telegram.app.common.handler import BaseHandler


class QRHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)
        self.qr_creator = QR()

    def __ask_for_url(self, message: types.Message) -> None:
        self.bot.send_photo(message.chat.id, self.qr_creator.get_qr(message.text), caption=qr_code_phrase)

    def begin(self, call: types.CallbackQuery) -> None:
        delete_message(self.bot, call.message)
        self.bot.send_message(call.message.chat.id, send_me_url_phrase)
        self.bot.register_next_step_handler(call.message, self.__ask_for_url)

    def register_command_handlers(self) -> None:
        self.bot.callback_query_handler(func=lambda call: call.data == "qr")(self.begin)
