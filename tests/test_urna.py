import os
from pathlib import Path
from random import randint

from app.urna import Urna
from app.utils import retornar_data_hora


def test_votar_em_candidatos():
    urna = Urna()

    candidatos = []
    quantidades_de_votos = []

    n_de_candidatos = randint(3, 10)

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

    resultado = True

    for i, voto in enumerate(votos):  # Verifica a quantidade de votos de cada um
        resultado = True if voto == quantidades_de_votos[i] else False

    assert resultado


def test_salvar_votos():
    urna = Urna()

    candidatos = []
    quantidades_de_votos = []

    n_de_candidatos = randint(3, 10)

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

    data = retornar_data_hora().replace('/', '-')
    file = Path(f'Votação {data}.txt')
    resultado = file.is_file()
    os.remove(file)

    assert resultado
