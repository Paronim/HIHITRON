from langchain.schema import SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
def Auth():
    chat = GigaChat(credentials='YzcwMGMzZTEtMjY1ZS00MmZkLTliYWQtZjZmOTFmODY1ODEwOmQ5ODg4OWY0LWY3M2EtNDQ4Yy04YjAxLTNhZDUxMjMxNjdiMg==', verify_ssl_certs=False)
    return chat

def mainPromt():
    messages = [
    SystemMessage(
        content="Ты высоковалифицированный бот-юрист, который помогает пользователю решить его проблемы связанные с законодаьельством РФ."
    )
    ]
    return messages

