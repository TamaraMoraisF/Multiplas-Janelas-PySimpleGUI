import PySimpleGUI as sg


class JogoDeAventura:

    def __init__(self):
        self.escolhaSulOuNorte = 'Você nasceu no norte eu ou no sul?)'
        self.perguntaNorte = 'Você prefere a espada ou escudo?'
        self.perguntaSul = 'Qual é a sua especialidade: linha de frente ou tatico?'
        self.finalHistoriaNorte1 = 'Você será um heroi na linha de frente!'
        self.finalHistoriaNorte2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoriaSul1 = 'Você irá se sacrificar na batalha!'
        self.finalHistoriaSul2 = 'Você não é capaz de lutar nessa batalha!'

    def Janela_finalizar(self, finalDoJogo):
        layout = [
            [sg.Text(finalDoJogo)],
            [sg.Button('sair')],
        ]
        self.janela = sg.Window('Jogo de Aventura!', layout=layout)
        self.LerValores()

    def Janela_executar(self, texto):
        layout = [
            [sg.Text(texto)],
            [sg.Input(size=(25, 0), key='escolha')],
            [sg.Button('Responder'), sg.Button('sair')]
        ]
        self.janela = sg.Window('Jogo de Aventura!', layout=layout)
        self.LerValores()
        self.janela.close()

    def Iniciar(self):
        self.Janela_executar(self.escolhaSulOuNorte)

        while True:
            if self.evento == 'Responder':

                if self.valores['escolha'] == 'norte':
                    self.Janela_executar(self.perguntaNorte)

                    if self.valores['escolha'] == 'espada':
                        self.Janela_finalizar(self.finalHistoriaNorte1)

                    elif self.valores['escolha'] == 'escudo':
                        self.Janela_finalizar(self.finalHistoriaNorte2)

                elif self.valores['escolha'] == 'sul':
                    self.Janela_executar(self.perguntaSul)

                    if self.valores['escolha'] == 'linha de frente':
                        self.Janela_finalizar(self.finalHistoriaSul1)

                    elif self.valores['escolha'] == 'tatico':
                        self.Janela_finalizar(self.finalHistoriaSul2)
                else:
                    self.Janela_finalizar('ERRO, Digite novamente!')
                    self.Janela_executar(self.escolhaSulOuNorte)

            else:
                break

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()


jogo = JogoDeAventura()
jogo.Iniciar()



