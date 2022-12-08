import re

H = [] #horarios
S = [] #salas
Tt = [] #tamanhos das turmas
Ts = [] #capacidade das salas
maiorS = 0  #sala de maior tamanho

#-------------------------------------------------


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
            horariosI.append(int (input('H%d: '%(j+1)) ))
        H.append(horariosI)
        #Entrada tamanho da turma
        tam = int( input('Informe o tamanho da turma %d: '%(j+1)))
        if tam <= 0:
            print("Tamanho de turma inválido")
            return
        Tt.append(tam)
    #Entrada tamanho das salas
    global maiorS
    qtSalas = int(input('Informe a quantidade de salas: '))
    for i in range(0, qtSalas):
        tam = int( input('Informe a capacidade da sala %d: '%(i+1)) )
        if tam <= 0:
            print("Capacidade inválida")
            return
        Ts.append(tam)
        if tam > Ts[maiorS]: #atualiza o indice da maior sala
            maiorS = i
        S.append([]) #adiciona sala vazia
        

def encontrar_sala(turma,horario):
    """
    Retorna a menor sala disponível com tamanho suficiente.
    """
    print("Inserindo T%dH%d"%(turma,horario))
    menorT = Ts[maiorS]
    sala = 0
    for i,si in enumerate(S): #Percorre salas
        if Ts[i] <= menorT and Ts[i] >= Tt[turma]: #Sala menor que a menor sala atual com tamanho suficiente
            print("I = %d , Ts[i] = %d >= Tturma = %d "%(i,Ts[i],Tt[turma]))
            disponivel = True
            for aula in si: #Se a sala não possui outra aula no mesmo horario
                if re.findall("H%d"%horario,aula):
                    disponivel = False
                    break
            if disponivel:
                sala = i
                menorT = Ts[i]
    return sala

get_dados()

#-----------Algoritmo------------
for turmaI, turma in enumerate(H): 
    for horario in turma:
        sala = encontrar_sala(turmaI, horario)
        S[sala].append("T%dH%d"%(turmaI+1,horario))

print("=====Resultado=====")
for salaI,sala in enumerate(S):
    print("\nSala %d: "%(salaI+1))
    for turma in sala:
        print(turma + " ")
print("===================")