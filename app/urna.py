from operator import itemgetter
from time import sleep
from rich import print

from app.utils import cabecalho, retornar_data_hora


class Urna:

    def __init__(self) -> None:
        self.candidatos = []
        self.votos = {}
        self.votacao_aberta = False

    def abrir_votacao(self, *candidatos: tuple):
        if (len(candidatos) >= 1
            and (isinstance(candidatos[0], tuple)
                 or isinstance(candidatos[0], list))):
            candidatos = candidatos[0]

        for candidato in candidatos:
            self.candidatos.append(candidato)
            self.votos[candidato] = 0

        if len(self.candidatos) == 0:
            print('Sem candidatos para abrir votação')
            self.votacao_aberta = False
            return

        if len(self.candidatos) == 1:
            print('Não é possível abrir votação com apenas 1 candidato')
            self.votacao_aberta = False
            return

        self.votacao_aberta = True

    def votar(self, voto):
        try:
            self.votos[self.candidatos[voto]] += 1
            print(
                f'Voto em [blue]{self.candidatos[voto]}[/] [green]Confirmado![/]')
        except Exception as erro:
            print('[red]ERRO: [/]')
            print(erro.__class__)

    def listar_candidatos(self):
        cabecalho('LISTA DE CANDIDATOS')

        if len(self.candidatos) == 0:
            print('Sem candidatos para mostrar')
            return
        for candidato in self.candidatos:
            print(candidato)

    def mostrar_votos(self, candidato=-1, formatado=False):
        if candidato == -1:
            if not formatado:
                print(self.votos)
                return

            resultado = sorted(self.votos.items(),
                               key=itemgetter(1), reverse=True)

            cabecalho('Total de votos')
            for i, value in enumerate(resultado):
                print(f'{i+1}º {value[0]}: {value[1]} votos')
                sleep(1)
            return

        candidato = self.candidatos[candidato]
        print(
            f'O Candidato [blue]{candidato}[/] tem {self.votos[candidato]} votos')

    def salvar_votos(self):
        try:
            data = retornar_data_hora()
            resultado = sorted(self.votos.items(),
                               key=itemgetter(1), reverse=True)

            with open(f'Votação {data}.txt', 'w') as votacao:
                for value in resultado:
                    votacao.write(f'{value[0]};{value[1]}\n')

            print('Votação salva com [bold][green]Sucesso[/][/]')

        except Exception as erro:
            print('[red]ERRO[/] ao salvar votação')
            print(erro.__class__)
