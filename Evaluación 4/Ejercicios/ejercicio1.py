class NodoArbol:
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

def insertar_nodo( raiz, dato):
    if raiz is None:
        raiz = NodoArbol(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.der, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)