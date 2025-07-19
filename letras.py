def contar_letras(texto):
    contador=0
    for caracter in texto:
      if caracter.isalpha():
        contador+=1
    return contador
palabra="buenos dias"
letras= contar_letras(palabra)
print("numero de letras:",letras)
