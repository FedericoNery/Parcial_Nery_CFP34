from random import randint
def generarMatrizTriangular(numero):
    if(type(numero) is int):
        if(numero>1):
            cantidadNumeros=numero**2
            listaNumerosAleatorios=[]
            contador=0
            listaNumerosDeA4=[]
            matriz=[]
            for j in range (0,cantidadNumeros):
                listaNumerosAleatorios.append(randint(1,9))
            for h in range(0,numero):
                for i in range(0,numero):
                    if((h>0) and (h-i>0)):
                        listaNumerosDeA4.append(0)
                    else:
                        listaNumerosDeA4.append(listaNumerosAleatorios[contador])
                    contador=contador+1
                matriz.append(listaNumerosDeA4)
                listaNumerosDeA4=[]
            return (matriz)
        else:
            return ([])
    else:
        return ([])

def ejercicio3(var1):
    return generarMatrizTriangular(var1)


print(ejercicio3(-1)) # []
print(ejercicio3(0)) # []
print(ejercicio3(1)) # []
print(ejercicio3(2)) # [[x,x],[0,x]]
print(ejercicio3(3)) # [[x,x,x],[0,x,x],[0,0,x]]
print(ejercicio3(4)) # [[x,x,x,x],[0,x,x,x],[0,0,x,x],[0,0,0,x]]
print(ejercicio3("4")) #[]
print(ejercicio3("PEPE")) #[]
print(ejercicio3(2.5)) #[]
