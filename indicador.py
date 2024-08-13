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

filme01=input('Filme 1:')

for linha in  matriz_filmes:
    filmeInline =
    if filme01 != {matriz_filmes}

filme02=input('filme 2:')


filme03=input('filme 3:')
print(f'Os filmes escolhidos foram:{filme01}, {filme02}, {filme03}')





