import telebot
from convertor import Convertor
TOKEN ="5361461268:AAGV03zKIdK1Yk0-MV7JgkldcKsfDucTm0I"
access_key = "sdfgdrfg"
bot = telebot.TeleBot(TOKEN)

zapros = []
l = 0
quantity = 1

exchanges = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
    'юань': 'CNY',
    'казахский_тенге': 'KZT',
    'белорусский_рубль': 'BYN'
}

@bot.message_handler(commands=["start"])
def function_name(message):
    bot.reply_to(message, "Здравствуйте!\n"
                          "для ознакомления с возможностями бота наберите\n"
                          "комманду '/help'")

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(commands=["help"])
def function_name(message):
    bot.reply_to(message, "Для конвертации валют наберите команду '/values',\n"
                          "из открывшегося списка валют, доступных для конвертации,\n"
                          "наберите валюту из которой хотите конвертировать,\n"
                          "затем через пробел наберите валюту в которую нужно\n"
                          "конвертировать и через пробел сумму конвертации\n"
                          "'1' можно не вводить")

@bot.message_handler(content_types=["text"])
def handlet_text(message):
    s = message.text.strip()

    values = message.text.split(' ')
    j = 0
    quantity = 1
    zapros = []
    z = True
    # удаление лишних пробелов
    for i in range(len(values)):
        if values[i] != '':
            zapros.insert(j, values[i])
            j += 1

    # проверка ввода
    l = len(zapros)
    if 1 < l < 4:   # определение количества введенных значений

        if (zapros[1] in exchanges) and (zapros[0] in exchanges):
            if zapros[0] == zapros[1]:
                bot.reply_to(message, "Введены одинаковые валюты")
            else:
                if l == 3:
                    zapros[2] = zapros[2].replace(',', '.')    # замена запятой на точку в сумме для конвертации
                    z = zapros[2].replace('.', '')  # удаление точки из суммы для конвертации
                    # проверка на наличие символов кроме цифр в сумме
                    if z.isdigit() > 0:
                        quantity = float(zapros[2])

                    else:
                        z = False
                        bot.reply_to(message, f"Не  правильно введено количество валюты {zapros[2]}")
                if z:
                    # запрос курса валют и выдача ответа в бот
                    q = Convertor.price(exchanges.get(zapros[0]), exchanges.get(zapros[1]), quantity, access_key)
                    bot.reply_to(message, f"В {quantity} '{zapros[0]}'  по курсу  {q} '{zapros[1]}'")

        else:
            bot.reply_to(message, "Не правильно введены названия валют")
    else:
        bot.reply_to(message, f"Не  правильно введено количество параметров!   {len(zapros)}")


bot.polling(none_stop=True)
