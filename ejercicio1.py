def generarListaDivisores(Numero,listaPosiblesDivisores):
    listaDivisores=[]
    contador=0
    cantidadDivisores=len(listaPosiblesDivisores)
    if(type(Numero)is int):
        if(Numero>0):
            while(contador<cantidadDivisores):
                if(Numero%listaPosiblesDivisores[contador]==0):
                    listaDivisores.append(listaPosiblesDivisores[contador])
                contador=contador+1
            return (listaDivisores)
        else:
            return (listaDivisores)
    else:
        return (listaDivisores)

def ejercicio1(var1,var2):
    return generarListaDivisores(var1,var2)


print(ejercicio1("",[1,2,3])) # []
print(ejercicio1(-1,[1,2,3])) # []
print(ejercicio1(0,[1,2,3])) # []
print(ejercicio1(0,[])) # []
print(ejercicio1(1,[1,2])) # [1]
print(ejercicio1(2,[1,-2])) # [1,-2]
print(ejercicio1(8,[1,7,2,-4,6,9])) # [1,2,-4]
print(ejercicio1(331,[1,2,3,7,147,331,518])) # [1,331]