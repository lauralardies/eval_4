from csv import reader

class NodoArbol:
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
        
def arbol_alpha(raiz, info):
    if raiz is None:
        raiz = NodoArbol(info)
    elif info > raiz.info:
        raiz.der = arbol_alpha(raiz.der, info)
    else:
        raiz.izq = arbol_alpha(raiz.izq, info)
    return raiz

def arbol_num(raiz, info):
    if raiz is None:
        raiz = NodoArbol(info)
    elif info < raiz.info:
        raiz.der = arbol_num(raiz.der, info)
    else:
        raiz.izq = arbol_num(raiz.izq, info)
    return raiz

def crear_arboles(ruta):
    with open(ruta, 'r') as archivo:
        lector = reader(archivo)
        nombres, numeros, tipos = None, None, None
        for i in lector:
            if i != ['#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']:
                nombres = arbol_alpha(nombres, i[1])
                numeros = arbol_num(numeros, i[0])
                tipos = arbol_alpha(tipos, i[2])
    return nombres, numeros, tipos

def print_info(ruta, lista, nombre):
    sol = []
    if len(lista) == 0:
        return 'No se ha encontrado ningún Pokémon con los datos aportados.'
    for l in lista:
        with open(ruta, 'r') as archivo:
            lector = reader(archivo)
            for i in lector:
                for j in range(len(i)):
                    if i[j] == l.info:
                        if nombre == True and j != 3:
                            sol.append(i[1])
                            break
                        elif nombre == False:
                            sol.append('Pokémon número {}, {} de tipo {} y débil ante {} con\nTotal: {}.\nHP: {}.\nAttack: {}.\nDefense: {}.\nSp. Atk: {}.\nSp. Def: {}.\nSpeed: {}.\nGeneration: {}.\nLegendary: {}.'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
                            break
                        else:
                            break
    return sol

def buscar(raiz, clave, pos):
    if raiz is not None:
        if raiz.info == clave and raiz not in pos:
            pos.append(raiz)
        pos = buscar(raiz.izq, clave, pos)
        pos = buscar(raiz.der, clave, pos)
    return pos

def filtrar(raiz, clave, pos):
    if raiz is not None:
        if raiz.info.startswith(clave) and raiz not in pos:
            pos.append(raiz)
        pos = filtrar(raiz.izq, clave, pos)
        pos = filtrar(raiz.der, clave, pos)
    return pos

def valores_unicos(raiz, unicos):
    if raiz is not None:
        if raiz.info not in unicos:
            unicos[raiz.info] = 1
        else:
            unicos[raiz.info] = unicos[raiz.info] + 1
        unicos = valores_unicos(raiz.izq, unicos)
        unicos = valores_unicos(raiz.der, unicos)
    return unicos

def debil(ruta, raiz):
    sol = []
    with open(ruta, 'r') as archivo:
        lector = reader(archivo)
        for i in lector:
            if i[3] == raiz.info:
                sol.append(i[1])
    return sol