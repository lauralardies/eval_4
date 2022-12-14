import ejercicio1, ejercicio2, ejercicio3

def iniciar():

    while True:

        print('-------------------------------------')
        print('------ Ejercicios Evaluación 4 ------')
        print('-------------------------------------')
        print('[1] Ejercicio 1: Comprimir mensajes.')
        print('[2] Ejercicio 2: Pokémons.')
        print('[3] Ejercicio 3: Las 7 maravillas.')
        print('[4] Salir del menú.')

        opcion = input('> ')

        if opcion == '1':
            print('\nBienvenido al ejericio 1...')
            simbolos = ['A', 'F', '1', '3', '0', 'M', 'T']
            frecuencias = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
            raiz = ejercicio1.arbol_huffman(simbolos, frecuencias)
            print('\nObtenemos los siguientes códigos por cada símbolo:')
            print('A: ', ejercicio1.comprimir('A', raiz))
            print('F: ', ejercicio1.comprimir('F', raiz))
            print('1: ', ejercicio1.comprimir('1', raiz))
            print('3: ', ejercicio1.comprimir('3', raiz))
            print('0: ', ejercicio1.comprimir('0', raiz))
            print('M: ', ejercicio1.comprimir('M', raiz))
            print('T: ', ejercicio1.comprimir('T', raiz))
            print('\nSi codificamos la palabra M0T0 obtenemos el siguiente resultado:', ejercicio1.comprimir('M0T0', raiz))
            print('Si decodificamos ese código obtenemos la palabra inicial:', ejercicio1.descomprimir(ejercicio1.comprimir('M0T0', raiz), raiz), '\n')

            while True:
                print('¿Quiere codificar algún mensaje? [Y]/N')
                eleccion = input('> ')
                if eleccion.upper() == 'N':
                    print('\nVolviendo al menú principal...\n')
                    break
                else:
                    print('\nMi tabla de símbolos es', simbolos)
                    print('\nIntroduce un mensaje con los símbolos de la tabla')
                    mensaje = input('> ')
                    for m in mensaje:
                        if m not in simbolos:
                            print('\nNo ha introducido un string válido.\n')
                            break
                        else:
                            print('\nSi codificamos la palabra ', mensaje, ' obtenemos el siguiente resultado:', ejercicio1.comprimir(mensaje, raiz))
                            print('Si decodificamos ese código obtenemos la palabra inicial:', ejercicio1.descomprimir(ejercicio1.comprimir(mensaje, raiz), raiz), '\n')
                            break
                        
        elif opcion == '2':
            print('\nBienvenido al ejericio 2...')
            print('---------------------------')
            while True:

                print('[1] Buscar Pokémon por número.')
                print('[2] Buscar Pokémon por nombre.')
                print('[3] Filtrar Pokémon por tipo (Fuego, Agua, Planta y Eléctrico).')
                print('[4] Listado por nombre y número de Pokémon.')
                print('[5] Listado por nivel por nombre.')
                print('[6] Pokémons débiles a otros (Jolteon, Lycanroc y Tyrantrum).')
                print('[7] Mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.')
                print('[8] Hacer otro ejercicio.')

                ruta = 'Evaluación 4/Ejercicios/pokemon.csv'
                nombres, numeros, tipos = ejercicio2.crear_arboles(ruta)
                apartado = input('> ')

                if apartado == '1':
                    print('\nIntroduce el número de Pokémon que quiere buscar:')
                    n = input('> ')
                    print('\n', ejercicio2.print_info(ruta, ejercicio2.buscar(numeros, n, pos = []), False), '\n')
                    
                elif apartado == '2':
                    print('\nIntroduce el nombre de Pokémon que quiere buscar:')
                    n = input('> ')
                    print('\n', ejercicio2.print_info(ruta, ejercicio2.filtrar(nombres, n, pos = []), False), '\n')

                elif apartado == '3':
                    while True:
                        print('\n¿Qué tipo de Pokémon quiere mostrar? ¿Fire? ¿Water? ¿Grass? ¿Electric?')
                        print('Inserta el tipo de Pokémon que quiere mostrar de los nombrados anteriormente:')
                        tipo = input('> ')
                        if tipo != 'Fire' and tipo != 'Water' and tipo != 'Grass' and tipo != 'Electric':
                            print('No ha insertado un tipo de Pokémon correcto, inténtelo de nuevo.')
                        else:
                            print('\nLos Pokémon tipo ', tipo, ' son:')
                            print(ejercicio2.print_info(ruta, ejercicio2.buscar(tipos, tipo, pos = []), True), '\n')
                            break

                elif apartado == '4':
                    nombres_ordenados = ejercicio2.ordenar_arbol(nombres, lista_ordenada = [])
                    nom_num = ejercicio2.cambiar_arbol(ruta, nombres_ordenados)
                    nom_num_ordenados = ejercicio2.ordenar_arbol(nom_num, lista_ordenada = [])
                    print('\n', ejercicio2.print_info(ruta, nom_num_ordenados, nombre = True), '.\n')

                elif apartado == '5':
                    lista = ejercicio2.listado_por_nivel(nombres)
                    print('\n')
                    for i in range(len(lista)):
                        print('Nivel ', i+1, ':', ejercicio2.print_info(ruta, lista[i], nombre = True), '.')
                    print('\n')

                elif apartado == '6':
                    while True:
                        print('\n¿Frente a qué Pokémon quiere ver que sean débiles otros Pokémons? ¿Jolteon? ¿Lycanroc? ¿Tyrantrum?')
                        print('Inserta un Pokémon de los nombrados anteriormente:')
                        pok = input('> ')
                        if pok != 'Jolteon' and pok != 'Lycanroc' and pok != 'Tyrantrum':
                            print('No ha insertado un Pokémon de los mencionados anteriormente. Inténtelo de nuevo')
                        else:
                            nombre = ejercicio2.buscar(nombres, pok, pos = [])
                            if len(nombre) != 0:
                                tipo = ejercicio2.buscar_tipo(ruta, nombre[0])
                                print('\nLos Pokémons débiles ante ', pok, 'son:')
                                print(ejercicio2.print_info(ruta, ejercicio2.debil(ruta, tipo), nombre = True), '.\n')
                            else:
                                print('\nEl Pokémon nombrado no se ecuentra en nuestros datos.\n')
                            break

                elif apartado == '7':
                    dictio = ejercicio2.valores_unicos(tipos, unicos = {})
                    print('\nLos tipos de Pokémons son los siguientes:')
                    for tipo in dictio:
                        print(tipo, ':', dictio[tipo], '.')
                    print('\n')

                elif apartado == '8':
                    print('\nVolviendo al menú principal...\n')
                    break

                else:
                    print('\nTiene que seleccionar una opción correcta, inténtelo de nuevo.\n')
        
        elif opcion == '3':
            print('\nBienvenido al ejericio 3...')
            maravillas = ejercicio3.Grafo()
            maravillas = ejercicio3.crear_grafo(maravillas)
            aristas_azules = ejercicio3.matriz_adyacencia(maravillas, maravillas.inicio, 'Azul')
            aristas_amarillas = ejercicio3.matriz_adyacencia(maravillas, maravillas.inicio, 'Amarilla')

        elif opcion == '4':
            print('\nSaliendo...')
            break 

        else:
            print('\nTiene que seleccionar una opción correcta, inténtelo de nuevo.\n')
