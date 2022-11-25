class NodoArista():
    def __init__(self, peso, color, destino):
        self.peso = peso
        # Nuestras aristas van a tener color para separar aquellas aristas que unen países con aquellas aristas que unen tipos
        self.color = color 
        self.destino = destino
        self.sig = None

class NodoVertice():
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
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

def insertar_vertice(grafo, nombre, pais, tipo):
    nodo = NodoVertice(nombre, pais, tipo)
    if grafo.inicio is None or grafo.inicio.nombre > nombre:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.nombre < nodo.nombre:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    return grafo

def buscar_vertice(grafo, dato):
    aux = grafo.inicio
    while aux is not None:
        while aux.nombre != dato or aux.pais != dato or aux.tipo != dato:
            aux = aux.sig
            break
    return aux

def insertar_arista(grafo, origen, peso, color, destino):
    nodo = NodoArista(peso, color, destino)
    origen = buscar_vertice(grafo, origen)
    destino = buscar_vertice(grafo, destino)

    if origen.adyacentes is None:
        nodo.sig = origen.adyacentes.inicio
        origen.adyacentes.inicio = nodo
    else:
        ant = origen.adyacentes.inicio 
        act = origen.adyacentes.inicio.sig 
        while act is not None:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tam = origen.tam + 1

grafo = Grafo()
grafo = insertar_vertice(grafo, 'Chichen Itzá', ['México'], 'Arquetectónica')
grafo = insertar_vertice(grafo, 'La Gran Muralla China', ['China'], 'Arquetectónica')
grafo = insertar_vertice(grafo, 'Machu Picchu', ['Perú'], 'Arquetectónica')
grafo = insertar_vertice(grafo, 'Taj Majal', ['India'], 'Arquetectónica')
grafo = insertar_vertice(grafo, 'El Cristo Redentor', ['Brasil'], 'Arquetectónica')
grafo = insertar_vertice(grafo, 'La Ciudad de Petra', ['Jordania'], 'Arquetectónica')
grafo = insertar_vertice(grafo, 'El Coliseo de Roma', ['Italia'], 'Arquetectónica')
grafo = insertar_vertice(grafo, 'Cataratas de Iguazú', ['Argentina'], 'Natural')
grafo = insertar_vertice(grafo, 'Montaña de Mesa', ['Sudáfrica'], 'Natural')
grafo = insertar_vertice(grafo, 'Amazonia', ['Bolivia', 'Brasil', 'Colombia', 'Ecuador', 'Guayana Francesa', 'Guyana', 'Perú', 'Surinam', 'Venezuela'], 'Natural')
grafo = insertar_vertice(grafo, 'Bahía de Ha-Long', ['Vietnam'], 'Natural')
grafo = insertar_vertice(grafo, 'Isla Jeju', ['Corea del Sur'], 'Natural')
grafo = insertar_vertice(grafo, 'Parque Nacional de Komodo', ['Indonesia'], 'Natural')
grafo = insertar_vertice(grafo, 'Río Subterráneo de Puerto Princesa', ['Filipinas'], 'Natural')

print('hola')