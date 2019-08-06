import telebot
from db import set_state, get_state
import os
from flask import Flask, request

API_TOKEN = os.getenv('TG_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)


# -------------------------------Команды------------------------------------

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(chat_id=message.chat.id, text=f'Guten Morgen, {message.chat.first_name}')
    bot.send_message(chat_id=message.chat.id, text=f'We have questions, and we need answers!')
    bot.send_message(chat_id=message.chat.id, text=f'First question: what is your name?')

    set_state(message.chat.id, 0)


@bot.message_handler(func=lambda message: get_state(message.chat.id) == 0)
def echo_message(message):
        bot.send_message(chat_id=message.chat.id, text=f'Of course we already know your name, {message.chat.first_name}')
        bot.send_message(chat_id=message.chat.id, text=f'Second question: what color is sky ')
        set_state(message.chat.id, 1)

        ##DSDSDFFSDDSF

    # bot.reply_to(message, str(len(message.text.split())))
        #bot.send_message(chat_id=message.chat.id, text=f'FALSE, /restart to continue')


@bot.message_handler(func=lambda message: get_state(message.chat.id) == 1)
def send_1(message):
    if message.text == 'blue':
        bot.send_message(chat_id=message.chat.id, text=f'Well job, well job')
        bot.send_message(chat_id=message.chat.id, text=f'third question: What color is grass')
        set_state(message.chat.id, 2)


@bot.message_handler(func=lambda message: get_state(message.chat.id) == 2)
def send_2(message):
    if message.text == 'green':
        bot.send_message(chat_id=message.chat.id, text=f'Final question: What color is glass')
        set_state(message.chat.id, 3)


@bot.message_handler(func=lambda message: get_state(message.chat.id) == 3)
def send_f(message):
    if message.text == 'white':
        bot.send_message(chat_id=message.chat.id, text=f'You are the smartest man in this conversation, inded(after me of course)')
        bot.send_message(chat_id=message.chat.id, text=f'/restart to start this thing all over again')
        set_state(message.chat.id, -1)


@bot.message_handler(func=lambda message: get_state(message.chat.id) == -1)
def send_re(message):
        bot.send_message(chat_id=message.chat.id,
                         text=f'--------------Restarted-------------, ')
        bot.send_message(chat_id=message.chat.id, text=f'Guten Morgen, {message.chat.first_name}')
        bot.send_message(chat_id=message.chat.id, text=f'We have questions, and we need answers!')
        bot.send_message(chat_id=message.chat.id, text=f'First question: what is your name?')
        set_state(message.chat.id, 0)


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#	bot.reply_to(message, str(len(message.text.split())))

# ----------------------------------------------------------------------------

@server.route('/'+API_TOKEN, methods=['POST'])
def get_message():
    json_update = request.stream.read().decode('utf-8')
    update = telebot.types.Update.de_json(json_update)

    bot.process_new_updates([update])
    return '', 200
