class NodoArbol:
    def __init__(self, nombre, num, tipo):
        self.izq = None
        self.der = None
        self.padre = None
        self.nombre = nombre
        self.num = num
        self.tipo = tipo
