from telebot import *
import config # create a python file and write your token in it. For example token = <your token>

bot = TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_command(message):
    sticker = open('stickers/start.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nменя зовут лягушка\
 {1.first_name}.\nЯ - бот, созданный радовать людей".format(message.from_user, bot.get_me()), parse_mode='HTML')


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "{0.first_name},\
 чем могу тебе помочь?".format(message.from_user, bot.get_me()), parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def echo_command(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
