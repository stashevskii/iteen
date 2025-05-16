from io import BytesIO
from PIL import Image
from telebot import TeleBot, types

from src.images.resize import ImageResizer
from src.telegram.app.utils.phrases import *
from src.telegram.app.utils.validation import check_new_sizes
from src.telegram.app.сommon.handler import BaseHandler


class ImageHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)
        self.resizer = ImageResizer()

    def __del_message(self, message: types.Message, subtract: int = 0):
        self.bot.delete_message(message.chat.id, message.message_id - subtract)

    def __handle_photo(self, message: types.Message):
        if not message.photo:
            self.__del_message(message)
            self.bot.send_message(message.chat.id, send_me_photo_phrase)
            self.bot.register_next_step_handler(message, self.__handle_photo)
            return
        downloaded_file = self.bot.download_file(self.bot.get_file(message.photo[-1].file_id).file_path)
        self.resizer.set_src_img(downloaded_file)
        self.bot.send_message(message.chat.id, enter_sizes_phrase)
        self.bot.register_next_step_handler(message, self.__handle_new_sizes)

    def __handle_new_sizes(self, message: types.Message):
        sizes = check_new_sizes(message)
        if not sizes:
            self.__del_message(message)
            self.bot.send_message(message.chat.id, incorrect_format_of_sizes_phrase)
            self.bot.register_next_step_handler(message, self.__handle_new_sizes)
            return
        response = self.bot.send_message(message.chat.id, creating_image_phrase)
        self.bot.send_photo(message.chat.id, self.resizer.change_sizes((tuple(sizes))), caption=changed_image_phrase)
        self.__del_message(response)

    def resize_image(self, call: types.CallbackQuery):
        self.__del_message(call.message)
        self.bot.send_message(call.message.chat.id, send_me_photo_phrase)
        self.bot.register_next_step_handler(call.message, self.__handle_photo)

    def register_command_handlers(self):
        self.bot.callback_query_handler(func=lambda call: call.data == "resize")(self.resize_image)
