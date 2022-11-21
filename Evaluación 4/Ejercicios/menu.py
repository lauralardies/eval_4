import ejercicio1, ejercicio2, ejercicio3

def iniciar():

    while True:

        print('-------------------------------------')
        print('------ Ejercicios Evaluación 4 ------')
        print('-------------------------------------')
        print('[1] Ejercicio 1: Comprimir mensajes')
        print('[2] Ejercicio 2: Pokémons')
        print('[3] Ejercicio 3: Las 7 maravillas')
        print('[4] Salir del menú')

        opcion = input('> ')

        if opcion == '1':
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
            print('Si decodificamos ese código obtenemos la palabra inicial:', ejercicio1.descomprimir('101110101101010', raiz))

        elif opcion == '2':
            pass

        elif opcion == '3':
            pass

        elif opcion == '4':
            print('\nSaliendo...')
            break

        else:
            print('\nTiene que seleccionar una opción correcta, inténtelo de nuevo\n')
