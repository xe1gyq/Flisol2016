import time

import pyupm_grove as grove
#import pyupm_i2clcd as lcd

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

temperatura = grove.GroveTemp(0)
luz = grove.GroveLight(1)
#display = lcd.Jhd1313m1(0, 0x3E, 0x62)

def funcionTemperatura(bot, update):
    grados = temperatura.value()
    bot.sendMessage(update.message.chat_id, text='Temperatura ' + str(grados))

def funcionEcho(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

if __name__ == '__main__':

    updater = Updater("209701132:AAEBn3_8ZBN-Lk8l8kRnkLKegmjA-S5iPeQ")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("temperatura", funcionTemperatura))
    dp.add_handler(MessageHandler([Filters.text], funcionEcho))

    updater.start_polling()
    updater.idle()

'''
while True:

    grados = temperatura.value()
    luxes = luz.value()

    display.setColor(255, 0, 0)

    display.setCursor(0,0)
    display.write('Temperatura ' + str(grados))

    display.setCursor(1,0)
    display.write('Luz ' + str(luxes))

    time.sleep(5)
'''
del temperatura
