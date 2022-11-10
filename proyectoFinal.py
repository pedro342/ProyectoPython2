import random

def ord_burbuja(arreglo):
    OeBubble = 0

    n = len(arreglo) 

    for i in range(n-1): 
        for j in range(n-1-i): 
            if arreglo[j] > arreglo[j+1]: 
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j] 
                OeBubble += 11
        OeBubble += 7        
    OeBubble += 3
    print(OeBubble)

def insercion(A):
    OeInsercion = 0
    for i in range(len(A)): 
        for j in range(i,0,-1): 
            if(A[j-1] > A[j]): 
                aux=A[j] 
                A[j]=A[j-1] 
                A[j-1]=aux 
                OeInsercion += 14
        OeInsercion += 10
    OeInsercion += 4
    print (OeInsercion)

def seleccion(arreglo):
    longitud = len(arreglo) 
    OeSeleccion = 2
    for i in range(longitud-1): 
        for j in range(i+1, longitud): 
            if arreglo[i] > arreglo[j]: 
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i] 
                OeSeleccion += 7
        OeSeleccion += 9        
    OeSeleccion += 4
    print(OeSeleccion)

def shellsort(vectorshell):
    largo = 0 
    OeShell = 1
    for i in vectorshell: 
        largo += 1 
        OeShell += 3
    OeShell += 2
    distancia = largo // 2 
    OeShell += 2
    while distancia > 0: 
        for i in range(distancia, largo): 
            val = vectorshell[i] 
            j = i 
            while j >= distancia and vectorshell[j - distancia] > val: 
                vectorshell[j] = vectorshell[j - distancia] 
                j -= distancia 
                OeShell += 12
            vectorshell[j] = val 
            OeShell += 15
        distancia //= 2 
        OeShell += 7
    OeShell += 1
    print(OeShell)
 
def quicksort(arreglo, izquierda, derecha):
    if izquierda < derecha: 
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort(arreglo, izquierda, indiceParticion)
        quicksort(arreglo, indiceParticion + 1, derecha)

def particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda] 
    while True:
        while arreglo[izquierda] < pivote: 
            izquierda += 1   
        while arreglo[derecha] > pivote: 
            derecha -= 1 
        if izquierda >= derecha: 
            return derecha
        else:
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda] 
            izquierda += 1 
            derecha -= 1 

tam = int(input("que tamanio quiere darle al vector: "))
vect = [tam]

def llenar_vectMan(tam):
	for i in range(0,tam):
		vect.append(int(input("ingrese un numero: ")))

def crear_lista(tam):
    for i in range(tam):
        vect.append(random.randint(0,10000))

if tam < 10:
    como = input("Como desea ingresar los numero, manual o autorrellenar: ")
    if como == "manual":
        llenar_vectMan(tam)
    elif como == "autorrellenar":
        crear_lista(tam)
    else:
        print("la respuesta no es correcta")
elif tam > 10:
    crear_lista(tam)
else:
    print("El valor es incorrecto, solo se permiten numeros positivos")
quicksort(vect, 0, len(vect)-1)
ord_burbuja(vect)
insercion(vect)
seleccion(vect)
shellsort(vect)