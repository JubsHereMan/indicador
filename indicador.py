import random

from categoriasFilmes.drama import *
from categoriasFilmes.romance import *
from categoriasFilmes.acao import *
from categoriasFilmes.aventura import * 
from categoriasFilmes.animacao import *
from categoriasFilmes.terror import *
from categoriasFilmes.scifi import *

categorias= ['Ficção Científica','Aventura','Drama','Animação','Terror''Romance','Ação','Suspense','Comédia']


listaFilmes=[filmesAcao,filmeTerror, filmesScifi,filmesRomance,filmeDrama,filmesAnimacao,filmesAventura]

#funcções
def matriz_Catalogo(tamanho=3):
    if tamanho != 3:
        raise ValueError('Precisa ser uma matriz de 3x3')
    

    matriz=[]
    for i in range(tamanho):
        linha=[(random.choice(random.choice(listaFilmes)))for i in range(tamanho)]
        for i,filme in enumerate(linha):
            nome= filme['nome']
            categoria=filme['categoria']
            linha[i]={'nome':nome,'categoria':categoria}
        matriz.append(linha)

    return matriz

def obter_filme_valido(matriz):
    while True:
        filme01=input('Digite o nome de um filme da lista')
        filme_encontrado=false 
        for linha in matriz:
            if filme01 in linha:
                filme_encontrado=True
                break
        if filme_encontrado:
            return filme01
        else:
            print('Filme não encontrado, digite um filme valido')


def coletar_filmes_validos(matriz,num_filmes=3)


    filmes_digitados=[]

    for i in range(num_filmes)
    print(f'filme{i+1}:')
    filme= obter_filme_valido(matriz)
    filmes_digitados.append(filme)

    return filmes_digitados


filmes_escolhidos = coletar_filmes_validos(matriz_filmes)

print('filmes escolhidos:')
for filme in filmes_escolhidos:
    print(filme)


print('''Bem vindo ao catalogo de Filmes
      
      1. para iniciar a pesquisa de filmes
      2. entender o objetivo do codigo
    ''')

opcao_escolhida=int(input('Digite o numero da sua opção:'))



if opcao_escolhida == 1:
    print('''Escolha 3 filmes que mais lhe agradam:
          
          
          ''')
    matriz_filmes= matriz_Catalogo()

    for linha in matriz_filmes:
        print(linha)




