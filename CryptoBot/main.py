import time

import requests
from telebot import TeleBot
from telebot import types
import random
import string
from os import getenv

TOKEN_TELEGRAM_BOT = getenv("TELEGRAM_API_TOKEN")
API_ENDPOINT_URL = f'http://backend:8080'
bot = TeleBot(TOKEN_TELEGRAM_BOT)

@bot.message_handler(commands=['start'])
def handle_start_command(message):
    user_id = message.from_user.id
    username = message.from_user.username
    is_premium = message.from_user.is_premium
    if is_premium == None:
        is_premium = False
    else:
        is_premium = True
    referral_code = len(message.text.split()) > 1 and message.text.split()[1] or None
    print(is_premium)
    photos = bot.get_user_profile_photos(user_id)
    file_id = photos.photos[0][0].file_id
    file = bot.get_file(file_id)
    url = f"{API_ENDPOINT_URL}/api/v.1.0/oauth/create_user?client_id=1&referral_code={referral_code}"
    payload = {
        "user_id": f'{user_id}',
        "username": username,
        "file_path": f'{file.file_path}',
        "is_premium": is_premium,
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Пытается определить HTTP ошибки
        data = response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        bot.send_message(user_id, "Произошла ошибка при связи с сервером.")
        return
    except requests.exceptions.RequestException as e:
        print(f"Error while requesting: {e}")
        bot.send_message(user_id, "Произошла ошибка при попытке соединения.")
        return

    api_key = data.get('token', '')

    keyboard = types.InlineKeyboardMarkup()
    webAppInfo = types.WebAppInfo(f"{getenv('WEBAPP_URL')}?api_key={api_key}")
    button_play = types.InlineKeyboardButton("💵 Начать играть", web_app=webAppInfo)
    keyboard.row(button_play)

    bot.send_message(user_id, "Добро пожаловать в крипто бота. Это техническое сообщение, его надо будет заменить. Аккаунт был добавлен в базу данных", reply_markup=keyboard)

if __name__ == '__main__':
    try:
        print("BOT STARTED")
        bot.polling()
    except Exception as e:
        time.sleep(3)
        print(e)
