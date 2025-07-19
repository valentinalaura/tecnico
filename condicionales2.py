from datetime import date

datef=date.today()
date2=date(2011,6,23)

def calculo(datef,date2):
    año1= datef.year
    año2=date2.year
    edad= año1 - año2
    if edad>= 18:
        print("es menor de edad")
    else:
        print("es mayor de edad")
calculo(datef,date2)