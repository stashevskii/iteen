from typing import Callable
from telebot import types, TeleBot

from src.telegram.app.utils.phrases import send_me_photo_phrase


def delete_message(bot: TeleBot, message: types.Message, subtract: int = 0):
    bot.delete_message(message.chat.id, message.message_id - subtract)


def get_photo(bot: TeleBot, message: types.Message, unsuccess: Callable) -> bytes | None:
    if not message.photo:
        delete_message(bot, message)
        bot.send_message(message.chat.id, send_me_photo_phrase)
        bot.register_next_step_handler(message, unsuccess)
        return
    return bot.download_file(bot.get_file(message.photo[-1].file_id).file_path)
