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
            print('\nMi tabla de símbolos es', simbolos)
            print('Con sus correspondientes frecuencias', frecuencias)
            print('\nObtenemos los siguientes códigos por cada símbolo:')
            print('A: ', ejercicio1.comprimir('A', raiz))
            print('F: ', ejercicio1.comprimir('F', raiz))
            print('1: ', ejercicio1.comprimir('1', raiz))
            print('3: ', ejercicio1.comprimir('3', raiz))
            print('0: ', ejercicio1.comprimir('0', raiz))
            print('M: ', ejercicio1.comprimir('M', raiz))
            print('T: ', ejercicio1.comprimir('T', raiz))
            print('\nSi codificamos la palabra M0T0 obtenemos el siguiente resultado:', ejercicio1.comprimir('M0T0', raiz))
            print('Si decodificamos ese código obtenemos la palabra inicial:', ejercicio1.descomprimir('101110101101010', raiz), '\n')

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
                    print('\n', '\n\n'.join(ejercicio2.print_info(ruta, ejercicio2.buscar(numeros, n, pos = []), False)), '\n')
                    
                elif apartado == '2':
                    print('\nIntroduce el nombre de Pokémon que quiere buscar:')
                    n = input('> ')
                    print('\n', '\n\n'.join(ejercicio2.print_info(ruta, ejercicio2.filtrar(nombres, n, pos = []), False)), '\n')

                elif apartado == '3':
                    while True:
                        print('\n¿Qué tipo de Pokémon quiere mostrar? ¿Fire? ¿Water? ¿Grass? ¿Electric?')
                        print('Inserta el tipo de Pokémon que quiere mostrar de los nombrados anteriormente:')
                        tipo = input('> ')
                        if len(ejercicio2.buscar(tipos, tipo, pos = [])) is 0:
                            print('No ha insertado un tipo de Pokémon correcto, inténtelo de nuevo.')
                        else:
                            print('\n', ', '.join(ejercicio2.print_info(ruta, ejercicio2.buscar(tipos, tipo, pos = []), True)), '.\n')
                            break

                elif apartado == '4':
                    print('Apartado no hecho')

                elif apartado == '5':
                    print('Apartado no hecho')

                elif apartado == '6':
                    print('\n¿Frente a qué Pokémon quiere ver que sean débiles otros Pokémons? ¿Jolteon? ¿Lycanroc? ¿Tyrantrum?')
                    print('Inserta un Pokémon que quiere de los nombrados anteriormente:')
                    pok = input('> ')

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
            print('Ejercicio no hecho')

        elif opcion == '4':
            print('\nSaliendo...')
            break 

        else:
            print('\nTiene que seleccionar una opción correcta, inténtelo de nuevo.\n')
