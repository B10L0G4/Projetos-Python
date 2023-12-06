#Simulador de dados 
''' Simular o play de um dado, gerando um valor de 1 até 6  '''

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self): #initi define configurações iniciais 
        self.valor_minimo = 1 
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado ?'
    #Layout 
        self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
    def Iniciar(self): 
        #Criar uma janela 
        self.janela = sg.Window('Simulador de dados', layout = self.layout)
        #ler os valores da tela 
        self.eventos, self.valores = self.janela.Read()
        #fazer alguma com os valores 
        try: 
            if self.eventos == 'sim'or self.eventos =='s':
                self.GerarvalordoDado()
            elif self.eventos == 'não' or self.eventos =='n':
                print('Agradecemos a participação')
            else:
                print('Digite sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarvalordoDado(self): 
        print(random.randint(self.valor_minimo, self.valor_maximo))

simuladoe = SimuladorDeDado()
simuladoe.Iniciar()

