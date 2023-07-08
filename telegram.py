# ---------------------------------------------------------------------
# using the python api
# ---------------------------------------------------------------------

# import telebot

# def send_message(bot, chat_id, text):
#     bot.send_message(chat_id, text)

# if __name__ == "__main__":
#     bot = telebot.TeleBot("")
#     chat_id = ''
#     text = "This is a test message."
#     send_message(bot, chat_id, text)


# ---------------------------------------------------------------------
# using the official telegram api
# ---------------------------------------------------------------------

# import requests
# import json

# class TelegramAPI:
#     def __init__(self, token):
#         self.token = token
#         self.base_url = f"https://api.telegram.org/bot{token}/"

#     def send_message(self, chat_id, text):
#         url = self.base_url + "sendMessage"
#         params = {
#             "chat_id": chat_id,
#             "text": text
#         }
#         response = requests.get(url, params=params)
#         # Handle the response and any errors here

#     # Add other methods for interacting with the Telegram API

# def read_credentials(filename):
#     with open(filename, 'r') as file:
#         data = json.load(file)
#         token = data['token']
#         chat_id = data['chat_id']
#     return token, chat_id


# def main():
#     token, chat_id = read_credentials('/home/pranav125/Desktop/mycroft-core/skills/birthday-skill/credentials/telegramcreds.json')
#     api = TelegramAPI(token)
#     text = "Message"
#     api.send_message(chat_id, text)

# if __name__ == "__main__":
#     main()