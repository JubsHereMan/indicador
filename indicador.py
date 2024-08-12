from categoriasFilmes.drama import *
from categoriasFilmes.romance import *
from categoriasFilmes.acao import *
from categoriasFilmes.aventura import * 
from categoriasFilmes.animacao import *

categorias= ['animacao', 'aventura', 'terror', 'acao',' romance','drama']


#funcções
def mostrarCatalogo():
    from categoriasFilmes


print('''Bem vindo ao catalogo de Filmes
      
      1. para iniciar a pesquisa de filmes
      2. entender o objetivo do codigo
    ''')

opcao_escolhida=input('Digite o numero da sua opção:')



if opcao_escolhida == 1:
    mostrarCatalogo()
