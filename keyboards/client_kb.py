# Импорт клавиатурных кнопок телеграм
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопка /OH - охрана труда, /EB - электро- безопасность
b1 = KeyboardButton('/OH')
b2 = KeyboardButton('/EB')

# Инициализация кнопок, resize - авторазмер кнопки, one_time - после одного нажатия - свернуть кнопки
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# add Отображает кнопки по строчно, для редизайна можно использовать inseart() или row()
kb_client.add(b1, b2)
