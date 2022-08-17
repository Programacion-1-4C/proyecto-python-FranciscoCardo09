import random
from Funciones_Preguntados import menu_1, menu_2, OPCIONES,OPCIONES2,lista_categorias_jugador_1,Info_jugador_2,Info_jugador_3,Info_jugador_4,lista_categorias_jugador_2,Info_jugador_1,preguntas_ciencia,preguntas_arte,preguntas_deporte,preguntas_geografia,preguntas_entretenimiento,preguntas_historia
if __name__ == "__main__":
    respuestas = 'Correctos'
    incorrectos = 0
    correctos = 0
    i = 1
    contador_correctos_jugador_1 = 0
    contador_correctos_jugador_2 = 0
    contador_correctos_jugador_3 = 0
    contador_correctos_jugador_4 = 0
    contador_incorrectos_jugador_1 = 0
    contador_incorrectos_jugador_2 = 0
    contador_incorrectos_jugador_3 = 0
    contador_incorrectos_jugador_4 = 0
    print('Elegi un modo de juego')
    desicion = menu_1(OPCIONES)
    if desicion == '1':
        print('Bien, preparado para jugar?')
        while 20 > correctos:
            numero_random_1 = random.randint(1, 6)
            numero_random_2 = random.randint(1, 20)
            if numero_random_1 == 1:
                correctos,incorrectos,respuestas = preguntas_deporte (numero_random_1,numero_random_2,correctos,incorrectos)
                print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
            elif numero_random_1 == 2:
                correctos,incorrectos,respuestas = preguntas_ciencia(numero_random_1, numero_random_2, correctos, incorrectos)
                print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
            elif numero_random_1 == 3:
                correctos,incorrectos,respuestas = preguntas_geografia(numero_random_1, numero_random_2, correctos, incorrectos)
                print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
            elif numero_random_1 == 4:
                correctos,incorrectos,respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2, correctos, incorrectos)
                print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
            elif numero_random_1 == 5:
                correctos,incorrectos,respuestas = preguntas_historia(numero_random_1, numero_random_2, correctos, incorrectos)
                print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
            elif numero_random_1 == 6:
                correctos,incorrectos,respuestas = preguntas_arte(numero_random_1, numero_random_2, correctos, incorrectos)
                print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
            if incorrectos == 3:
                print('Perdiste, seguí participando')
                break
    if desicion == '2':
        cant_de_jugadores = int(input('Cuantos jugadores van a jugar?(Maximo 4 jugadores)\n>>>'))
        rango = cant_de_jugadores + 1
        while i != 0:
            if i == rango:
                i = 1
            else:
                if i == 1:
                    while i == 1:
                        print(f'Turno del jugador 1')
                        print(Info_jugador_1)
                        numero_random_1 = random.randint(1, 7)
                        numero_random_2 = random.randint(1, 20)
                        if numero_random_1 == 1:
                            correctos,incorrectos,respuestas = preguntas_deporte(numero_random_1, numero_random_2, correctos, incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_1 += 1
                                if contador_correctos_jugador_1 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_1)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Deporte')
                                            Info_jugador_1['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Arte')
                                            Info_jugador_1['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Entretenimiento')
                                            Info_jugador_1['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Ciencia')
                                            Info_jugador_1['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Geografia')
                                            Info_jugador_1['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Historia')
                                            Info_jugador_1['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_1 += 1
                        elif numero_random_1 == 2:
                            correctos,incorrectos,respuestas = preguntas_ciencia(numero_random_1, numero_random_2, correctos, incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_1 += 1
                                if contador_correctos_jugador_1 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_1)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Deporte')
                                            Info_jugador_1['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Arte')
                                            Info_jugador_1['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Entretenimiento')
                                            Info_jugador_1['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Ciencia')
                                            Info_jugador_1['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Geografia')
                                            Info_jugador_1['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Historia')
                                            Info_jugador_1['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_1 += 1
                        elif numero_random_1 == 3:
                            correctos,incorrectos,respuestas = preguntas_geografia(numero_random_1, numero_random_2, correctos,incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_1 += 1
                                if contador_correctos_jugador_1 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_1)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Deporte')
                                            Info_jugador_1['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Arte')
                                            Info_jugador_1['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Entretenimiento')
                                            Info_jugador_1['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Ciencia')
                                            Info_jugador_1['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Geografia')
                                            Info_jugador_1['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Historia')
                                            Info_jugador_1['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_1 += 1
                        elif numero_random_1 == 4:
                            correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2,correctos, incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_1 += 1
                                if contador_correctos_jugador_1 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_1)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Deporte')
                                            Info_jugador_1['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Arte')
                                            Info_jugador_1['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,numero_random_2,correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Entretenimiento')
                                            Info_jugador_1['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Ciencia')
                                            Info_jugador_1['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Geografia')
                                            Info_jugador_1['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,numero_random_2, correctos,incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Historia')
                                            Info_jugador_1['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_1 += 1
                        elif numero_random_1 == 5:
                            correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,
                                                                                     correctos, incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_1 += 1
                                if contador_correctos_jugador_1 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_1)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1,
                                                                                               numero_random_2, correctos,
                                                                                               incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Deporte')
                                            Info_jugador_1['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1,
                                                                                            numero_random_2, correctos,
                                                                                            incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Arte')
                                            Info_jugador_1['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,
                                                                                                       numero_random_2,
                                                                                                       correctos,
                                                                                                       incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Entretenimiento')
                                            Info_jugador_1['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1,
                                                                                               numero_random_2, correctos,
                                                                                               incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Ciencia')
                                            Info_jugador_1['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,
                                                                                                 numero_random_2, correctos,
                                                                                                 incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Geografia')
                                            Info_jugador_1['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,
                                                                                                numero_random_2, correctos,
                                                                                                incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Historia')
                                            Info_jugador_1['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_1 += 1
                        elif numero_random_1 == 6:
                            correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,
                                                                                     correctos, incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_1 += 1
                                if contador_correctos_jugador_1 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_1)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1,
                                                                                               numero_random_2, correctos,
                                                                                               incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Deporte')
                                            Info_jugador_1['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1,
                                                                                            numero_random_2, correctos,
                                                                                            incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Arte')
                                            Info_jugador_1['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,
                                                                                                       numero_random_2,
                                                                                                       correctos,
                                                                                                       incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Entretenimiento')
                                            Info_jugador_1['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1,
                                                                                               numero_random_2, correctos,
                                                                                               incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Ciencia')
                                            Info_jugador_1['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,
                                                                                                 numero_random_2, correctos,
                                                                                                 incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Geografia')
                                            Info_jugador_1['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,
                                                                                                numero_random_2, correctos,
                                                                                                incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_1.remove('Historia')
                                            Info_jugador_1['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_1 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_1 += 1
                                            contador_correctos_jugador_1 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_1 += 1
                elif i == 2:
                    while i == 2:
                        print(f'Turno del jugador 2')
                        print(Info_jugador_2)
                        numero_random_1 = random.randint(1, 7)
                        numero_random_2 = random.randint(1, 20)
                        if numero_random_1 == 1:
                            correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2, correctos,incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_2 += 1
                                if contador_correctos_jugador_2 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_2)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2,correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Deporte')
                                            Info_jugador_2['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,
                                                                                            correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Arte')
                                            Info_jugador_2['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,
                                                                                                       numero_random_2, correctos,
                                                                                                       incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Entretenimiento')
                                            Info_jugador_2['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2,
                                                                                               correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Ciencia')
                                            Info_jugador_2['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2,
                                                                                                 correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Geografia')
                                            Info_jugador_2['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,
                                                                                                correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Historia')
                                            Info_jugador_2['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_2 += 1
                        elif numero_random_1 == 2:
                            correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2, correctos,
                                                                                   incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_2 += 1
                                if contador_correctos_jugador_2 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_2)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2,
                                                                                               correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Deporte')
                                            Info_jugador_2['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,
                                                                                            correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Arte')
                                            Info_jugador_2['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,
                                                                                                       numero_random_2, correctos,
                                                                                                       incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Entretenimiento')
                                            Info_jugador_2['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2,
                                                                                               correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Ciencia')
                                            Info_jugador_2['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2,
                                                                                                 correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Geografia')
                                            Info_jugador_2['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,
                                                                                                correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Historia')
                                            Info_jugador_2['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_2 += 1
                        elif numero_random_1 == 3:
                            correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2, correctos,
                                                                                     incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_2 += 1
                                if contador_correctos_jugador_2 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_2)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2,
                                                                                               correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Deporte')
                                            Info_jugador_2['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,
                                                                                            correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Arte')
                                            Info_jugador_2['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_1 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,
                                                                                                       numero_random_2, correctos,
                                                                                                       incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Entretenimiento')
                                            Info_jugador_2['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2,
                                                                                               correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Ciencia')
                                            Info_jugador_2['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2,
                                                                                                 correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Geografia')
                                            Info_jugador_2['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,
                                                                                                correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Historia')
                                            Info_jugador_2['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_2 += 1
                        elif numero_random_1 == 4:
                            correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2,
                                                                                           correctos, incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_2 += 1
                                if contador_correctos_jugador_2 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_2)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2,
                                                                                               correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Deporte')
                                            Info_jugador_2['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,
                                                                                            correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Arte')
                                            Info_jugador_2['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,
                                                                                                       numero_random_2, correctos,
                                                                                                       incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Entretenimiento')
                                            Info_jugador_2['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2,
                                                                                               correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Ciencia')
                                            Info_jugador_2['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2,
                                                                                                 correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Geografia')
                                            Info_jugador_2['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,
                                                                                                correctos, incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Historia')
                                            Info_jugador_2['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_2 += 1
                        elif numero_random_1 == 5:
                            correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,
                                                                                    correctos, incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_2 += 1
                                if contador_correctos_jugador_2 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_2)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1,
                                                                                               numero_random_2, correctos,
                                                                                               incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Deporte')
                                            Info_jugador_2['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1,
                                                                                            numero_random_2, correctos,
                                                                                            incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Arte')
                                            Info_jugador_2['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,
                                                                                                       numero_random_2,
                                                                                                       correctos,
                                                                                                       incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Entretenimiento')
                                            Info_jugador_2['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1,
                                                                                               numero_random_2, correctos,
                                                                                               incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Ciencia')
                                            Info_jugador_1['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,
                                                                                                 numero_random_2, correctos,
                                                                                                 incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Geografia')
                                            Info_jugador_2['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,
                                                                                                numero_random_2, correctos,
                                                                                                incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Historia')
                                            Info_jugador_2['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_2 += 1
                        elif numero_random_1 == 6:
                            correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,
                                                                                correctos, incorrectos)
                            if respuestas == 'Correcto':
                                contador_correctos_jugador_2 += 1
                                if contador_correctos_jugador_2 == 3:
                                    print('Elegí la categoria')
                                    print(lista_categorias_jugador_2)
                                    eleccion = input('>>>')
                                    if eleccion == 'Deporte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1,
                                                                                               numero_random_2, correctos,
                                                                                               incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Deporte')
                                            Info_jugador_2['Deporte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Arte':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_arte(numero_random_1,
                                                                                            numero_random_2, correctos,
                                                                                            incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Arte')
                                            Info_jugador_2['Arte'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Entretenimiento':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,
                                                                                                       numero_random_2,
                                                                                                       correctos,
                                                                                                       incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Entretenimiento')
                                            Info_jugador_2['Entretenimiento'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Ciencia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1,
                                                                                               numero_random_2, correctos,
                                                                                               incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Ciencia')
                                            Info_jugador_2['Ciencia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Geografia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,
                                                                                                 numero_random_2, correctos,
                                                                                                 incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Geografia')
                                            Info_jugador_2['Greografia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                    if eleccion == 'Historia':
                                        numero_random_2 = random.randint(1, 20)
                                        correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,
                                                                                                numero_random_2, correctos,
                                                                                                incorrectos)
                                        if respuestas == 'Correcto':
                                            lista_categorias_jugador_2.remove('Historia')
                                            Info_jugador_1['Historia'] = 'Ganado'
                                            i += 1
                                            contador_correctos_jugador_2 = 0
                                        elif respuestas == 'Incorrecto':
                                            i += 1
                                            contador_incorrectos_jugador_2 += 1
                                            contador_correctos_jugador_2 = 0
                                else:
                                    continue
                            elif respuestas == 'Incorrecto':
                                i += 1
                                contador_incorrectos_jugador_2 += 1


