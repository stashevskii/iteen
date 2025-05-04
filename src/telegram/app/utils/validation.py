from telebot import types, TeleBot
from src.telegram.app.utils.phrases import enter_number, enter_number_more_than_zero


def check_message_text(message: types.Message) -> bool:
    if message.text:
        return True
    return False


def validate_question_quantity(message: types.Message, bot: TeleBot) -> bool:
    if check_message_text(message) and message.text.isdigit():
        if int(message.text) <= 0:
            bot.send_message(message.chat.id, enter_number_more_than_zero)
            return False
        return True
    bot.send_message(message.chat.id, enter_number)
    return False


def validate_poll(poll) -> bool:
    if poll.is_closed or poll.is_anonymous or poll.type != "quiz":
        return False
    return True


def check_message_has_poll(message: types.Message) -> bool:
    try:
        _ = message.poll
        return True
    except AttributeError:
        return False
