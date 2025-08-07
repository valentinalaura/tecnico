from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    
    def calcular_area(self):
        return 3.14159 * (self.radio**2)
    
circulo=Circulo(2)
print(f"area de radio 2: {circulo.calcular_area()}")