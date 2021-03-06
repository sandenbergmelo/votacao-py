from pathlib import Path
from random import randint

from app.urna import Urna
from app.utils import retornar_data_hora


def test_votar_em_candidatos():
    urna = Urna()

    candidatos = []
    quantidades_de_votos = []

    n_de_candidatos = randint(2, 10)

    for i in range(n_de_candidatos):
        # Gera os nomes dos candidatos
        # e as quantidades de votos de cada um
        candidatos.append(f'Candidato {i}')
        quantidades_de_votos.append(randint(1, 15))

    urna.abrir_votacao(candidatos)

    for candidato in range(len(urna.candidatos)):  # Vota nos candidatos
        for _ in range(quantidades_de_votos[candidato]):
            urna.votar(candidato)

    votos = list(urna.votos.values())

    # Verifica a quantidade de votos de cada um
    resultado = all(voto == quantidades_de_votos[i]
                    for i, voto in enumerate(votos))

    assert resultado


def test_salvar_votos():
    urna = Urna()

    candidatos = []
    quantidades_de_votos = []

    n_de_candidatos = randint(2, 10)

    for i in range(n_de_candidatos):
        # Gera os nomes dos candidatos
        # e as quantidades de votos de cada um
        candidatos.append(f'Candidato {i}')
        quantidades_de_votos.append(randint(1, 15))

    urna.abrir_votacao(candidatos)

    for candidato in range(len(urna.candidatos)):  # Vota nos candidatos
        for _ in range(quantidades_de_votos[candidato]):
            urna.votar(candidato)

    urna.salvar_votos()

    data = retornar_data_hora()
    file = Path(f'Votação {data}.txt')
    resultado = file.is_file()
    file.unlink()

    assert resultado
