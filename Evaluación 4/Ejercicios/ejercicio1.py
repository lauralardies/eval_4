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

def ordenar_objetos(lista):
    lista = sorted(lista, key=lambda x: x.simbolo)
    lista = sorted(lista, key=lambda x: x.freq)
    return lista

def arbol_huffman(simbolos, frecuencias):
    nodos = []
    for i in range(len(simbolos)): # Con este bucle tengo una lista de nodos desordenada
        nodos.append(NodoArbol(simbolos[i], frecuencias[i]))
    nodos = ordenar_objetos(nodos)
    return nodos

simbolos = ['A', 'F', '1', '3', '0', 'M', 'T']
frecuencias = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
lista = arbol_huffman(simbolos, frecuencias)
print('hola')