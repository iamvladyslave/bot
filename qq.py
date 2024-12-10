import telebot

bot = telebot.TeleBot('8116893983:AAHTiHpIw5JP6RkYDYr6_10XBt07tSfr4W4')


@bot.message_handler(commands=['start'])
def start():
    bot.send_message(message.chat.id, 'Hi! Nice ti see you! Tell me: where aue u from?')



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()


bot.polling(non_stop=True)



