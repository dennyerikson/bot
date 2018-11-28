import telepot
from chatbot import ChatBot

telegram = telepot.Bot("783162685:AAEtd_uP2bRQNmMQCeh9n0EyvERKd1TI684")

bot = ChatBot("VgBot")

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)

telegram.message_loop(recebendoMsg)

while True:
    pass
