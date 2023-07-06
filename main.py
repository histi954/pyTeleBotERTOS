# logging - библиотека логирования состояния программы. Необходима для записи и контроля над выполнением программы)
import logging
# Executor - точка входа для выполнения кода телеграм ботом
from aiogram import executor
# Связь между исполняющим модулем create_bot и этим файлом по средством вызова метода dp из него сюда
from create_bot import dp

# Configure logging
logging.basicConfig(level=logging.INFO)


# Уведомление о старте программы в консоль
async def on_startup(_):
    print('Бот вышел в онлайн')


# Менеджмент кода. Вызываем отсюда, выполняется в других модулях
from handlers import client, admin, other

client.register_handlers_client(dp)
# client.register_handlers_admin(dp)
# client.register_handlers_other(dp)


# Точка входа
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
