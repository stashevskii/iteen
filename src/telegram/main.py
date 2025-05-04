from src.telegram.app.app import bot

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
