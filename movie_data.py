import pandas as pd

def create_movie_data(dataset):
    lista_filmes = []
    for _, item in dataset.iterrows():
        filme = {
            "Titulo": item['name'],
            "Diretor": item['director'],
            "Ano": item['year']
        }
        lista_filmes.append(filme)

    return lista_filmes