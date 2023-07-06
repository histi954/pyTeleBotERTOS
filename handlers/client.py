from aiogram import types, Dispatcher
from text_commands_for_tbot import comanda_start
from keyboards import kb_client


# @dp.message_handler(commands=['start']) - декоратор, используется для вызова метода напрямую из библиотеки
# но сейчас не используется так как вызывается методом dp. ниже
async def send_welcome(message: types.Message):
    '''Запуск бота при вводе пользователем команды /start'''
    try:
        # Если штатно: отрабатывает ответ от бота с переменной comana_start, хранится в файле с большим текстом
        # И вызывает клавиатуру с кастомными кнопками
        await message.answer(comanda_start, reply_markup=kb_client)
    except:
        # Если что-то пошло не так:
        await message.reply('Напишите боту в личные сообщения /start')


# Замена встроенным декораторам. В последующем можно переделать под class
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
