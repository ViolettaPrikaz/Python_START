import telebot
import math

bot = telebot.TeleBot('токет удален') 

def negafib(n):
    if n > 0:
        a, b = 0, 1
        for i in range(n):
            a, b = b - a, a
        return b
    elif n < 0 and n % 2 == 0:
        a, b = 0, 1
        for i in range(abs(n)):
            a, b = b - a, a
        return -b
    elif n < 0 and n % 2 != 0:
        a, b = 0, 1
        for i in range(abs(n)):
            a, b = b - a, a
        return b
    else:
        return 0

def to_binary(n):
    return bin(n)[2:]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Пожалуйста, используйте команду '/negafib n', чтобы получить n-е число Негафибоначчи, команду '/tobinary n', чтобы преобразовать n в двоичный код, или введите математическое выражение для вычисления.")

@bot.message_handler(commands=['negafib'])
def send_negafib(message):
    try:
        n = int(message.text.split()[1])
        result = negafib(n)
        bot.reply_to(message, f"{n} равно {result}")
    except:
        bot.reply_to(message, "Неверный ввод. Пожалуйста, введите число.")

@bot.message_handler(commands=['tobinary'])
def send_binary(message):
    try:
        n = int(message.text.split()[1])
        result = to_binary(n)
        bot.reply_to(message, f"Двоичное представление {n} - это {result}")
    except:
        bot.reply_to(message, "Неверный ввод. Пожалуйста, введите число.")

@bot.message_handler(func=lambda message: True)
def send_result(message):
    if message.text.startswith('/'):
        bot.reply_to(message, "Недопустимая команда. Пожалуйста, используйте команду '/negafib n', чтобы получить n-е число Негафибоначчи, команду '/tobinary n', чтобы преобразовать n в двоичный код, или введите математическое выражение для вычисления.")
    else:
        try:
            result = eval(message.text)
            bot.reply_to(message, f"В результате получается {result}")
        except:
            bot.reply_to(message, "Неверный ввод. Пожалуйста, введите корректное выражение.")

bot.polling()