palabra= input ("introduce una palabra: ")
vocales="aeiou"
contador=0
for letra in palabra:
    if letra in vocales:
      contador +=1
print (f"la palabra '{palabra}' tiene {contador} vocal. ")
