from telebot import TeleBot, types
from src.images.resize import Resizer
from src.telegram.app.utils.phrases import *
from src.telegram.app.utils.validation import check_new_sizes
from src.telegram.app.common.handler import BaseHandler
from src.telegram.app.utils.bot import get_photo, delete_message


class ResizeHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)
        self.resizer = Resizer()

    def __handle_photo(self, message: types.Message) -> None:
        self.resizer.set_src_img(get_photo(self.bot, message, self.__handle_photo))
        self.bot.send_message(message.chat.id, enter_sizes_phrase)
        self.bot.register_next_step_handler(message, self.__handle_new_sizes)

    def __handle_new_sizes(self, message: types.Message) -> None:
        sizes = check_new_sizes(message)
        if not sizes:
            delete_message(self.bot, message)
            self.bot.send_message(message.chat.id, incorrect_format_of_sizes_phrase)
            self.bot.register_next_step_handler(message, self.__handle_new_sizes)
            return
        self.bot.send_photo(message.chat.id, self.resizer.change_sizes((tuple(sizes))), caption=changed_image_phrase)

    def begin(self, call: types.CallbackQuery) -> None:
        delete_message(self.bot, call.message)
        self.bot.send_message(call.message.chat.id, send_me_photo_phrase)
        self.bot.register_next_step_handler(call.message, self.__handle_photo)

    def register_command_handlers(self) -> None:
        self.bot.callback_query_handler(func=lambda call: call.data == "resize")(self.begin)
