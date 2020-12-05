# Simundador de dados
# Gerar valores de 1 até 6
import random
import PySimpleGUI as sg


class SimundadorDeDado:
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        # Criar janela
        self.janela = sg.Window('Simulador de dados', self.layout)
        #Ler dados 
        self.eventos, self.valore = self.janela.Read()

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.gerarValordoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Obrigado pela sua participação!')
            else:
                print('Por favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def gerarValordoDado(self):
        print(random.randint(self.valorMinimo, self.valorMaximo))


simulador = SimundadorDeDado()
simulador.Iniciar()
