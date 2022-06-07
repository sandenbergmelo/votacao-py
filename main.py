from app.urna import Urna
from app.utils import menu, confirmar, limpar, sair


def main():
    urna = Urna()
    urna.abrir_votacao('Candidato 0', 'Candidato 1',
                       'Candidato 2', 'Candidato 3')

    if not urna.votacao_aberta:
        sair()

    while True:
        limpar()

        voto = menu('VOTAÇÃO', urna.candidatos)

        urna.votar(voto)

        continuar = confirmar('\nVotar novamente?')

        if not continuar:
            break

    limpar()
    urna.mostrar_votos(formatado=True)

    salvar = confirmar('Salvar votos?')

    if salvar:
        urna.salvar_votos()


if __name__ == '__main__':
    main()
