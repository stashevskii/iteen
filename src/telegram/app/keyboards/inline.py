from telebot import types

start_keyboard = types.InlineKeyboardMarkup()
start_keyboard.add(types.InlineKeyboardButton("Изменить размер", callback_data="resize"))
start_keyboard.add(types.InlineKeyboardButton("Изменить формат", callback_data="format"))
start_keyboard.add(types.InlineKeyboardButton("Наложить фильтры", callback_data="filters"))
start_keyboard.add(types.InlineKeyboardButton("Создать QR код", callback_data="qr"))
start_keyboard.add(types.InlineKeyboardButton("Картика в текст", callback_data="itt"))

format_keyboard = types.InlineKeyboardMarkup()
format_keyboard.add(types.InlineKeyboardButton("WEBP", callback_data="image_format_WEBP"))
format_keyboard.add(types.InlineKeyboardButton("PNG", callback_data="image_format_PNG"))
format_keyboard.add(types.InlineKeyboardButton("JPEG", callback_data="image_format_JPEG"))
format_keyboard.add(types.InlineKeyboardButton("BMP", callback_data="image_format_BMP"))

filters_keyboard = types.InlineKeyboardMarkup()
filters_keyboard.add(types.InlineKeyboardButton("Блюр", callback_data="image_filter_BLUR"))
filters_keyboard.add(types.InlineKeyboardButton("Контур", callback_data="image_filter_EMBOSS"))
filters_keyboard.add(types.InlineKeyboardButton("Черно-белый", callback_data="image_filter_BW"))
