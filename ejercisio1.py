palabra=input("Ingresa una palabra: ")
vocales=("a","e","i","o","u")
contador=0
for letras in (palabra):
    if letras in vocales:
        contador+=1
print("la palabra=",palabra,"tiene",contador,"vocales")