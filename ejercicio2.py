def validarExtension(extension,listaFormatos):
    booleanoValidacion=None
    longitudExtension = len(extension)
    if((longitudExtension!=0) and (listaFormatos!=[])):
        longitudFormatos=len(listaFormatos)
        if(('.'in extension)==True):
            posicionPunto = extension.index('.')
            formatoDeExtension=""
            formatoDeExtension=extension[posicionPunto+1:longitudExtension]
            formatoDeExtension=formatoDeExtension.lower()
            for i in listaFormatos:
                listaFormatos=i.lower()
            if((formatoDeExtension in listaFormatos)==True):
                return (True)
            else:
                return(False)
        else:
            return (False)
    else:
        return (False)

def ejercicio2(var1,var2):
    return validarExtension(var1,var2)


print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg'])) # False
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg','txt'])) # True
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg','TXT'])) # True
print(ejercicio2('/home/user/listado.tXt',['mp3','wav','mpeg','TXT'])) # True
print(ejercicio2('/home/user/listado.txt',['txt'])) # True
print(ejercicio2('/home/user/listado',['mp3','wav','mpeg','txt'])) # False
print(ejercicio2('/home/user/listado',[])) # False
print(ejercicio2('',[])) # False




