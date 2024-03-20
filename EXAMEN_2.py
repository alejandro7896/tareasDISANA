n = eval(input("Ingrese el cuadrado: "))
import math
ra = n*n

#print(f"ra: {ra}")

arr = [[0 for _ in range(n)] for _ in range(n)]

#print(f"arr: {arr}")

a_i = 0


recorrido = 1

c = [[0],[0]]

while True:
    if a_i == ra:
        break
    if recorrido == 1: #hacia adelante
        arr[c[0][0]][c[1][0]] = a_i+1 #asigna
        #print(f"asigné {a_i+1} al espacio {c[0][0]},{c[1][0]} R: {recorrido}")
        #print(arr)
        try:
            #verifica
            if arr[c[0][0]][c[1][0]+1] == 0:
                
                #avanza
                c[1][0]+=1 #arreglo guia
                a_i +=1 #numero de indice
                #siguiente ciclo
                continue
            else:
                #ya está ocupado
                recorrido = 2 #hacia abajo
                c[0][0]+=1
                a_i +=1 #numero de indice
                continue
        except:
            #se salió de los bounds, hay que cambiar de movimiento
            recorrido = 2 #hacia abajo
            c[0][0]+=1
            a_i +=1 #numero de indice
            continue
            
            
    if recorrido == 2:
        arr[c[0][0]][c[1][0]] = a_i+1 #asigna
        #print(f"asigné {a_i+1} al espacio {c[0][0]},{c[1][0]} R: {recorrido}")
        
        #print(arr)
        
        try:
            #verifica
            if arr[c[0][0]+1][c[1][0]] == 0:
                #avanza
                c[0][0]+=1 #arreglo guia
                a_i +=1 #numero de indice
                #siguiente ciclo
                continue
            else:
                #ya está ocupado
                recorrido = 3 #hacia la izquierda
                c[1][0]-=1
                a_i +=1 #numero de indice
                continue
        except:
            #ya está ocupado
            recorrido = 3 #hacia la izquierda
            c[1][0]-=1
            a_i +=1 #numero de indice
            continue
    if recorrido == 3:
        arr[c[0][0]][c[1][0]] = a_i+1 #asigna
        #print(f"asigné {a_i+1} al espacio {c[0][0]},{c[1][0]} R: {recorrido}")
        #print(arr)
        try:
            #verifica
            if arr[c[0][0]][c[1][0]-1] == 0:
                #avanza
                c[1][0]-=1 #arreglo guia
                a_i +=1 #numero de indice
                #siguiente ciclo
                continue
            else:
                #ya está ocupado
                recorrido = 4 #hacia arriba
                c[0][0]-=1
                a_i +=1 #numero de indice
                continue
        except:
            #ya está ocupado
            recorrido = 4 #hacia arriba
            c[0][0]-=1
            a_i +=1 #numero de indice
            continue
    if recorrido == 4:
        arr[c[0][0]][c[1][0]] = a_i+1 #asigna
        #print(f"asigné {a_i+1} al espacio {c[0][0]},{c[1][0]} R: {recorrido}")
        #print(arr)
        try:
            #verifica
            if arr[c[0][0]-1][c[1][0]] == 0:
                #avanza
                c[0][0]-=1 #arreglo guia
                a_i +=1 #numero de indice
                #siguiente ciclo
                continue
            else:
                #ya está ocupado
                recorrido = 1 #hacia izquierda
                c[1][0]+=1
                a_i +=1 #numero de indice
                continue
        except:
            #ya está ocupado
            recorrido = 1 #hacia izquierda
            c[1][0]+=1
            a_i +=1 #numero de indice
            continue
            
    
for x in range(n):
    for a in range(n):
        print(f"{arr[x][a]}\t",end="")
    print("\n",end="")


    
    
    
    
    

    


