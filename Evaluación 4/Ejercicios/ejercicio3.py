class NodoArista():
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None

class NodoVertice():
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo():
    def __init__(self, dirigido=False):
        self.inicio = None
        self.dirigido = dirigido
        self.tam = 0

class Arista():
    def __init__(self):
        self.inicio = None
        self.tam = 0