import telebot
from telebot import types
from gigaChat import methods
from config import tg_token
from langchain.schema import HumanMessage

chat = methods.Auth()

messages = methods.mainPromt()

# Initialize the bot
bot = telebot.TeleBot(tg_token)

keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_start = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_restart = types.KeyboardButton('Прервать беседу')
button_start = types.KeyboardButton('Старт')

keyboard.add(button_restart)
keyboard_start.add(button_start)

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    bot.send_message(message.chat.id, "Привет! Я бот-юрист, готов помочь тебе с вопросами законодательства РФ.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Прервать беседу")
def restart_chat(message):
    methods.mainPromt()

    bot.send_message(message.chat.id, "Чат перезапущен.", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Хотите еще что-то спросить?", reply_markup=keyboard)
    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    

# Handle all text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        user_input = message.text
        promt_category = methods.classPromt(chat, user_input)

        if promt_category == "другие":
            result = "Это вне моей компетенции"
        else:
            messages.append(HumanMessage(content=user_input))
            res = chat(messages)
            messages.append(res)
            result = res.content

        bot.reply_to(message, result)

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")

# Start the bot
def startBot():
    bot.polling()