import telebot
import config
from random import *
bot = telebot.TeleBot(config.TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/Играть', '1', '2', '3', '4', '5')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard1)

@bot.message_handler(commands=['Играть'])
def start_message(message):
    global i
    bot.send_message(message.chat.id, 'Я загадал число от 1 до 5, напиши его в чат)😘')
    i = str(randint(1, 5))
    print(i)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == i:
            bot.send_message(message.chat.id, 'Оgо ты отгадал. Если хочешь продолжить тыкай на ИГРАТЬ😄')

        elif message.text != i:
            bot.send_message(message.chat.id, 'ТЫ не отгадал. Если хочешь продолжить тыкай на ИГРАТЬ😅')


#git add
#git commit -m ""
#git push -u origin

bot.polling(bot.polling(none_stop=True))