from csv import reader

class NodoArbol:
    def __init__(self, info, linea):
        self.izq = None
        self.der = None
        self.info = info
        self.linea = linea

# Creamos árboles
def arbol(raiz, info, linea):
    '''
    Función que nos crea un árbol cualquiera
    '''
    if raiz is None:
        raiz = NodoArbol(info, linea)
    elif info > raiz.info:
        raiz.der = arbol(raiz.der, info, linea)
    else:
        raiz.izq = arbol(raiz.izq, info, linea)
    return raiz

def crear_arboles(ruta):
    '''
    Función donde especificamos los árboles a crear a partir del csv
    '''
    with open(ruta, 'r') as archivo:
        lector = reader(archivo)
        nombres, numeros, tipos = None, None, None
        linea = 0
        for i in lector:
            linea = linea + 1
            if i != ['#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']:
                nombres = arbol(nombres, i[1], linea)
                numeros = arbol(numeros, i[0], linea)
                tipos = arbol(tipos, i[2], linea)
    return nombres, numeros, tipos

# Mostramos en pantalla el nodo
def print_info(ruta, lista, nombre):
    sol = []
    if len(lista) == 0:
        return 'No se ha encontrado ningún Pokémon con los datos aportados.'
    for l in lista:
        with open(ruta, 'r') as archivo:
            lector = reader(archivo)
            for i, fila in enumerate(lector):
                if i == l.linea - 1:
                    if nombre == True:
                        sol.append(fila[1])
                        break
                    elif nombre == False:
                        sol.append('Pokémon número {}, {} de tipo {} y débil ante {} con\nTotal: {}.\nHP: {}.\nAttack: {}.\nDefense: {}.\nSp. Atk: {}.\nSp. Def: {}.\nSpeed: {}.\nGeneration: {}.\nLegendary: {}.'.format(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12]))
                        break
    if nombre == True:
        return ', '.join(sol)
    
    return '\n\n'.join(sol)

# Apartados 1, 2 y 3
def buscar(raiz, clave, pos):
    '''
    Función que busca en un árbol la clave dada
    '''
    if raiz is not None:
        if raiz.info == clave and raiz not in pos:
            pos.append(raiz)
        pos = buscar(raiz.izq, clave, pos)
        pos = buscar(raiz.der, clave, pos)
    return pos

def filtrar(raiz, clave, pos):
    '''
    Función que busca en un árbol parte de la clave dada
    '''
    if raiz is not None:
        if clave in raiz.info and raiz not in pos:
            pos.append(raiz)
        pos = filtrar(raiz.izq, clave, pos)
        pos = filtrar(raiz.der, clave, pos)
    return pos

# Apartado 6
def buscar_tipo(ruta, dato):
    '''
    A partir de otro dato como por ejemplo el nombre, buscamos el tipo de dicho Pokémon
    '''
    with open(ruta, 'r') as archivo:
        lector = reader(archivo)
        for i, fila in enumerate(lector):
            if i == dato.linea - 1:
                return fila[2]

def debil(ruta, tipo):
    '''
    A partir de un tipo de Pokémon, analizamos qué Pokémons son débiles a este tipo 
    '''
    with open(ruta, 'r') as archivo:
        lector = reader(archivo)
        debiles = None
        linea = 0
        for i in lector:
            linea = linea + 1
            if i != ['#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']:
                debiles = arbol(debiles, i[3], linea)
    sol = buscar(debiles, tipo, pos = [])
    return sol

# Apartado 7
def valores_unicos(raiz, unicos):
    '''
    Crea un diccionario de los valores de la raiz cuyos valores son el número de ocurrencias que hay en el csv
    Al tratarse de un diccionario, nuestros keys no se repiten y conseguimos los valores únicos
    '''
    if raiz is not None:
        if raiz.info not in unicos:
            unicos[raiz.info] = 1
        else:
            unicos[raiz.info] = unicos[raiz.info] + 1
        unicos = valores_unicos(raiz.izq, unicos)
        unicos = valores_unicos(raiz.der, unicos)
    return unicos