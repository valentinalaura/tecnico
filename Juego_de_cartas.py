import random

class Carta:
    def __init__(self,palo,valor,nombre):
        self.palo=palo
        self.valor=valor
        self.nombre = nombre

def __str__(self):
    return f"{self.nombre_valor} de {self.palo}"

class Mazo:
    def __init__(self):
        self.cartas = []
        palos=["Corazones","Diamante","Treboles","picas"]
        valores_numericos= list(range(2, 11))
        nombre_valores= [str(v) for v in valores_numericos]+["J","Q","k","As"]
        valores_mapeado= {
            "J":11 , "Q":12 , "K": 13 , "As":14 
        }

        for palo in palos:
            for i, nombre_valor in enumerate(nombre_valores):
                if nombre_valor.isdigit():
                    valor = int(nombre_valor)
                else:
                    valor = valores_mapeado.get(nombre_valor)
                self.cartas.append(Carta(palo, valor, nombre_valor))

    def baraja(self):
        random.shuffle(self.cartas)

    def repartir_cartas(self):
        if not self.cartas:
            return None
        return self.cartas.pop()
    
class Jugador:
    def __init__(self, nombre):
        self.nombre=nombre
        self.mano=[]
        self.Puntaje= 0

    def agregar_carta(self, carta):
        self.mano.append(carta)

    def mostrar_mano(self):
       if not self.mano:
           print(f"{self.nombre} no tiene cartas en la mano.")
           return
       print(f"Mano de {self.nombre}:")
       for carta in self.mano:
           print(f" - {carta}")

    def jugar_carta(self):
        if self.mano:
            return self.mano.pop(0)
        return None

    def sumar_puntos(self):
        self.Puntaje +=1


def jugar_ronda(jugador1,jugador2,mazo):
    print("\n--- ¡Nueva Ronda! ---")
    jugador1.mano= []
    jugador2.mano= []

    carta1= mazo.repartir_cartas()
    carta2= mazo.repartir_cartas()

    if not carta1 or not carta2:
        print("xx ¡No hay suficientes cartas en el mazo para jugar otra ronda¡ xx")
        return False
    
    jugador1.agregar_carta(carta1)
    jugador2.agregar_carta(carta2)

    print(f"{jugador1.nombre} jugó: {carta1}")
    print(f"{jugador2.nombre} jugó: {carta2}")

    if carta1.valor > carta2.valor:
        print(f"¡{jugador1.nombre} Gana la ronda!")
    elif carta2.valor > carta1.valor:
        print(f"¡{jugador2.nombre} Gana la ronda!")
    else:
        print("¡es un Empate!")

    print(f"Puntuacion actual: {jugador1.nombre}: {jugador1.puntuacion} - {jugador2.nombre}: {jugador2.puntuacion}")
    return True

def iniciar_juego():
    print("¡Bienvenido al juego de mayor o menor con POO")

    nombre1=input("ingresa tu nombre de jugador 1:")   
    nombre2=input("ingresa tu nombre de jugador 2:")
    jugador1= Jugador(nombre1)
    jugador2= Jugador(nombre2)

    mazo = Mazo()
    mazo.baraja()
    print("Mazo creado y barajeado.")

    num_rondas= int(input("¿cuantas rondas quieren jugar?"))
    rondas_jugadas= 0

    while rondas_jugadas < num_rondas:
        if not jugar_ronda(jugador1, jugador2, mazo):
            break
        rondas_jugadas +=1

    print("\n-- ¡juego terminado! --")
    print(f"Puntacion Final")
    print(f"{jugador1.nombre}: {jugador1.Puntaje} Puntos")
    print(f"{jugador2.nombre}: {jugador2.Puntaje} Puntos")

    if jugador1.Puntaje > jugador2.Puntaje:
            print(f"¡El Ganador es {jugador1.nombre}!") 
    elif jugador2.Puntaje > jugador1.Puntaje:
            print(f"El Ganador es {jugador2.nombre}!")
    else:
            print("****** ¡El juego termino en un empate! ******")

iniciar_juego()