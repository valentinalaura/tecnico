esvocal=False
vocales=["a","e","i","o","u"]
contador = 0
palabra = "fgfgrt"
for indice in palabra:
     contador +=1
     if indice in vocales:
         esvocal=True
         break

if esvocal:
    print("es vocal")
else:
    print("no es vocal")