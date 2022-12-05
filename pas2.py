import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random

H = [] #horarios
S = [] #capacidade das salas
salasDisponiveis = []
T = [] #tamanhos das turmas

def get_dados():
    """
    Entrada de dados
    """
    #Entrada turmas
    qtTurmas = int( input('Informe a quantidade de turmas: '))
    if qtTurmas <= 0:
        print("Quantidade inválida de turmas")
        return
    #Entrada horarios
    for i in range(1,qtTurmas+1):
        qtHorarios = int( input('Informe a quantidade de horarios da turma %d: '%i))
        if(qtHorarios < 0):
            print("Quantidade inválida de horarios")
            return
        horariosI = []
        print('Informe os %d horarios da turma %d'%(qtHorarios,i))
        for j in range (0, qtHorarios):
            horariosI.append( input('H%d: '%(j+1)) )
        H.append(horariosI)
        #Entrada tamanho da turma
        tam = int( input('Informe o tamanho da turma %d: '%(j+1)))
        if tam <= 0:
            print("Tamanho de turma inválido")
            return
        T.append(tam)
    #Entrada tamanho das salas
    qtSalas = int(input('Informe a quantidade de salas: '))
    for i in range(0, qtSalas):
        tam = int( input('Informe a capacidade da sala %d: '%(i+1)) )
        if tam <= 0:
            print("Capacidade inválida")
            return
        S.append(tam)
        salasDisponiveis.append(i)

def menor_disponivel(tam):
    """
    Retorna a menor sala disponível com tamanho suficiente
    """
    menorT = S[salasDisponiveis[0]]
    for i in salasDisponiveis:
        if S[i] < menorT and S[i] >= tam:
            menorT = S[i]
    if menorT < tam:
        print("Não existe sala disponível para a capacidade %d"%tam)
        return -1
    return menorT

get_dados()

#-----Algoritmo----------------


"""

3
2
1
2
25
2
1
2
30
1
1
10
4
62
31
25
10

"""