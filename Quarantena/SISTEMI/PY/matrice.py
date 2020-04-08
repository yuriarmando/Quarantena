def funzmatrice(): 
    Nodi = int(input("inserire il numero di nodi: "))
    matrice = [ [ 0 for i in range(Nodi) ] for j in range(Nodi) ]

    for i in range(Nodi):
        Link = input(f"il nodo {i} a chi è collegato?: ").split(",")
        int_Link = [int (i) for i in Link]
        print(Link)
        for a in int_Link:
        if(i == a ):
            matrice[i][a] = 0
        else:
            matrice[i][a] = 1
    print("la matrice é:")
    for i in range(Nodi) :  
         for j in range(Nodi):
        print(matrice[i][j], end=" ")
        print()


    