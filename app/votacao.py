from time import sleep

from app.urna import Urna
from app.utils import sair, limpar, menu, confirmar


class Votacao:

    def __init__(self, *candidatos) -> None:
        self.urna = Urna()
        self.candidatos = candidatos

        if (len(candidatos) > 0
            and (isinstance(candidatos[0], list) or
                 isinstance(candidatos[0], tuple))):
            self.candidatos = candidatos[0]

    def iniciar(self):
        self.urna.abrir_votacao(self.candidatos)

        if not self.urna.votacao_aberta:
            sair()

        while True:
            limpar()

            voto = menu('VOTAÇÃO', self.urna.candidatos)

            self.urna.votar(voto)

            continuar = confirmar('\nVotar novamente?')

            if not continuar:
                break

    def concluir(self):
        while True:
            opc = menu('Selecione uma opção: ',
                       ['Listar candidatos',
                        'Mostrar votos',
                        'Mostrar votos (detalhado)',
                        'Salvar votação',
                        'Sair do sistema'])

            limpar()

            if opc == 0:
                self.urna.listar_candidatos()
            elif opc == 1:
                print('Votos: ')
                self.urna.mostrar_votos()
            elif opc == 2:
                self.urna.mostrar_votos(formatado=True)
            elif opc == 3:
                self.urna.salvar_votos()
            elif opc == 4:
                break

            sleep(1)
        sair()
