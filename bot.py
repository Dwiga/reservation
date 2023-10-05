import telebot
from app.libs.config import telegram_token
from app.services.order_service import approve_order

bot = telebot.TeleBot(telegram_token())


@bot.message_handler(commands=['approve'])
def send_welcome(message):
    transaction_id = message.text.split(" ")[1]
    approve_order(transaction_id)
    bot.reply_to(message, "{} is approved".format(transaction_id))


bot.infinity_polling()
