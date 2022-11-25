import pandas as pd

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
    grafo.tam = grafo.tam + 1
    return grafo

def insertar_arista(grafo, origen, peso, color, destino):
    nodo = NodoArista(peso, color, destino)
    origen = buscar_vertice(grafo, origen)[0]
    destino = buscar_vertice(grafo, destino)[0]

    if origen.adyacentes.inicio is None:
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
    origen.adyacentes.tam = origen.adyacentes.tam + 1
    return grafo

def buscar_vertice(grafo, dato):
    sol = []
    aux = grafo.inicio
    while aux is not None:
        if aux.nombre != dato and dato not in aux.pais and aux.tipo != dato:
            aux = aux.sig
        else:
            sol.append(aux)
            aux = aux.sig
    return sol

def crear_grafo(grafo):
    grafo = insertar_vertice(grafo, 'Chichen Itzá', ['México'], 'Arquitectónica')
    grafo = insertar_vertice(grafo, 'La Gran Muralla China', ['China'], 'Arquitectónica')
    grafo = insertar_vertice(grafo, 'Machu Picchu', ['Perú'], 'Arquitectónica')
    grafo = insertar_vertice(grafo, 'Taj Majal', ['India'], 'Arquitectónica')
    grafo = insertar_vertice(grafo, 'El Cristo Redentor', ['Brasil'], 'Arquitectónica')
    grafo = insertar_vertice(grafo, 'La Ciudad de Petra', ['Jordania'], 'Arquitectónica')
    grafo = insertar_vertice(grafo, 'El Coliseo de Roma', ['Italia'], 'Arquitectónica')

    grafo = insertar_vertice(grafo, 'Cataratas de Iguazú', ['Argentina'], 'Natural')
    grafo = insertar_vertice(grafo, 'Montaña de Mesa', ['Sudáfrica'], 'Natural')
    grafo = insertar_vertice(grafo, 'Amazonia', ['Bolivia', 'Brasil', 'Colombia', 'Ecuador', 'Guayana Francesa', 'Guyana', 'Perú', 'Surinam', 'Venezuela'], 'Natural')
    grafo = insertar_vertice(grafo, 'Bahía de Ha-Long', ['Vietnam'], 'Natural')
    grafo = insertar_vertice(grafo, 'Isla Jeju', ['Corea del Sur'], 'Natural')
    grafo = insertar_vertice(grafo, 'Parque Nacional de Komodo', ['Indonesia'], 'Natural')
    grafo = insertar_vertice(grafo, 'Río Subterráneo de Puerto Princesa', ['Filipinas'], 'Natural')

    grafo = crear_arista_amarilla(grafo)
    grafo = crear_arista_azul(grafo)
    grafo = crear_arista_verde(grafo)

    return grafo 

def matriz_adyacencia(grafo, nodo, color):
    indices = ['Chichen Itzá', 'La Gran Muralla China', 'Machu Picchu', 'Taj Majal', 'El Cristo Redentor', 'La Ciudad de Petra', 'El Coliseo de Roma', 'Cataratas de Iguazú', 'Montaña de Mesa', 'Amazonia', 'Bahía de Ha-Long', 'Isla Jeju', 'Parque Nacional de Komodo', 'Río Subterráneo de Puerto Princesa']
    matriz = pd.DataFrame(0, index = indices, columns = indices)

    aux = nodo.adyacentes.inicio
    aristas = []
    while aux is not None:
        if aux.color == color and aux not in aristas:
            aristas.append(aux)
            aux = buscar_vertice(grafo, aux.destino)[0].adyacentes.inicio
        else:
            aux = aux.sig
    return matriz

def crear_arista_amarilla(grafo):
    v = buscar_vertice(grafo, 'Arquitectónica')
    l = [x.nombre for x in v]
    for i in range(len(l)):
        try:
            origen = l[i]
            destino = l[i+1]
        except IndexError:
            origen = l[-1]
            destino = l[0]
        grafo = insertar_arista(grafo, origen, '90', 'Amarilla', destino)
    return grafo

def crear_arista_azul(grafo):
    v = buscar_vertice(grafo, 'Natural')
    l = [x.nombre for x in v]
    for i in range(len(l)):
        try:
            origen = l[i]
            destino = l[i+1]
        except IndexError:
            origen = l[-1]
            destino = l[0]
        grafo = insertar_arista(grafo, origen, '90', 'Azul', destino)
    return grafo

def crear_arista_verde(grafo):
    paises = ['Argentina', 'Bolivia', 'Brasil', 'China', 'Colombia', 'Corea del Sur', 'Ecuador', 'Filipinas', 'Guayana Francesa', 'Guyana', 'India', 'Indonesia', 'Italia', 'Jordania', 'México', 'Perú', 'Sudáfrica', 'Surinam', 'Venezuela', 'Vietnam']
    maravilla_pais = {}
    for pais in paises:
        v = buscar_vertice(grafo, pais)
        i = [x.nombre for x in v]
        maravilla_pais[pais] = i

    for llave in maravilla_pais:
        for i in range(len(maravilla_pais[llave])):
            try:
                origen = maravilla_pais[llave][i]
                destino = maravilla_pais[llave][i+1]
            except IndexError:
                origen = maravilla_pais[llave][-1]
                destino = maravilla_pais[llave][0]
            grafo = insertar_arista(grafo, origen, '90', 'Verde', destino)
    return grafo