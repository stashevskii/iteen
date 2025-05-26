from telebot import TeleBot, types
from src.images.filter import Filter
from src.telegram.app.keyboards.inline import filters_keyboard
from src.telegram.app.utils.bot import get_photo, delete_message
from src.telegram.app.utils.phrases import send_me_photo_phrase, choose_filter_phrase, changed_image_phrase
from src.telegram.app.common.handler import BaseHandler


class FiltersHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)
        self.filter = Filter()

    def __handle_photo(self, message: types.Message) -> None:
        self.filter.set_src_img(get_photo(self.bot, message, self.__handle_photo))
        self.bot.send_message(message.chat.id, choose_filter_phrase, reply_markup=filters_keyboard)

    def add_filters(self, call: types.CallbackQuery) -> None:
        delete_message(self.bot, call.message)
        self.bot.send_photo(
            call.message.chat.id,
            self.filter.add_filter(call.data.split("_")[2]),
            caption=changed_image_phrase
        )

    def begin(self, call: types.CallbackQuery) -> None:
        delete_message(self.bot, call.message)
        self.bot.send_message(call.message.chat.id, send_me_photo_phrase)
        self.bot.register_next_step_handler(call.message, self.__handle_photo)

    def register_command_handlers(self) -> None:
        self.bot.callback_query_handler(func=lambda call: call.data == "filters")(self.begin)
        self.bot.callback_query_handler(func=lambda call: call.data.startswith("image_filter"))(self.add_filters)
