import telebot     
import logging
from telebot import types
### ^ Import libraries ^
bot = telebot.TeleBot("5843870161:AAG8clSucD4H5tWVy7hVIo3y9j4kKJuuSZY")
logger = telebot.logger 
### ^ Fundamentals ^
telebot.logger.setLevel(logging.DEBUG)
### ^ Logging ^
@bot.message_handler(commands=['start'])
def greeting(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_btn = types.KeyboardButton("🌿Информация")
    ivents_btn = types.KeyboardButton("♻Мероприятия")
    report_btn = types.KeyboardButton("🌳Жалоба")
    markup.add(info_btn, ivents_btn, report_btn)
    bot.reply_to(message, "Здравствуйте👋! Это экологический вестник города Гуково! \n━━━━━━━━━━━━━\nЗдесь можно:\n • Получить актуальную информацию об экологических показателях\n • Узнать о экологических мероприятиях\n • Оставить жалобу о экологических проблемах(несанкционированные свалки и т.д)", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def getting_msg(message):
    if message.text == "🌿Информация":
        bot.reply_to(message, "•Воздух•:\nВзвешенные вещества: выше нормы! 3,5ПДК\nОксид углерода: выше нормы! 1,3ПДК")
    elif message.text == "♻Мероприятия":
        bot.reply_to(message, "01.31.2023 07:00 - 'Долой мусор'")
    elif message.text == "🌳Жалоба":
        bot.reply_to(message, "Опишите вашу проблему:\nУкажите адрес\nДату\nПроблему")
bot.infinity_polling()
