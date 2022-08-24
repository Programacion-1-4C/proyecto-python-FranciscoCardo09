import random
from Funciones_Preguntados import menu_1, menu_2, OPCIONES, OPCIONES2, lista_categorias_jugador_1, Info_jugador_2, \
    jugador_1, jugador_2, jugador_3, jugador_4, Info_jugador_3, Info_jugador_4, lista_categorias_jugador_2, \
    Info_jugador_1, preguntas_ciencia, \
    preguntas_arte, preguntas_deporte, preguntas_geografia, lista_ganadora, preguntas_entretenimiento, \
    preguntas_historia, \
    lista_categorias_jugador_3, lista_categorias_jugador_4, coronita_jugador_1_Arte, coronita_jugador_1_Ciencia, \
    coronita_jugador_1_Entretenimiento, \
    coronita_jugador_1_Deporte, coronita_jugador_1_Geografia, coronita_jugador_1_Historia \
    , coronita_jugador_2_Entretenimiento, coronita_jugador_2_Ciencia, coronita_jugador_2_Historia, \
    coronita_jugador_2_Deporte, \
    coronita_jugador_2_Geografia, coronita_jugador_2_Arte, coronita_jugador_3_Arte, coronita_jugador_3_Ciencia, \
    coronita_jugador_3_Deporte, \
    coronita_jugador_3_Entretenimiento, coronita_jugador_3_Geografia, coronita_jugador_3_Historia, \
    coronita_jugador_4_Arte, \
    coronita_jugador_4_Ciencia, coronita_jugador_4_Deporte, coronita_jugador_4_Entretenimiento, \
    coronita_jugador_4_Geografia, coronita_jugador_4, CATEGORIAS, preguntas, coronita_jugador

if __name__ == "__main__":
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
                correctos,incorrectos,respuestas = preguntas_deporte(numero_random_1,numero_random_2,correctos,incorrectos)
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
                    print(Info_jugador_1)
                    while i == 1:
                        print(f'Turno del jugador 1')
                        numero_random_1 = random.randint(1, 7)
                        numero_random_2 = random.randint(1, 20)
                        if numero_random_1 == 1:
                            correctos,incorrectos,respuestas = preguntas_deporte(numero_random_1, numero_random_2, correctos, incorrectos)
                            contador_correctos_jugador_1, contador_incorrectos_jugador_1, i, respuestas, lista_categorias_jugador_1, Info_jugador_1 = jugador_1(respuestas,contador_correctos_jugador_1,contador_incorrectos_jugador_1,correctos,incorrectos,i)
                        elif numero_random_1 == 2:
                            correctos,incorrectos,respuestas = preguntas_ciencia(numero_random_1, numero_random_2, correctos, incorrectos)
                            contador_correctos_jugador_1, contador_incorrectos_jugador_1, i, respuestas, lista_categorias_jugador_1, Info_jugador_1 = jugador_1(respuestas,contador_correctos_jugador_1,contador_incorrectos_jugador_1,correctos,incorrectos,i)
                        elif numero_random_1 == 3:
                            correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_1, contador_incorrectos_jugador_1, i, respuestas, lista_categorias_jugador_1, Info_jugador_1 = jugador_1(respuestas,contador_correctos_jugador_1,contador_incorrectos_jugador_1,correctos,incorrectos,i)
                        elif numero_random_1 == 4:
                            correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_1, contador_incorrectos_jugador_1, i, respuestas, lista_categorias_jugador_1, Info_jugador_1 = jugador_1(respuestas,contador_correctos_jugador_1,contador_incorrectos_jugador_1,correctos,incorrectos,i)
                        elif numero_random_1 == 5:
                            correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_1, contador_incorrectos_jugador_1, i, respuestas, lista_categorias_jugador_1, Info_jugador_1 = jugador_1(respuestas,contador_correctos_jugador_1,contador_incorrectos_jugador_1,correctos,incorrectos,i)
                        elif numero_random_1 == 6:
                            correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_1, contador_incorrectos_jugador_1, i, respuestas, lista_categorias_jugador_1, Info_jugador_1 = jugador_1(respuestas,contador_correctos_jugador_1,contador_incorrectos_jugador_1,correctos,incorrectos,i)
                        elif numero_random_1 == 7:
                            print('Coronita\nElegí la categoria')
                            print(lista_categorias_jugador_1)
                            eleccion = input('>>>')
                            if eleccion == 'Deporte' or eleccion == 'deporte':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2,correctos,incorrectos)
                                i, lista_categorias_jugador_1, Info_jugador_1, contador_correctos_jugador_1 = coronita_jugador_1_Deporte(respuestas,contador_correctos_jugador_1,contador_incorrectos_jugador_1,i)
                            elif eleccion == 'Arte' or eleccion == 'arte':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_1, Info_jugador_1, contador_correctos_jugador_1 = coronita_jugador_1_Arte(respuestas, contador_correctos_jugador_1, contador_incorrectos_jugador_1, i)
                            elif eleccion == 'Ciencia' or eleccion == 'ciencia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_1, Info_jugador_1, contador_correctos_jugador_1 = coronita_jugador_1_Ciencia(respuestas, contador_correctos_jugador_1, contador_incorrectos_jugador_1, i)
                            elif eleccion == 'Entretenimiento' or eleccion == 'entretenimiento':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_1, Info_jugador_1, contador_correctos_jugador_1 = coronita_jugador_1_Entretenimiento(respuestas, contador_correctos_jugador_1, contador_incorrectos_jugador_1, i)
                            elif eleccion == 'Geografia' or eleccion == 'geografia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_1, Info_jugador_1, contador_correctos_jugador_1 = coronita_jugador_1_Geografia(respuestas, contador_correctos_jugador_1, contador_incorrectos_jugador_1, i)
                            elif eleccion == 'Historia' or eleccion == 'historia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_1, Info_jugador_1, contador_correctos_jugador_1 = coronita_jugador_1_Historia(respuestas, contador_correctos_jugador_1, contador_incorrectos_jugador_1, i)
                elif i == 2:
                    print(Info_jugador_2)
                    while i == 2:
                        print(f'Turno del jugador 2')
                        numero_random_1 = random.randint(1, 7)
                        numero_random_2 = random.randint(1, 20)
                        if numero_random_1 == 1:
                            correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2, correctos,incorrectos)
                            contador_correctos_jugador_2,contador_incorrectos_jugador_2,i,respuestas,lista_categorias_jugador_2,Info_jugador_2 = jugador_2(respuestas,contador_correctos_jugador_2,contador_incorrectos_jugador_2,correctos,incorrectos,i)
                        elif numero_random_1 == 2:
                            correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2, correctos,incorrectos)
                            contador_correctos_jugador_2,contador_incorrectos_jugador_2,i,respuestas,lista_categorias_jugador_2,Info_jugador_2 = jugador_2(respuestas,contador_correctos_jugador_2,contador_incorrectos_jugador_2,correctos,incorrectos,i)
                        elif numero_random_1 == 3:
                            correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2, correctos,incorrectos)
                            contador_correctos_jugador_2,contador_incorrectos_jugador_2,i,respuestas,lista_categorias_jugador_2,Info_jugador_2 = jugador_2(respuestas,contador_correctos_jugador_2,contador_incorrectos_jugador_2,correctos,incorrectos,i)
                        elif numero_random_1 == 4:
                            correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_2,contador_incorrectos_jugador_2,i,respuestas,lista_categorias_jugador_2,Info_jugador_2 = jugador_2(respuestas,contador_correctos_jugador_2,contador_incorrectos_jugador_2,correctos,incorrectos,i)
                        elif numero_random_1 == 5:
                            correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_2,contador_incorrectos_jugador_2,i,respuestas,lista_categorias_jugador_2,Info_jugador_2 = jugador_2(respuestas,contador_correctos_jugador_2,contador_incorrectos_jugador_2,correctos,incorrectos,i)
                        elif numero_random_1 == 6:
                            correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_2,contador_incorrectos_jugador_2,i,respuestas,lista_categorias_jugador_2,Info_jugador_2 = jugador_2(respuestas,contador_correctos_jugador_2,contador_incorrectos_jugador_2,correctos,incorrectos,i)
                        elif numero_random_1 == 7:
                            print('Coronita\nElegí la categoria')
                            print(lista_categorias_jugador_2)
                            eleccion = input('>>>')
                            if eleccion == 'Deporte' or eleccion == 'deporte':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_2, Info_jugador_2, contador_correctos_jugador_2 = coronita_jugador_2_Deporte(respuestas, contador_correctos_jugador_2, contador_incorrectos_jugador_2,i)
                            elif eleccion == 'Arte' or eleccion == 'arte':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2, correctos, incorrectos)
                                i, lista_categorias_jugador_2, Info_jugador_2,contador_correctos_jugador_2 = coronita_jugador_2_Arte(respuestas, contador_correctos_jugador_2, contador_incorrectos_jugador_2,i)
                            elif eleccion == 'Ciencia' or eleccion == 'ciencia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2, correctos, incorrectos)
                                i, lista_categorias_jugador_2, Info_jugador_2,contador_correctos_jugador_2 = coronita_jugador_2_Ciencia(respuestas, contador_correctos_jugador_2, contador_incorrectos_jugador_2,i)
                            elif eleccion == 'Entretenimiento' or eleccion == 'entretenimiento':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2, correctos, incorrectos)
                                i, lista_categorias_jugador_2, Info_jugador_2,contador_correctos_jugador_2 = coronita_jugador_2_Entretenimiento(respuestas, contador_correctos_jugador_2, contador_incorrectos_jugador_2,i)
                            elif eleccion == 'Geografia' or eleccion == 'geografia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,numero_random_2, correctos,incorrectos)
                                i, lista_categorias_jugador_2, Info_jugador_2,contador_correctos_jugador_2 = coronita_jugador_2_Geografia(respuestas, contador_correctos_jugador_2, contador_incorrectos_jugador_2,i)
                            elif eleccion == 'Historia' or eleccion == 'historia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2, correctos, incorrectos)
                                i, lista_categorias_jugador_2, Info_jugador_2,contador_correctos_jugador_2 = coronita_jugador_2_Historia(respuestas, contador_correctos_jugador_2, contador_incorrectos_jugador_2,i)
                elif i == 3:
                    print(Info_jugador_3)
                    while i == 3:
                        print(f'Turno del jugador 3')
                        numero_random_1 = random.randint(1, 7)
                        numero_random_2 = random.randint(1, 20)
                        if numero_random_1 == 1:
                            correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2, correctos,incorrectos)
                            contador_correctos_jugador_3,contador_incorrectos_jugador_3,i,respuestas,lista_categorias_jugador_3,Info_jugador_3 = jugador_3(respuestas,contador_correctos_jugador_3,contador_incorrectos_jugador_3,correctos,incorrectos,i)
                        elif numero_random_1 == 2:
                            correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_3, contador_incorrectos_jugador_3, i, respuestas, lista_categorias_jugador_3, Info_jugador_3 = jugador_3(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, correctos, incorrectos, i)
                        elif numero_random_1 == 3:
                            correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_3, contador_incorrectos_jugador_3, i, respuestas, lista_categorias_jugador_3, Info_jugador_3 = jugador_3(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, correctos, incorrectos, i)
                        elif numero_random_1 == 4:
                            correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_3, contador_incorrectos_jugador_3, i, respuestas, lista_categorias_jugador_3, Info_jugador_3 = jugador_3(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, correctos, incorrectos, i)
                        elif numero_random_1 == 5:
                            correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_3, contador_incorrectos_jugador_3, i, respuestas, lista_categorias_jugador_3, Info_jugador_3 = jugador_3(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, correctos, incorrectos, i)
                        elif numero_random_1 == 6:
                            correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_3, contador_incorrectos_jugador_3, i, respuestas, lista_categorias_jugador_3, Info_jugador_3 = jugador_3(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, correctos, incorrectos, i)
                        elif numero_random_1 == 7:
                            print('Coronita\nElegí la categoria')
                            print(lista_categorias_jugador_3)
                            eleccion = input('>>>')
                            if eleccion == 'Deporte' or eleccion == 'deporte':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2, correctos, incorrectos)
                                i, lista_categorias_jugador_3, Info_jugador_3, contador_correctos_jugador_3 = coronita_jugador_3_Deporte(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, i)
                            elif eleccion == 'Arte' or eleccion == 'arte':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_3, Info_jugador_3, contador_correctos_jugador_3 = coronita_jugador_3_Arte(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, i)
                            elif eleccion == 'Ciencia' or eleccion == 'ciencia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2, correctos, incorrectos)
                                i, lista_categorias_jugador_3, Info_jugador_3, contador_correctos_jugador_3 = coronita_jugador_3_Ciencia(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, i)
                            elif eleccion == 'Entretenimiento' or eleccion == 'entretenimiento':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_3, Info_jugador_3, contador_correctos_jugador_3 = coronita_jugador_3_Entretenimiento(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, i)
                            elif eleccion == 'Geografia' or eleccion == 'geografia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,numero_random_2, correctos,incorrectos)
                                i, lista_categorias_jugador_3, Info_jugador_3, contador_correctos_jugador_3 = coronita_jugador_3_Geografia(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, i)
                            elif eleccion == 'Historia' or eleccion == 'historia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,numero_random_2, correctos,incorrectos)
                                i, lista_categorias_jugador_3, Info_jugador_3, contador_correctos_jugador_3 = coronita_jugador_3_Historia(respuestas, contador_correctos_jugador_3, contador_incorrectos_jugador_3, i)
                elif i == 4:
                    print(Info_jugador_4)
                    while i == 4:
                        print(f'Turno del jugador 4')
                        numero_random_1 = random.randint(1, 7)
                        numero_random_2 = random.randint(1, 20)
                        if numero_random_1 == 1:
                            correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2, correctos,incorrectos)
                            contador_correctos_jugador_4,contador_incorrectos_jugador_4,i,respuestas,lista_categorias_jugador_4,Info_jugador_4 = jugador_4(respuestas,contador_correctos_jugador_4,contador_incorrectos_jugador_4,correctos,incorrectos,i)
                        elif numero_random_1 == 2:
                            correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_4, contador_incorrectos_jugador_4, i, respuestas, lista_categorias_jugador_4, Info_jugador_4 = jugador_4(respuestas, contador_correctos_jugador_4, contador_incorrectos_jugador_4,correctos,incorrectos, i)
                        elif numero_random_1 == 3:
                            correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_4, contador_incorrectos_jugador_4, i, respuestas, lista_categorias_jugador_4, Info_jugador_4 = jugador_4(respuestas, contador_correctos_jugador_4, contador_incorrectos_jugador_4,correctos,incorrectos, i)
                        elif numero_random_1 == 4:
                            correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_4, contador_incorrectos_jugador_4, i, respuestas, lista_categorias_jugador_4, Info_jugador_4 = jugador_4(respuestas, contador_correctos_jugador_4, contador_incorrectos_jugador_4,correctos,incorrectos, i)
                        elif numero_random_1 == 5:
                            correctos, incorrectos, respuestas = preguntas_historia(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_4, contador_incorrectos_jugador_4, i, respuestas, lista_categorias_jugador_4, Info_jugador_4 = jugador_4(respuestas, contador_correctos_jugador_4, contador_incorrectos_jugador_4,correctos,incorrectos, i)
                        elif numero_random_1 == 6:
                            correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,correctos, incorrectos)
                            contador_correctos_jugador_4, contador_incorrectos_jugador_4, i, respuestas, lista_categorias_jugador_4, Info_jugador_4 = jugador_4(respuestas, contador_correctos_jugador_4, contador_incorrectos_jugador_4,correctos,incorrectos, i)
                        elif numero_random_1 == 7:
                            print('Coronita\nElegí la categoria')
                            print(lista_categorias_jugador_4)
                            eleccion = input('>>>')
                            eleccion = eleccion.capitalize()
                            if eleccion in CATEGORIAS:
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuesta = preguntas(numero_random_1, numero_random_2, eleccion)
                                i, lista_categorias_jugador_4, Info_jugador_4,contador_correctos_jugador_4 = coronita_jugador(respuesta, contador_incorrectos_jugador_4, lista_categorias, info_jugador, categoria)
                            if eleccion == 'Deporte' or eleccion == 'deporte':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_deporte(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_4, Info_jugador_4,contador_correctos_jugador_4 = coronita_jugador_4_Deporte(respuestas,contador_correctos_jugador_4,contador_incorrectos_jugador_4,i)
                            elif eleccion == 'Arte' or eleccion == 'arte':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_arte(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_4, Info_jugador_4,contador_correctos_jugador_4 = coronita_jugador_4_Arte(respuestas,contador_correctos_jugador_4,contador_incorrectos_jugador_4,i)
                            elif eleccion == 'Ciencia' or eleccion == 'ciencia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_ciencia(numero_random_1, numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_4, Info_jugador_4,contador_correctos_jugador_4 = coronita_jugador_4(respuestas,contador_correctos_jugador_4,contador_incorrectos_jugador_4,i)
                            elif eleccion == 'Entretenimiento' or eleccion == 'entretenimiento':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_entretenimiento(numero_random_1,numero_random_2,correctos, incorrectos)
                                i, lista_categorias_jugador_4, Info_jugador_4,contador_correctos_jugador_4 = coronita_jugador_4(respuestas,contador_correctos_jugador_4,contador_incorrectos_jugador_4,i)
                            elif eleccion == 'Geografia' or eleccion == 'geografia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_geografia(numero_random_1,numero_random_2, correctos,incorrectos)
                                i, lista_categorias_jugador_4, Info_jugador_4,contador_correctos_jugador_4 = coronita_jugador_4(respuestas,contador_correctos_jugador_4,contador_incorrectos_jugador_4,i)
                            elif eleccion == 'Historia' or eleccion == 'historia':
                                numero_random_1 = random.randint(1, 6)
                                numero_random_2 = random.randint(1, 20)
                                correctos, incorrectos, respuestas = preguntas_historia(numero_random_1,numero_random_2, correctos,incorrectos)
                                i, lista_categorias_jugador_4, Info_jugador_4,contador_correctos_jugador_4 = coronita_jugador_4(respuestas,contador_correctos_jugador_4,contador_incorrectos_jugador_4,i, "Historia")
                if lista_categorias_jugador_1 == lista_ganadora:
                    print('Jugador 1 es el ganador')
                    break
                elif lista_categorias_jugador_2 == lista_ganadora:
                    print('Jugador 2 es el ganador')
                    break
                elif lista_categorias_jugador_3 == lista_ganadora:
                    print('Jugador 3 es el ganador')
                    break
                elif lista_categorias_jugador_4 == lista_ganadora:
                    print('Jugador 4 es el ganador')
                    break
                else:
                    pass
    elif desicion == '3':
        desicion2 = menu_2(OPCIONES2)
        if desicion2 == '1':
            pass
