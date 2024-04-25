import telebot
from telebot import types
from gigaChat import methods
from config import tg_token
from langchain.schema import HumanMessage

chat = methods.Auth()

messages = methods.mainPromt()

# Initialize the bot
bot = telebot.TeleBot(tg_token)

# Create keyboard
keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_start = types.KeyboardButton('Начать общение')
button_restart = types.KeyboardButton('Прервать беседу')
button_end = types.KeyboardButton('Закончить')
keyboard.add(button_start, button_restart, button_end)

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот-юрист, готов помочь тебе с вопросами законодательства РФ.", reply_markup=keyboard)

# Handle /restart command
@bot.message_handler(commands=['restart'])
def restart_chat(message):
    methods.mainPromt()
    bot.send_message(message.chat.id, "Чат перезапущен.", reply_markup=keyboard)

# Handle /end command
@bot.message_handler(commands=['end'])
def end_chat(message):
    bot.send_message(message.chat.id, "Чат завершен. Напишите /start, чтобы начать новый чат.", reply_markup=keyboard)

# Handle all text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        user_input = message.text
        messages.append(HumanMessage(content=user_input))
        res = chat(messages)
        messages.append(res)
        bot.reply_to(message, res.content)

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")

# Start the bot
def startBot():
    bot.polling()