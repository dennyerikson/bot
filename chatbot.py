import json
import sys
import os
import subprocess as s
from print_vg import sala_13, sala_14, sala_15, sala_17, sala_23
#783162685:AAEtd_uP2bRQNmMQCeh9n0EyvERKd1TI684
#FatVgbot

class ChatBot():
    def __init__(self, nome):
        try:
            memoria = open(nome + '.json', 'r')
        except FileNotFoundError:
            memoria = open(nome + '.json', 'w')
            memoria.write('[["denny"], {"oi": "Olá, qual seu nome?", "tchau": "Tchau tachau"}]')
            memoria.close()
            memoria = open(nome+'.json','r')

        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None,]


    def escuta(self, frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        frase = frase.lower()
        frase = frase.replace('é', 'eh')
        return frase

    def pensa(self, frase):

        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprende':
            return 'Digite a frase: '

        # responde frases que dependem do histórico
        ultimaFrase = self.historico[-1]
        if ultimaFrase == 'Olá, qual seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase

        if ultimaFrase == 'Digite a frase: ':
            self.chave = frase
            return 'Digite a resposta: '

        if ultimaFrase == 'Digite a resposta: ':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Aprendido'

        try:
            #parei no eval
            resp = str(eval(frase))
            return resp
        except:
            pass
        if frase == 'print13':
            sala_13()
            return '13-Imprimindo..'

        if frase == 'print14':
            sala_14()
            return '14-Imprimindo..'

        if frase == 'print15':
            sala_15()
            return '15-Imprimindo..'

        if frase == 'print17':
            sala_17()
            return '17-Imprimindo..'

        if frase == 'print23':
            sala_23()
            return '23-Imprimindo..'

        return 'Não entendi'

    def pegaNome(self, nome):
        if 'o meu nome eh ' in nome:
            nome = nome[14:]
        return nome

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Eaew '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            self.gravaMemoria()

        nome = nome.title()
        return frase + nome
    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()

    def fala(self, frase):

        if 'executa' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')
            if 'win' in plataforma:
                os.startfile(comando)
            if 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError:
                    s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)

