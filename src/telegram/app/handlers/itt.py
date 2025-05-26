from telebot import types

from src.images.itt import image_to_text
from src.telegram.app.common.handler import BaseHandler
from src.telegram.app.utils.bot import get_photo, delete_message
from src.telegram.app.utils.phrases import (
    send_me_photo_phrase,
    gotten_text_phrase,
    extracting_error_phrase
)


class ImageToTextHandler(BaseHandler):
    def __handle_photo(self, message: types.Message) -> None:
        img_bytes = get_photo(self.bot, message, self.__handle_photo)
        extracted = image_to_text(img_bytes)
        if extracted != -1:
            self.bot.send_message(message.chat.id, f"{gotten_text_phrase}\n{extracted}")
            return
        self.bot.send_message(message.chat.id, extracting_error_phrase)

    def begin(self, call: types.CallbackQuery) -> None:
        delete_message(self.bot, call.message)
        self.bot.send_message(call.message.chat.id, send_me_photo_phrase)
        self.bot.register_next_step_handler(call.message, self.__handle_photo)

    def register_command_handlers(self) -> None:
        self.bot.callback_query_handler(func=lambda call: call.data == "itt")(self.begin)
