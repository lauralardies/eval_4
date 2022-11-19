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
    lista = sorted(lista, key=lambda x: x.simbolo) # Primero ordenamos alfabéticamente
    lista = sorted(lista, key=lambda x: x.freq) # Luego ordenamos las frecuencias a partir de la lista ordenada alfabéticamente 
    return lista

def insertar_nodo_huffman(lista, nodo):
    for i in range(len(lista)):
        if lista[i].freq > nodo.freq: 
            lista.insert(i, nodo)
            break
        if i == len(lista)-1: # En el caso en el que tengamos que añadir nuestro nodo al final de la lista
            lista.append(nodo)
            break
    return lista

def arbol_huffman(simbolos, frecuencias):
    nodos = []
    for i in range(len(simbolos)): # Con este bucle tengo una lista de nodos desordenada
        nodos.append(NodoArbol(simbolos[i], frecuencias[i]))
    nodos = ordenar_objetos(nodos) # Nodos ordenados
    while len(nodos) > 1:
        nodo = NodoArbol('XX', nodos[0].freq + nodos[1].freq) # Creamos un nuevo nodo al que no le corresponde ningún símbolo
        nodo.izq = nodos[0]
        nodo.der = nodos[1]
        nodos = insertar_nodo_huffman(nodos, nodo)
        nodos.pop(1)
        nodos.pop(0)
    return nodos

simbolos = ['A', 'F', '1', '3', '0', 'M', 'T']
frecuencias = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
lista = arbol_huffman(simbolos, frecuencias)
