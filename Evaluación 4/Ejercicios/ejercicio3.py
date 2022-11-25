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
    sol = []
    aux = grafo.inicio
    while aux is not None:
        if aux.nombre != dato and dato not in aux.pais and aux.tipo != dato:
            aux = aux.sig
        else:
            sol.append(aux)
            aux = aux.sig
    return sol

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

grafo = insertar_arista(grafo, 'Chichen Itzá', '90', 'Amarillo', 'El Coliseo de Roma')
grafo = insertar_arista(grafo, 'El Coliseo de Roma', '90', 'Amarillo', 'El Cristo Redentor')
grafo = insertar_arista(grafo, 'El Cristo Redentor', '90', 'Amarillo', 'La Ciudad de Petra')
grafo = insertar_arista(grafo, 'La Ciudad de Petra', '90', 'Amarillo', 'La Gran Muralla China')
grafo = insertar_arista(grafo, 'La Gran Muralla China', '90', 'Amarillo', 'Machu Picchu')
grafo = insertar_arista(grafo, 'Machu Picchu', '90', 'Amarillo', 'Taj Majal')
grafo = insertar_arista(grafo, 'Taj Majal', '90', 'Amarillo', 'Chichen Itzá')

grafo = insertar_arista(grafo, 'Amazonia', '90', 'Azul', 'Bahía de Ha-Long')
grafo = insertar_arista(grafo, 'Bahía de Ha-Long', '90', 'Azul', 'Cataratas de Iguazú')
grafo = insertar_arista(grafo, 'Cataratas de Iguazú', '90', 'Azul', 'Isla Jeju')
grafo = insertar_arista(grafo, 'Isla Jeju', '90', 'Azul', 'Montaña de Mesa')
grafo = insertar_arista(grafo, 'Montaña de Mesa', '90', 'Azul', 'Parque Nacional de Komodo')
grafo = insertar_arista(grafo, 'Parque Nacional de Komodo', '90', 'Azul', 'Río Subterráneo de Puerto Princesa')
grafo = insertar_arista(grafo, 'Río Subterráneo de Puerto Princesa', '90', 'Azul', 'Amazonia')

paises = ['Argentina', 'Bolivia', 'Brasil', 'China', 'Colombia', 'Corea del Sur', 'Ecuador', 'Filipinas', 'Guayana Francesa', 'Guyana', 'India', 'Indonesia', 'Italia', 'Jordania', 'México', 'Perú', 'Sudáfrica', 'Surinam', 'Venezuela', 'Vietnam']
maravilla_pais = {}
for pais in paises:
    v = buscar_vertice(grafo, pais)
    i = [x.nombre for x in v]
    maravilla_pais[pais] = i

for llave in maravilla_pais:
    for i in range(len(maravilla_pais[llave])):
        try:
            v1 = maravilla_pais[llave][i]
            v2 = maravilla_pais[llave][i+1]
        except IndexError:
            v1 = maravilla_pais[llave][-1]
            v2 = maravilla_pais[llave][0]
        grafo = insertar_arista(grafo, v1, '90', 'Verde', v2)