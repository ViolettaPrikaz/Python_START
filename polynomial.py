import telebot

bot = telebot.TeleBot('токет удален') 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я помогу вам сложить два многочлена вида ax^2 + bx + c. Пожалуйста, введите коэффициенты первого многочлена (через запятую):")

@bot.message_handler(func=lambda message: True)
def send_second_poly(message):
    try:
        a, b, c = map(int, message.text.split(','))
        bot.reply_to(message, "Введите коэффициенты второго многочлена (через запятую):")
        bot.register_next_step_handler(message, lambda m: send_result(m, a, b, c))
    except:
        bot.reply_to(message, "Неверный формат. Пожалуйста, введите коэффициенты в формате 'a,b,c'")

def send_result(message, a, b, c):
    try:
        d, e, f = map(int, message.text.split(','))
        res_a = a + d
        res_b = b + e
        res_c = c + f
        result = f"{res_a}x^2 + {res_b}x + {res_c}"
        bot.reply_to(message, f"Результат сложения двух многочленов: {result}")
    except:
        bot.reply_to(message, "Неверный формат. Пожалуйста, введите коэффициенты в формате 'a,b,c'")

bot.polling()