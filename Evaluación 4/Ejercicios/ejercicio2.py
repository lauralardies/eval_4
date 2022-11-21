from csv import reader

class NodoArbol:
    def __init__(self, nombre, num, tipo):
        self.izq = None
        self.der = None
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

def print_nodo(ruta, nodo):
    with open(ruta, 'r') as archivo:
        lector = reader(archivo)
        for i in lector:
            if i[0] == nodo.num:
                return 'Pokémon número {}, {} de tipo {} y {} con\nTotal: {}\nHP: {}\nAttack: {}\nDefense: {}\nSp. Atk: {}\nSp. Def: {}\nSpeed: {}\nGeneration: {}\nLegendary: {}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])

def buscar_num(raiz, clave):
    pos = None
    if raiz is not None:
        if raiz.num == clave: # Nos salimos cuando encontramos en nod que buscamos
            pos = raiz
            return pos
        if pos == None:
            pos = buscar_num(raiz.izq,clave)
        if pos == None:
            pos = buscar_num(raiz.der,clave)
    return pos

def buscar_nom(raiz, clave, pos = []):
    if raiz is not None:
        if raiz.nombre.startswith(clave):
            pos.append(raiz)
        pos = (buscar_nom(raiz.izq, clave, pos))
        pos = (buscar_nom(raiz.der, clave, pos))
    return pos

ruta = 'Evaluación 4/Ejercicios/pokemon.csv'
nombres, numeros, tipos = crear_arboles(ruta)

s = buscar_num(numeros, '6')
g = buscar_num(numeros, '-9')

l = buscar_nom(nombres, 'Zorz')
r = buscar_nom(nombres, 'Bee')

for i in r:
    print(print_nodo(ruta, i))