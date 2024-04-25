import telebot
from telebot import types
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='YzcwMGMzZTEtMjY1ZS00MmZkLTliYWQtZjZmOTFmODY1ODEwOmQ5ODg4OWY0LWY3M2EtNDQ4Yy04YjAxLTNhZDUxMjMxNjdiMg==')

messages = [
    SystemMessage(
        content="Ты высоковалифицированный бот-юрист, который помогает пользователю решить его проблемы связанные с законодаьельством РФ."
    )
]

# Initialize the bot
bot = telebot.TeleBot('7019952787:AAFryO24ON1r-6pfrxHTVfl9pKTrmXQBs3w')

# Create keyboard
keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_start = types.KeyboardButton('Старт')
button_restart = types.KeyboardButton('Перестарт')
button_end = types.KeyboardButton('Ценок')
keyboard.add(button_start, button_restart, button_end)

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот-юрист, готов помочь тебе с вопросами законодательства РФ.", reply_markup=keyboard)

# Handle /restart command
@bot.message_handler(commands=['restart'])
def restart_chat(message):
    global messages
    messages = [
        SystemMessage(
            content="Ты высоковалифицированный бот-юрист, который помогает пользователю решить его проблемы связанные с законодаьельством РФ."
        )
    ]
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
bot.polling()
