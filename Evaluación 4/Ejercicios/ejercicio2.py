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

def print_nodo(ruta, lista):
    sol = []
    if len(lista) == 0:
        return 'No se ha encontrado ningún Pokémon con los datos aportados.'
    for l in lista:
        with open(ruta, 'r') as archivo:
            lector = reader(archivo)
            for i in lector:
                if i[1] == l.nombre:
                    sol.append('Pokémon número {}, {} de tipo {} y {} con\nTotal: {}\nHP: {}\nAttack: {}\nDefense: {}\nSp. Atk: {}\nSp. Def: {}\nSpeed: {}\nGeneration: {}\nLegendary: {}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
    return '\n\n'.join(sol)

def print_nombre(lista):
    sol = []
    if len(lista) == 0:
        return 'No se ha encontrado ningún Pokémon con los datos aportados.'
    for l in lista:
        sol.append(l.nombre)
    return ', '.join(sol)

def buscar_tipo(raiz, clave, pos):
    if raiz is not None:
        if raiz.tipo == clave and raiz not in pos:
            pos.append(raiz)
        pos = buscar_tipo(raiz.izq, clave, pos)
        pos = buscar_tipo(raiz.der, clave, pos)
    return pos

def buscar_num(raiz, clave, pos):
    if raiz is not None:
        if raiz.num == clave and raiz not in pos:
            pos.append(raiz)
        pos = buscar_nom(raiz.izq, clave, pos)
        pos = buscar_nom(raiz.der, clave, pos)
    return pos

def buscar_nom(raiz, clave, pos):
    if raiz is not None:
        if raiz.nombre.startswith(clave) and raiz not in pos:
            pos.append(raiz)
        pos = buscar_nom(raiz.izq, clave, pos)
        pos = buscar_nom(raiz.der, clave, pos)
    return pos

ruta = 'Evaluación 4/Ejercicios/pokemon.csv'
nombres, numeros, tipos = crear_arboles(ruta)

s = buscar_num(numeros, '6', pos = [])
g = buscar_num(numeros, '-9', pos = [])

l = buscar_nom(nombres, 'Zorz', pos = [])
r = buscar_nom(nombres, 'Bee', pos = [])

fuego = buscar_tipo(tipos, 'Fire', pos = [])
agua = buscar_tipo(tipos, 'Water', pos = [])
planta = buscar_tipo(tipos, 'Grass', pos = [])
elec = buscar_tipo(tipos, 'Electric', pos = [])

print(print_nodo(ruta, l))
print(print_nodo(ruta, r))
