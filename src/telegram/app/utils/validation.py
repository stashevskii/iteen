from telebot import types


def check_new_sizes(message: types.Message) -> list:
    try:
        r = list(map(int, message.text.split("x")))
        return [] if len(r) != 2 else r
    except ValueError:
        return []
