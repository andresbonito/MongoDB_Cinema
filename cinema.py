from pymongo import MongoClient
import pandas as pd
from movie_data import create_movie_data

# Configurações
MONGO_URL = "PORTA"
DB_NAME = "DATABASE_NAME"
COLLECTION_NAME = "COLLECTION_NAME"
CSV_FILE = 'movies.csv'

with MongoClient(MONGO_URL) as cliente:
    banco = cliente[DB_NAME]
    colecao = banco[COLLECTION_NAME]

    try:
        df = pd.read_csv(CSV_FILE)
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        exit(1)

    new_df = df[['name', 'year', 'director']]
    dados_filmes = create_movie_data(new_df)

    filmes_para_inserir = []
    for filme in dados_filmes:
        if 'Titulo' in filme and 'Diretor' in filme and 'Ano' in filme:
            filme_database = {
                'Titulo': filme['Titulo'],
                'Diretor': filme['Diretor'],
                'Ano': filme['Ano']
            }
            filmes_para_inserir.append(filme_database)
        else:
            print(f"Filme com dados inválidos: {filme}")

    if filmes_para_inserir:
        colecao.insert_many(filmes_para_inserir)

    print("\nFilmes cadastrados:")
    for f in colecao.find().limit(10):  # Limitar a quantidade de filmes exibidos
        print(f"{f['Titulo']} ({f['Ano']}) - Direção: {f['Diretor']}")
