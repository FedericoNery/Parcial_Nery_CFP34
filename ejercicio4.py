def calcularGanadorDeLiga(listaPartidos):
    equipoGanador=""
    cantidadPartidos=len(listaPartidos)
    posicionEquipo1=0
    posicionEquipo2=0
    posicionGanador=0
    listaEquipos=[]
    listaPuntaje=[]
    listaTotal=(listaEquipos,listaPuntaje)
    if(cantidadPartidos!=0):
        for i in listaPartidos:
            if((i[0] in listaEquipos)==False):
                listaEquipos.append(i[0])
                listaPuntaje.append(0)
            if((i[2] in listaEquipos)==False):
                listaEquipos.append(i[2])
                listaPuntaje.append(0)
            posicionEquipo1=listaEquipos.index(i[0])
            posicionEquipo2=listaEquipos.index(i[2])
            if(i[1]>i[3]):
                listaPuntaje[posicionEquipo1]=listaPuntaje[posicionEquipo1]+2
            elif(i[1]==i[3]):
                listaPuntaje[posicionEquipo1]=listaPuntaje[posicionEquipo1]+1
                listaPuntaje[posicionEquipo2]=listaPuntaje[posicionEquipo2]+1
            else:
                listaPuntaje[posicionEquipo2]=listaPuntaje[posicionEquipo2]+2
            posicionGanador=listaPuntaje.index(max(listaPuntaje))
        return(listaEquipos[posicionGanador])
    else:
        return("")


def ejercicio4(var1):
    return calcularGanadorDeLiga(var1)

campeonato = []
print(ejercicio4(campeonato)) # ""

campeonato = [("a",1,"b",0)]
print(ejercicio4(campeonato)) # a

campeonato = [("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]
print(ejercicio4(campeonato)) # c

campeonato = [("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]
print(ejercicio4(campeonato)) # a  b  c (cualquiera de las 3)

campeonato = [("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]
print(ejercicio4(campeonato)) # a