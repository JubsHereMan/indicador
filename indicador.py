import random

from categoriasFilmes.drama import *
from categoriasFilmes.romance import *
from categoriasFilmes.acao import *
from categoriasFilmes.aventura import * 
from categoriasFilmes.animacao import *
from categoriasFilmes.terror import *
from categoriasFilmes.scifi import *

categorias = ['Ficção Científica', 'Aventura', 'Drama', 'Animação', 'Terror', 'Romance', 'Ação', 'Suspense', 'Comédia']

listaFilmes = [filmesAcao, filmeTerror, filmesScifi, filmesRomance, filmeDrama, filmesAnimacao, filmesAventura]


def matriz_Catalogo(tamanho=3):
    if tamanho != 3:
        raise ValueError('Precisa ser uma matriz de 3x3')

    matriz = []
    for i in range(tamanho):
        linha = [(random.choice(random.choice(listaFilmes))) for _ in range(tamanho)]
        for j, filme in enumerate(linha):
            nome = filme['nome']
            categoria = filme['categoria']
            linha[j] = {'nome': nome, 'categoria': categoria}
        matriz.append(linha)

    return matriz

def obter_filme_valido(matriz):
    while True:
        filme01 = input('Digite o nome de um filme da lista: ')
        filme_encontrado = False
        for linha in matriz:
            for filme in linha:
                if filme01 == filme['nome']:
                    filme_encontrado = True
                    break
            if filme_encontrado:
                break
        
        if filme_encontrado:
            return filme01
        else:
            print('Filme não encontrado. Por favor, digite um filme válido.')

def coletar_filmes_validos(matriz, num_filmes=3):
    filmes_digitados = []

    for i in range(num_filmes):
        print(f'Filme {i+1}:')
        filme = obter_filme_valido(matriz)
        filmes_digitados.append(filme)

    return filmes_digitados

print('''Bem vindo ao catálogo de Filmes
      
      1. para iniciar a pesquisa de filmes
      2. entender o objetivo do código
    ''')

opcao_escolhida = int(input('Digite o número da sua opção: '))

if opcao_escolhida == 1:
    print('''Escolha 3 filmes que mais lhe agradam:
          
          ''')
    matriz_filmes = matriz_Catalogo()

    for linha in matriz_filmes:
        print(linha)

    filmes_escolhidos = coletar_filmes_validos(matriz_filmes)

    print('Filmes escolhidos:')
    for filme in filmes_escolhidos:
        print(filme)

elif opcao_escolhida == 2:
    print('O objetivo do código é gerar um catálogo aleatório de filmes e permitir que você escolha seus filmes favoritos a partir desse catálogo.')
