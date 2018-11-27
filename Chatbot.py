import json
class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome + '.json', 'r')
        except FileNotFoundError:
            memoria = open(nome + '.json', 'w')
            memoria.write('["denny"]')
            memoria.close()
            memoria = open(nome+'.json','r')

        self.nome = nome
        self.conhecidos = json.load(memoria)
        memoria.close()
        self.historico = []
        self.frases = {'oi': 'Olá, qual seu nome', 'tchau': 'Tchau tachau'}

    def escuta(self):
        frase = input('>: ')
        frase = frase.lower()
        frase = frase.replace('é', 'eh')
        return frase

    def pensa(self, frase):

        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprende':
            chave = input('Digite a frase: ')
            resp = input('Digite a resposta: ')
            self.frases[chave] = resp
            return 'Aprendido'

        if self.historico[-1] == 'Olá, qual seu nome?':
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        try:
            #parei no eval
            resp = eval(frase)
            return resp
        except:
            pass

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
            memoria = open(self.nome+'.json', 'w')
            json.dump(self.conhecidos, memoria)
            memoria.close()

        nome = nome.title()
        return frase + nome

    def fala(self, frase):
        print(frase)
        self.historico.append(frase)

