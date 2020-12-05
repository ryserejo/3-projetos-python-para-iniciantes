# Simundador de dados
# Gerar valores de 1 até 6
import random

class SimundadorDeDado:
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.gerarValordoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Obrigado pela sua participação!')
            else:
                print('Por favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def gerarValordoDado(self):
        print(random.randint(self.valorMinimo, self.valorMaximo))


simulador = SimundadorDeDado()
simulador.Iniciar()

