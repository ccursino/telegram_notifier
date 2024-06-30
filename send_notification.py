import requests

def send_telegram_message(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

# Substitua pelo token do seu bot
TOKEN = 'YOUR_BOT_TOKEN'

# Substitua pelo seu chat ID
CHAT_ID = 'YOUR_CHAT_ID'

# Mensagem a ser enviada
MESSAGE = 'Process has ended!'

# Envie a mensagem
send_telegram_message(TOKEN, CHAT_ID, MESSAGE)
