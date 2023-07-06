# os - в данном случае используется для работы с .bat файлом (чтение из него)
import os
# aiogram - библиотека для работы с телеграм ботом
# Bot, Dispatcher - инициализаторы бота и метода работы с ним
from aiogram import Bot, Dispatcher
# Memory storage - нужна для машины состояний, сохраняет последовательность ответов от пользователя в оперативке
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
