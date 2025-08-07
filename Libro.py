#Taller  de programacion 10

class libro:
    def __init__(self,titulo,autor,año):
        self.titulo=titulo
        self.autor=autor
        self.año=año

def mostrar_info(self):
    print(f"Del año:{self.año}")

mi_libro=libro ("Orgullo y prejuicio","jane austen", 1813)

print(f"Mio libro es {mi_libro.titulo} de {mi_libro.autor}")

mi_libro.mostrar_info()