import telebot
from Tok import keys, Token
from class_1 import ConvertionException, CryptoConverter


bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start', 'help'])
def help (message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следющем формате:\n' \
           'Название валюты \n' \
           'Перевод для ВАС \n' \
           'Нажмите на команду /value'


    bot.reply_to(message, text)

@bot.message_handler(commands=['value'])
def value(message: telebot.types.Message):
    text = 'Посмотрите, доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key))

    bot.reply_to(message, text)
@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        value = message.text.split(' ')

        if len(value) != 3:
            raise ConvertionException('Вы набрали много параметров.')

        quote, base, amount = value
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f' Никак не удается обработать команду\n{e}')
    else:

        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message (message.chat.id, text)


bot.polling()
