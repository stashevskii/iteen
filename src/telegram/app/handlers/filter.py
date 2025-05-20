from telebot import TeleBot, types
from src.images.filter import Filter
from src.telegram.app.keyboards.inline import filters_keyboard
from src.telegram.app.utils.phrases import send_me_photo_phrase, choose_filter_phrase, changed_image_phrase
from src.telegram.app.сommon.handler import BaseHandler


class FiltersHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)
        self.filter = Filter()

    def __del_message(self, message: types.Message, subtract: int = 0):
        self.bot.delete_message(message.chat.id, message.message_id - subtract)

    def __handle_photo(self, message: types.Message):
        if not message.photo:
            self.__del_message(message)
            self.bot.send_message(message.chat.id, send_me_photo_phrase)
            self.bot.register_next_step_handler(message, self.__handle_photo)
            return
        downloaded_file = self.bot.download_file(self.bot.get_file(message.photo[-1].file_id).file_path)
        self.filter.set_src_img(downloaded_file)
        self.bot.send_message(message.chat.id, choose_filter_phrase, reply_markup=filters_keyboard)

    def add_filters(self, call: types.CallbackQuery):
        self.bot.send_photo(call.message.chat.id, self.filter.add_filter(call.data.split("_")[2]), caption=changed_image_phrase)

    def begin(self, call: types.CallbackQuery):
        self.__del_message(call.message)
        self.bot.send_message(call.message.chat.id, send_me_photo_phrase)
        self.bot.register_next_step_handler(call.message, self.__handle_photo)

    def register_command_handlers(self):
        self.bot.callback_query_handler(func=lambda call: call.data == "filters")(self.begin)
        self.bot.callback_query_handler(func=lambda call: call.data.startswith("image_filter"))(self.add_filters)
