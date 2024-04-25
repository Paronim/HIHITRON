from langchain.schema import SystemMessage
from langchain.chat_models.gigachat import GigaChat
from config import chat_token
from gigaChat import promts
from langchain.prompts import load_prompt

# Авторизация в сервисе GigaChat
def Auth():
    chat = GigaChat(credentials=chat_token, verify_ssl_certs=False)
    return chat

def mainPromt():
    messages = [
    SystemMessage(
        content="Ты высоковалифицированный бот-юрист, который помогает пользователю решить его проблемы связанные с законодаьельством РФ."
    )
    ]
    return messages

def classPromt(chat, messege):
    prompt = load_prompt('promts.yaml')
    chain = prompt | chat
    promt_category = chain.invoke(
        {
            "text": messege
        }
    ).content
    return promt_category