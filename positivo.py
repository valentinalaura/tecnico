n=int(input("ingresa un n positivo: "))
if n <0:
    print("por favor, ingresa un numero entero positivo. ")
else: 
    for i in range(0, n + 1, 2):
        print(i)