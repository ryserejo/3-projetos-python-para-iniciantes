import random

class Chute:
    def __init__(self):
        self.valorMinimo = 0
        self.valorMaximo = 10
        self.mensagem = 'Adivinhe o número'
        self.achou = False
        self.numeroGerado = self.genNunber()
        self.pontos = 10
    
    def Iniciar(self):
        print(self.mensagem)

        while self.achou == False:
            try:
                resposta = int(input('Qual é o número? '))
            except:
                print('Insira apenas números')
            try:
                if resposta == self.numeroGerado:
                    print('Parabéns!' + ' ' + 'Você fez: ', self.pontos, ' Pontos')
                    self.achou = True
                    pass

                elif resposta > self.numeroGerado:
                    print('Opa! o número é menor.')
                    self.pontos = self.pontos - 1
                    pass

                elif resposta < self.numeroGerado:
                    print('Opa! o número é maior')
                    self.pontos = self.pontos - 1
                else:
                    print('Tente de novo')
                    self.pontos = self.pontos - 1
            except:
                print('Ocorreu um erro')
    def genNunber(self):
        return random.randint(self.valorMinimo, self.valorMaximo)


chuteOnumero = Chute()
chuteOnumero.Iniciar()