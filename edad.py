from datetime import date 
def calcular_edad(year,month,day):
    today = date.today()
    date2= date(year,month,day)
    if today.year-date2.year>=18:
        print("eres mayr de edad")
    else:
        print("eres menor de edad ")

calcular_edad(2010,8,3)