from time import sleep

from .urna import Urna
from .utils import *


class Votacao:

    def __init__(self, *candidatos) -> None:
        self.urna = Urna()
        self.candidatos = candidatos

        if (len(candidatos) > 0
            and (isinstance(candidatos[0], list) or
                 isinstance(candidatos[0], tuple))):
            self.candidatos = candidatos[0]

    @staticmethod
    def ler_candidatos() -> list:
        cabecalho('Votação')

        candidatos = []
        c = 0

        while True:
            candidato = input_str(f'Digite o nome do candidato {c}: ').title()

            candidatos.append(candidato)

            continuar = confirmar('Cadastrar outro candidato?')
            print()
            c += 1

            if not continuar:
                break

        limpar()
        return candidatos

    def iniciar(self):
        self.urna.abrir_votacao(self.candidatos)

        if not self.urna.votacao_aberta:
            sair()

        while True:

            voto = menu('VOTAÇÃO', self.urna.candidatos)

            self.urna.votar(voto)

            continuar = confirmar('\nVotar novamente?')

            limpar()
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
