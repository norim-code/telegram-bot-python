import telebot

bot = telebot.TeleBot("5843870161:AAG8clSucD4H5tWVy7hVIo3y9j4kKJuuSZY")

@bot.message_handler(commands=['start', 'help'])
def greeting(message):
    bot.reply_to(message, "Hello! It's a test!")
bot.infinity_polling()
