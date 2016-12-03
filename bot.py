from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater("301341289:AAHFtMhf0cudzz3rGI_XN6IXMQcJATctRqc")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me)) #Фильтруем по типу текст и отвечаем
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
    print(update.message)

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, update.message.text)

def show_error (bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))

if __name__ == '__main__':
    main()