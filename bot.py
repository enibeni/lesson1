from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from yandex_translate import YandexTranslate
import telegram
import ephem
import datetime



def main():
    updater = Updater("301341289:AAHFtMhf0cudzz3rGI_XN6IXMQcJATctRqc")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", count_words))
    dp.add_handler(CommandHandler("calc", calc_me))
    dp.add_handler(CommandHandler("moon", moon_status))
    dp.add_handler(MessageHandler([Filters.text], translate_input))  # Фильтруем по типу текст и отвечаем

    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()


def moon_status(bot, update):
    # print(ephem.next_full_moon('2016/10/01'))
    print('0')
    now = datetime.datetime.now()
    print('1')
    date = str(now.year) + '/' + str(now.month) + '/' + str(now.day)
    print('2')
    print(date)
    text = update.message.text
    print(text)
    if 'полнолуние' in text or 'Полнолуние' in text:
        bot.sendMessage(update.message.chat_id, 'Следующее полнолуние будет ' + str(ephem.next_full_moon(date)))
    elif 'растущая' in text or 'Растущая' in text:
        bot.sendMessage(update.message.chat_id, 'Растущая луна будет ' + str(ephem.next_new_moon(date)))



def calc_me(bot, update):
    custom_keyboard = [['1', '2', '3', '*'], ['4', '5', '6', '/'],
                       ['7', '8', '9', '-'], ['0', '.', '=', '+']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    # bot.sendMessage(chat_id=update.message.chat_id, text = "Custom Keyboard Test", reply_markup = reply_markup)
    text = update.message.text

    numbers = {"один": "1",
               "два": "2",
               "три": "3",
               "четыре": "4",
               "пять": "5",
               "шесть": "6",
               "семь": "7",
               "восемь": "8",
               "девять": "9"}

    # digits = dict([(v, k) for k, v in numbers.items()])  ВЖУХ! И словарь наоборот

    text = text.strip('=')[6:]
    # if ' ' in text:
    #     bot.sendMessage(update.message.chat_id, "избавься от пробелов!")
    #     return
    text = text.split
    try:
        print(text)
        if 'плюс' in text:
            # elems = text.split("+")
            result = float(numbers[text[0]]) + float(numbers[text[2]])
        elif 'минус' in text:
            # elems = text.split("-")
            result = float(numbers[text[0]]) - float(numbers[text[2]])
        elif 'умножить' in text:
            # elems = text.split("*")
            result = float(numbers[text[0]]) * float(numbers[text[2]])
        elif 'делить' in text:
            # elems = text.split("/")
            try:
                result = float(numbers[text[0]]) / float(numbers[text[2]])
            except ZeroDivisionError:
                bot.sendMessage(update.message.chat_id, "деление на ноль!")
                return
    except ValueError:
        bot.sendMessage(update.message.chat_id, "кривая запись!")
        return
    bot.sendMessage(update.message.chat_id, result)


def translate_input(bot, update):
    translate = YandexTranslate("trnsl.1.1.20161209T191544Z.6fdaae21be5d22b1."
                                "d9d87f06d7421d83fe7dcbbd0896d0a946e31f17")
    result = translate.translate(update.message.text, lang="en")
    bot.sendMessage(update.message.chat_id, result['text'])


def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
    print(update.message)


def count_words(bot, update):
    print("я внутри!")
    text = update.message.text
    print(text)
    if "\'" in text or text == ' ':
        bot.sendMessage(update.message.chat_id, "Невалидный ввод!")
    else:
        words = text.split(' ')
        words.remove('/wordcount')
        print(words)
        bot.sendMessage(update.message.chat_id, "я вас всех посчитаю! " + str(len(words)))


def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, update.message.text)


def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))


if __name__ == '__main__':
    main()
