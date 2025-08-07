from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    
    def calcular_area(self):
        return 3.14159 * (self.radio ** 2)


try:
    forma = Forma()
except TypeError as e:
    print(f"Error al instanciar clase abstracta: {e}")


circulo = Circulo(5)
print(f"Área del círculo con radio 5: {circulo.calcular_area():.2f}")