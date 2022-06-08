from app.votacao import Votacao
from app.utils import cabecalho, confirmar, input_str, limpar


def main():
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

    votacao = Votacao(candidatos)

    votacao.iniciar()

    limpar()

    votacao.concluir()


if __name__ == '__main__':
    main()
