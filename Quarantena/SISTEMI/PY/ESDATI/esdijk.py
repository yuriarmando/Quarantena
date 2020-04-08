#YURI ARMANDO
#4 AROB

import networkx as nx
import numpy as np

def toDizionario(matr):
    diz = {}
    for i in range(0, len(matr)):
        vet = []
        for j in range(0, len(matr)):
            vet.append(matr[i][j])
        diz['nodo '+ str(i+1)] = vet
    return diz

def leggiPavi():
    file = open("data.txt", "r")
    lines = file.readlines()
    pavi = []
    dim = 0
    for line in lines:
        cells = line.replace("\n", "").split(" ")
        vet = []
        for cell in cells:
            if cell == "True":
                vet.append(True)
            elif cell == "False" :
                vet.append(False)
                dim = dim + 1
            
        pavi.append(vet)
    return pavi, dim

def creazioneCampo(pavi):
    campo = []
    cont = 0
    
    for i in range(0, len(pavi)):
        vet = []
        for j in range(0, len(pavi)):
            if pavi[i][j] == True:
                vet.append(cont)
                cont = cont + 1
            else: 
                vet.append(-1)
        campo.append(vet)
    return campo

def creazioneMatrAdiacenze(campo, dim):
    m = []
    for i in range(0, dim): 
        vet = []
        for j in range(0, dim):
            vet.append(0)
        m.append(vet)

    #Calcolo matrice adiacenze
    for i in range(0, len(campo)):
        for j in range(0, len(campo)):
            if campo[i][j] != -1:
                i2 = campo[i][j]
                if j+1 < len(campo):
                    if campo[i][j+1] != -1:
                        j2 = campo[i][j+1]
                        m[i2][j2] = 1
                        m[j2][i2] = 1
                if i+1 < len(campo):
                    if campo[i+1][j] != -1: 
                        j2 = campo[i+1][j]
                        m[i2][j2] = 1
                        m[j2][i2] = 1
    return m
        

def main():
    pavi, dim = leggiPavi()
    dim = len(pavi) * len(pavi) - dim
    campo = creazioneCampo(pavi)
    mAdiacenze = creazioneMatrAdiacenze(campo, dim)
    for i in range(0, len(mAdiacenze)):
        print(mAdiacenze[i])

    mAdiacenze = np.array(mAdiacenze)   #conversione della matrice 
    G = nx.from_numpy_matrix(mAdiacenze)
    start = input("nodo di partenza: ")
    destination = input("nodo di destinazione: ")
    print(nx.dijkstra_path(G, int(start), int(destination)))
    