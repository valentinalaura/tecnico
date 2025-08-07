from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

