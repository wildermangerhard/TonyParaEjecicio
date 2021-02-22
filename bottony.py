from telegram.ext import Updater, CommandHandler

def start(update, context):

     update.message.reply_text('Hoka HUANNO')



if __name__ == '__main__':
    updater = Updater(token='1681250654:AAFEKW1gYf0S5c7ZCqZyu-3zfoHqClV_b30',use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))

    updater.start_polling()
    updater.idle()
