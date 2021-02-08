import os


# Bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Web application setup
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))

# Webhook setup
WEBHOOK_HOST = 'https://neural-painter-bot.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
