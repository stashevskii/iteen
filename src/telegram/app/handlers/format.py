from telebot import TeleBot, types
from src.images.format import FormatChanger
from src.telegram.app.keyboards.inline import format_keyboard
from src.telegram.app.utils.bot import get_photo, delete_message
from src.telegram.app.utils.phrases import send_me_photo_phrase, choose_format_phrase, changed_image_phrase
from src.telegram.app.common.handler import BaseHandler


class FormatChangeHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)
        self.changer = FormatChanger()

    def __handle_photo(self, message: types.Message) -> None:
        self.changer.set_src_img(get_photo(self.bot, message, self.__handle_photo))
        self.bot.send_message(message.chat.id, choose_format_phrase, reply_markup=format_keyboard)

    def change_format(self, call: types.CallbackQuery) -> None:
        delete_message(self.bot, call.message)
        fmt = call.data.split("_")[2]
        self.bot.send_document(
            call.message.chat.id,
            document=self.changer.change_format(fmt),
            caption=changed_image_phrase,
            visible_file_name=f"result.{fmt.lower()}",
            disable_content_type_detection=True
        )

    def begin(self, call: types.CallbackQuery) -> None:
        delete_message(self.bot, call.message)
        self.bot.send_message(call.message.chat.id, send_me_photo_phrase)
        self.bot.register_next_step_handler(call.message, self.__handle_photo)

    def register_command_handlers(self) -> None:
        self.bot.callback_query_handler(func=lambda call: call.data == "format")(self.begin)
        self.bot.callback_query_handler(func=lambda call: call.data.startswith("image_format"))(self.change_format)
