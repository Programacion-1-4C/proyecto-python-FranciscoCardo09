import random
from Funciones_Preguntados import menu_1, menu_2, OPCIONES,OPCIONES2,preguntas_ciencia,preguntas_deporte,preguntas_geografia

if __name__ == "__main__":
    incorrectos = 0
    correctos = 0
    desicion = menu_1(OPCIONES)
    if desicion == '1':
        while 20 > correctos:
            numero_random_1 = random.randint(1, 6)
            numero_random_2 = random.randint(1, 20)
            if numero_random_1 == 1:
                preguntas_deporte (numero_random_1,numero_random_2,correctos,incorrectos)
                pass
            elif numero_random_1 == 2:
                preguntas_ciencia(numero_random_1, numero_random_2, correctos, incorrectos)
                pass
            elif numero_random_1 == 3:
                pass
            elif numero_random_1 == 4:
                pass
            elif numero_random_1 == 5:
                pass
            elif numero_random_1 == 6:
                pass