


import random 
from collections import Counter 


from categoriasFilmes.drama import * #importando os dados dos filmes
from categoriasFilmes.romance import * #importando os dados dos filmes
from categoriasFilmes.acao import * #importando os dados dos filmes
from categoriasFilmes.aventura import * #importando os dados dos filmes
from categoriasFilmes.animacao import * #importando os dados dos filmes
from categoriasFilmes.terror import * #importando os dados dos filmes
from categoriasFilmes.scifi import * #importando os dados dos filmes





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
                    return filme
            if filme_encontrado:
                break

        if not filme_encontrado:
            print('Filme não encontrado. Por favor, digite um filme válido.')



def coletar_filmes_validos(matriz, num_filmes=3):
    filmes_digitados = []

    for i in range(num_filmes):
        print(f'Filme {i + 1}:')
        filme = obter_filme_valido(matriz)
        filmes_digitados.append(filme)

    return filmes_digitados



def contar_categorias(filmes_escolhidos):
    contagem_categorias = Counter()

    for filme in filmes_escolhidos:
        for categoria in filme['categoria']:
            contagem_categorias[categoria] += 1

    return contagem_categorias



def categoria_preferida(contagem_categorias):
    categoria_mais_preferida = contagem_categorias.most_common(1)[0]
    return categoria_mais_preferida



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

    print('Filmes escolhidos e suas categorias:')
    for filme in filmes_escolhidos:
        print(f"Filme: {filme['nome']}, Categoria(s): {', '.join(filme['categoria'])}")


    contagem_categorias = contar_categorias(filmes_escolhidos)


    categoria_mais_preferida, quantidade = categoria_preferida(contagem_categorias)
    print(f"\nCategoria mais preferida: {categoria_mais_preferida} (Escolhida {quantidade} vezes)")

elif opcao_escolhida == 2:
    print(
        'O objetivo do código é gerar um catálogo aleatório de filmes e permitir que você escolha seus filmes favoritos a partir desse catálogo.')
