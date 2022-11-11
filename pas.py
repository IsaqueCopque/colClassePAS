import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random

#Variáveis globais
s = "T1H1"   #vértice qualquer
cor = 0
classe = [[s]] #Classe[cor] <- s 
Y = None
demanda = []
#-----------------
def start_grafo():
    """
    Forma o grafo de entrada do algoritmo.
    """
    horariosT = [(1,[1,2]),(2,[1,2]),(3,[3])] #(turma,[horarios])
    G = nx.Graph()
    
    for h1 in horariosT: 
        for horario in h1[1]: #adiciona vértices
            G.add_node('T%dH%d'%(h1[0],horario))
        for h2 in horariosT:
            if h1 is not h2: #não comparar com a mesma turma
                qtHorarios = min(len(h1[1]),len(h2[1])) #menor quantidade de horarios
                if qtHorarios == len(h1[1]):
                    for i in range(qtHorarios): #adiciona arestas
                        if h1[1][i] in h2[1]: # se compartilha do mesmo horário
                            G.add_edge('T%dH%d'%(h1[0],h1[1][i]),'T%dH%d'%(h2[0],h1[1][i]))
                else:
                    for i in range(qtHorarios): #adiciona arestas
                        if h2[1][i] in h1[1]: # se compartilha do mesmo horário
                            G.add_edge('T%dH%d'%(h2[0],h2[1][i]),'T%dH%d'%(h1[0],h2[1][i]))
    
    global Y
    Y = list(G.nodes)
    Y.pop(Y.index(s)) #Y = V - {s}
    return G

def random_cor(tam):
    """
    Gera uma vetor de cores em hexadecimal aleatório para pintar os vértices.
    """
    cores = []
    for c in range(tam):
        cores.append("#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]))
    return cores

def colorir():
    """
    Colore o grafo.
    """
    vertices = list(G.nodes)
    corMap =[0]*len(vertices)
    cores = random_cor(len(vertices))
    for corI, cor in enumerate(classe):
        for v in (cor):
            corMap[vertices.index(v)] = cores[corI]   
    return corMap

def plotar_grafo():
    """
    Plota o grafo.
    """
    corMap = colorir()
    nx.draw(G,with_labels=True,font_weight="bold", alpha=0.8, node_color= corMap)
    # plt.tight_layout()
    plt.show()

def mostrar_tabela():
    """
    Exibe uma tabela com os vértices das cores.
    """
    print("=====Resultado do Col_Classe_Pas=====")
    vertices = []
    for cor in classe:
        nomeVertices = ""
        for v in cor:
            nomeVertices+= v+" "
        vertices.append(nomeVertices)
    df = pd.DataFrame(
        data = vertices,
        index=list(i for i in range (1,len(classe)+1)),
        columns=["Vértices"])
    df.index.name = "Cor"
    print(df)
    print("=====================================")

#-------Algoritmo Col_Classe_PAS--------
G = start_grafo()

while len(Y): #While Y != Vazio

    if cor > len(classe)-1: #posições ainda vazias de classe, criar cor
        classe.append([])

    YintersecVdeG = [v for v in list(G.nodes) if v in Y]
    for v in YintersecVdeG:
        N_v = list(G.adj[v]) #vizinhança de v
        adjacente = False
        for v_cor in classe[cor]:
            if v_cor in N_v:
                adjacente = True
                break
        if not adjacente: #classe[cor] ñ adjacente a v (FALTA VERIFICAR A DEMANDA)
            classe[cor].append(v)
            Y.pop(Y.index(v)) #Y = V - {v}
    cor = cor+1

mostrar_tabela()
plotar_grafo()