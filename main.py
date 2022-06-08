from app.votacao import Votacao


def main():
    votacao = Votacao(Votacao.ler_candidatos())
    votacao.iniciar()
    votacao.concluir()


if __name__ == '__main__':
    main()
