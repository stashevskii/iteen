from telebot import types
from src.telegram.app.utils.phrases import create_quizz_phrase

remove_keyboard = types.ReplyKeyboardRemove()

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.row(create_quizz_phrase)
