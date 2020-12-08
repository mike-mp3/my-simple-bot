import telebot
import config
from random import *
bot = telebot.TeleBot(config.TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/Киньмонетку')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard1)


@bot.message_handler(commands=['Киньмонетку'])
def start_message(message):
    i = randint(1, 2)
    print(i)
    if i == 1:
        bot.send_message(message.chat.id, 'Так...\n Решка')
    else:
        bot.send_message(message.chat.id, 'Так...\n Орел')






#git add
#git commit -m ""
#git push -u origin

bot.polling(bot.polling(none_stop=True))