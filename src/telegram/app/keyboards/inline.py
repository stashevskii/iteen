from telebot import types

remove_keyboard = types.ReplyKeyboardRemove()

start_keyboard = types.InlineKeyboardMarkup()
start_keyboard.add(types.InlineKeyboardButton("Изменить размер", callback_data="resize"))
start_keyboard.add(types.InlineKeyboardButton("Обрезать ✂️", callback_data="crop"))
