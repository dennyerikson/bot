# coding: utf8
# -*- coding: utf-8 -*-
from chatbot import ChatBot

Bot = ChatBot('Bot')
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'tchau':
        break
