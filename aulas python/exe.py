def coletarNota():
    nota= input().split()
    for i in range(len(nota)):
        nota[i]=float(nota[i])
    return nota

def preencher_turma(qtde_alunos):
    turma= []
    for i in range(qtde_alunos):
        print(f'{i+1}° aluno:', end=' ')
        aluno=coletarNota()
        turma.append((aluno))
    return turma


#def calcular_media(turma):
    media_do_aluno=[]
  #  for i[0] in turma(coletarNota()):
      #  medias= sum(aluno) / len(aluno)
 #       media_do_aluno.append(medias)


def calcular_media(aluno):
    soma=0
    for nota in aluno:
        soma+=nota
    return soma/len(aluno)


def resumo_turma(turma):
    for aluno in turma:
        media=calcular_media(aluno)
        print(f'notas: {aluno}| Média{media}')



#Principal
qtds_aluno=int(input('Quantidade de aluno na turma: '))
turma=preencher_turma(qtds_aluno)
resumo_turma(turma)
