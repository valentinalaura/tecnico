from abc import ABC, abstractmethod

# Clase abstracta Forma
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Clase concreta Circulo que hereda de Forma
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    # Implementación del método abstracto
    def calcular_area(self):
        return 3.14159 * (self.radio ** 2)

# Intentar crear un objeto de la clase abstracta (esto generará un error)
try:
    forma = Forma()
except TypeError as e:
    print(f"Error al instanciar clase abstracta: {e}")

# Crear un objeto Circulo y calcular su área
circulo = Circulo(5)
print(f"Área del círculo con radio 5: {circulo.calcular_area():.2f}")