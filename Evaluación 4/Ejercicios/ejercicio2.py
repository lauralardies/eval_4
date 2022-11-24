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
    elif info >= raiz.info:
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

# Calculamos altura del árbol
def altura(raiz):
    '''
    Función que nos permite conocer la altura de nuestro árbol
    '''
    if raiz is None:
        return 0
    else:
        altura_izq = altura(raiz.izq)
        altura_der = altura(raiz.der)
        if altura_izq > altura_der:
            return altura_izq + 1
        else:
            return altura_der + 1

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

# Apartado 4
def ordenar_arbol(raiz, lista_ordenada):
    '''
    Función que genera una lista ordenada ascendentemente incluyendo todos los nodos del árbol
    '''
    if raiz.izq:
        lista_ordenada = ordenar_arbol(raiz.izq, lista_ordenada)
    lista_ordenada.append(raiz) 
    if raiz.der:
        lista_ordenada = ordenar_arbol(raiz.der, lista_ordenada)
    return lista_ordenada

def cambiar_arbol(ruta, lista):
    '''
    Función que crea un árbol a partir de una lista de nodos cambiando su info
    '''
    raiz = None
    for l in lista:
        with open(ruta, 'r') as archivo:
            lector = reader(archivo)
            for i, fila in enumerate(lector):
                if i == l.linea - 1:
                    l.info = fila[0]
        raiz = arbol(raiz, l.info, l.linea)
    return raiz

# Apartado 5
def listado_de_nivel(raiz, nivel, listado):
    '''
    Función que devuelve una lista que incluye todos los nodos de un mismo nivel
    '''
    if raiz is None:
        return listado
    if nivel == 1:
        listado.append(raiz)
    elif nivel > 1:
        listado = listado_de_nivel(raiz.izq, nivel - 1, listado)
        listado = listado_de_nivel(raiz.der, nivel - 1, listado)
    return listado

def listado_por_nivel(raiz):
    '''
    Función que devuelve una lista que incluye los nodos de todos los niveles del árbol
    '''
    lista = []
    h = altura(raiz)
    for i in range(1, h + 1):
        listado = listado_de_nivel(raiz, i, listado = [])
        lista.append(listado)
    return lista

# Apartado 6
def buscar_tipo(ruta, dato):
    '''
    Función que a partir de un dato encuentra su correspondiente tipo de Pokémon
    '''
    with open(ruta, 'r') as archivo:
        lector = reader(archivo)
        for i, fila in enumerate(lector):
            if i == dato.linea - 1:
                return fila[2]

def debil(ruta, tipo):
    '''
    Función que analiza qué Pokémons son débiles ante cierto tipo de Pokémon 
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
    Función que crea un diccionario de los valores de la raiz cuyos valores son el número de ocurrencias que hay en el csv
    Al tratarse de un diccionario, nuestros keys no se repiten y obtenemos los valores únicos
    '''
    if raiz is not None:
        if raiz.info not in unicos:
            unicos[raiz.info] = 1
        else:
            unicos[raiz.info] = unicos[raiz.info] + 1
        unicos = valores_unicos(raiz.izq, unicos)
        unicos = valores_unicos(raiz.der, unicos)
    return unicos