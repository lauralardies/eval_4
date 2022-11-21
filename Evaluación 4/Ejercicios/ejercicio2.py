from csv import reader

class NodoArbol:
    def __init__(self, nombre, num, tipo):
        self.izq = None
        self.der = None
        self.padre = None
        self.nombre = nombre
        self.num = num
        self.tipo = tipo

def arbol_nombre(raiz, nombre, num, tipo):
    if raiz is None:
        raiz = NodoArbol(nombre, num, tipo)
    elif nombre > raiz.nombre:
        raiz.der = arbol_numero(raiz.der, nombre, num, tipo)
    else:
        raiz.izq = arbol_numero(raiz.izq, nombre, num, tipo)
    return raiz

def arbol_numero(raiz, nombre, num, tipo):
    if raiz is None:
        raiz = NodoArbol(nombre, num, tipo)
    elif num < raiz.num:
        raiz.der = arbol_numero(raiz.der, nombre, num, tipo)
    else:
        raiz.izq = arbol_numero(raiz.izq, nombre, num, tipo)
    return raiz

def arbol_nombre(raiz, nombre, num, tipo):
    if raiz is None:
        raiz = NodoArbol(nombre, num, tipo)
    elif tipo > raiz.tipo:
        raiz.der = arbol_numero(raiz.der, nombre, num, tipo)
    else:
        raiz.izq = arbol_numero(raiz.izq, nombre, num, tipo)
    return raiz

def crear_arboles(ruta):
    with open(ruta, 'r') as archivo:
        lector = reader(archivo)
        nombres, numeros, tipos = None, None, None
        for i in lector:
            if i == ['#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']:
                pass
            else:
                nombres = arbol_nombre(nombres, i[1], i[0], i[2])
                numeros = arbol_numero(numeros, i[1], i[0], i[2])
                tipos = arbol_nombre(tipos, i[1], i[0], i[2])
    return nombres, numeros, tipos

ruta = 'Evaluación 4/Ejercicios/pokemon.csv'
nombres, numeros, tipos = crear_arboles(ruta)