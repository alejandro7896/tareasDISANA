# AUTOR: ALEJANDRO ANTONIO AMAVIZCA LOPEZ
# DISENIO Y ANALISIS DE ALGORITMOS
# PROFESOR: MIGUEL BERNAL MARIN

print("DIFERENCIADOR DE CUADRILATEROS")
lados = []

for x in range(4):
    lados.append(int(input(f"Lado {x+1}: ")))

ap = lados[0]

cuadrado = False
rectangulo = False

for l in lados:
    if ap == l:
        cuadrado = True
    else:
        cuadrado = False
        break
for l in lados:
    if lados.count(l) == 2:
        rectangulo = True
    else:
        rectangulo = False
        break
    
if cuadrado:
    print("ES UN CUADRADO")
    
elif rectangulo:
    print("ES UN RECTÁNGULO")
    
else:
    print("ES OTRO CUADRILATERO")
    
