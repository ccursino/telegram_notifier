import requests

# Substitua pelo token do seu bot
TOKEN = 'YOUR_BOT_TOKEN'

# Substitua pelo nome de usuário do seu bot
USERNAME = 'YOUR_BOT_USERNAME'

# API URL para obter atualizações
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url)
data = response.json()

# Procure pelo chat_id
for result in data['result']:
    if 'message' in result and result['message']['chat']['username'] == USERNAME:
        chat_id = result['message']['chat']['id']
        print(f'Chat ID: {chat_id}')
        break
