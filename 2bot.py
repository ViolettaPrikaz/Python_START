import telebot
import csv

bot = telebot.TeleBot('токет удален') 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я помогу вам найти номер телефона пользователя. Пожалуйста, введите имя пользователя: Olga, Dmitry, Natalia, Vio")

@bot.message_handler(func=lambda message: True)
def send_info(message):
    name = message.text
    with open('users.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                bot.reply_to(message, f"Номер телефона для {name}: {row[1]}")
                break
        else:
            bot.reply_to(message, f"Информация о {name} не найдена")

bot.polling()