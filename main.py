import random
from Funciones_Preguntados import menu_1, menu_2, OPCIONES,OPCIONES2,preguntas_ciencia,preguntas_deporte,preguntas_geografia

if __name__ == "__main__":
    incorrectos = 0
    correctos = 0
    print('Elegi un modo de juego')
    desicion = menu_1(OPCIONES)
    if desicion == '1':
        print('Bien, preparado para jugar?')
        while 20 > correctos:
            numero_random_1 = random.randint(1, 6)
            numero_random_2 = random.randint(1, 20)
            if numero_random_1 == 1:
                correctos,incorrectos = preguntas_deporte (numero_random_1,numero_random_2,correctos,incorrectos)
            elif numero_random_1 == 2:
                correctos,incorrectos = preguntas_ciencia(numero_random_1, numero_random_2, correctos, incorrectos)
            elif numero_random_1 == 3:
                correctos,incorrectos = preguntas_geografia(numero_random_1, numero_random_2, correctos, incorrectos)
            elif numero_random_1 == 4:
                pass
            elif numero_random_1 == 5:
                pass
            elif numero_random_1 == 6:
                pass
            if incorrectos == 3:
                print('Perdiste, seguí participando')
                break
    if desicion == '2':
        cant_de_jugadores = int(input('Cuantos jugadores van a jugar?(Maximo 4 jugadores)\n>>>'))
        for i in range(cant_de_jugadores):
            numero_random_1 = random.randint(1, 6)
            numero_random_2 = random.randint(1, 20)
            if i == 1:
                print(f'Turno del jugador{i}')
                if numero_random_1 == 1:
                    correctos, incorrectos = preguntas_deporte(numero_random_1, numero_random_2, correctos, incorrectos)
                elif numero_random_1 == 2:
                    correctos, incorrectos = preguntas_ciencia(numero_random_1, numero_random_2, correctos, incorrectos)
                elif numero_random_1 == 3:
                    correctos, incorrectos = preguntas_geografia(numero_random_1, numero_random_2, correctos,incorrectos)
                elif numero_random_1 == 4:
                    pass
                elif numero_random_1 == 5:
                    pass
                elif numero_random_1 == 6:
                    pass
