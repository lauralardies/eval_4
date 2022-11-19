class NodoArbol:
    def __init__(self, simbolo, freq):
        self.izq = None
        self.der = None
        self.simbolo = simbolo
        self.freq = freq

def insertar_nodo(raiz, dato):
    if raiz is None:
        raiz = NodoArbol(dato)
    elif dato < raiz.freq:
        raiz.izq = insertar_nodo(raiz.der, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)

def arbol_huffman(simbolos, frecuencias):
    nodos = []
    for i in range(len(simbolos)): # Con este bucle tengo una lista de nodos desordenada
        nodos.append(NodoArbol(simbolos[i], frecuencias[i]))