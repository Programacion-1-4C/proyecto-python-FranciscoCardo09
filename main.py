import random
from Funciones_Preguntados import menu_1, menu_2, OPCIONES, OPCIONES2, CATEGORIAS, preguntas, mostrar_info_jugador, \
    elegir_categoria, categorias_faltan, CATEGORIAS_TEMATICAS, preguntas_tematicas

if __name__ == "__main__":
    incorrectos = 0
    correctos = 0
    print('Elegi un modo de juego')
    desicion = menu_1(OPCIONES)
    if desicion == '1':
        print('Bien, preparado para jugar?')
        while correctos < 20:
            cat_elegida = random.randint(0, len(CATEGORIAS)-1)
            respuesta = preguntas(CATEGORIAS[cat_elegida])
            if respuesta:
                correctos += 1
            else:
                incorrectos += 1
            print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
            if incorrectos == 3:
                print('Perdiste, seguí participando')
                break
    if desicion == '2':
        cant_de_jugadores = int(input('Cuantos jugadores van a jugar?(Maximo 4 jugadores)\n>>>'))
        rango = cant_de_jugadores + 1
        info_jugador = [{x: False for x in CATEGORIAS} for i in range(rango)]
        i = 1
        CORONITA = len(CATEGORIAS)
        while i != 0:
            if i == rango:
                i = 1
            else:
                correctos = 0
                incorrectos = 0
                mostrar_info_jugador(info_jugador[i-1], i)
                turno_actual = i
                while i == turno_actual:
                    print(f'\nTurno del jugador {i}')
                    cat_elegida = random.randint(0, CORONITA)
                    if cat_elegida != CORONITA:
                        respuesta = preguntas(CATEGORIAS[cat_elegida])

                        if respuesta:
                            correctos += 1
                            corrio = elegir_categoria(correctos, info_jugador[i-1])
                            if corrio:
                                i += 1
                        else:
                            incorrectos += 1
                            i += 1
                    else:
                        print('Coronita\nElegí la categoria')
                        correctos = 3
                        elegir_categoria(correctos, info_jugador[i-1])
                        i += 1
                if not categorias_faltan(info_jugador[i-1]):
                    print(f'Jugador {i} es el ganador')
                    break
    elif desicion == '3':
        desicion2 = menu_2(OPCIONES2)
        while correctos < 20:
            cat_elegida = desicion2
            respuesta = preguntas_tematicas(CATEGORIAS_TEMATICAS[cat_elegida])
            if respuesta:
                correctos += 1
            else:
                incorrectos += 1
            print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3\n')
            if incorrectos == 3:
                print('Perdiste, seguí participando')
                break
