#message.text -  получили
#bot.send_message(message.from_user.id, ans) - отправить отправителю
def get_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Здрасте")
    if message.text == "Пока":
        bot.send_message(message.from_user.id, "Аривидерчи")
    if message.text == "Добро пожаловать":
        bot.send_message(message.from_user.id, "Вам здесь не рады")

import telebot

bot = telebot.TeleBot("2085979201:AAH7oHr8j_LmUFJydTJ9G1GnFm9ZE-bgrzU")
bot.message_handler(content_types = ['text'])

bot.polling(none_stop = True, interval = 0)




