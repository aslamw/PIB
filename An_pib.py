import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as pg
import seaborn as sb

class abertura_pib():
    def __init__(self):
        #guardando dados dos arquivos
        self.tabela_pib = pd.read_csv('matplotlib\dados\conta.csv')
        self.key = self.tabela_pib.keys()
        self.N_paises = self.tabela_pib['Country Name']

        #componentes da janela
        layout = [
            [pg.Text('Digite os nomes dos paises para comparar o PIB')],
            [pg.Input(size=(20,0),key='paises'),pg.Button('Iniciar',)]
            #[pg.Output(size=(60,40))]
        ]
        self.janela = pg.Window('comparação de PIB').layout(layout)

    def start(self):
        while True:
            posicao = []
            self.button, self.value = self.janela.Read()
            self.paises = self.value['paises'].split(',')

            for o in range(len(self.paises)):
                for i in range(len(self.N_paises)): 
                    if self.paises[o] == self.N_paises[i]: posicao.append(i)

            Brasilpip = []
            dados = {}
            for o in range(len(posicao)):
                for i in range(4,len(self.key)): Brasilpip.append(self.tabela_pib[self.key[i]].loc[posicao[o]])

                dados[self.paises[o]] = np.array(Brasilpip)

            print(posicao)
            print(self.paises)
            
            for i in range(len(dados.keys())):
                sb.distplot((dados[self.paises[i]]),hist=False,label=dados.keys())
            plt.show()

jan = abertura_pib()
jan.start()
