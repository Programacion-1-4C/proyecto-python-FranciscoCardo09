import random

from Preguntas_Preguntados import Preguntas_Ciencia,Preguntas_Deporte,Preguntas_Geografia,Preguntas_Historia,Preguntas_Arte,preguntas_deporte,Preguntas_Entretenimiento,preguntas_ciencia
from Funciones_Preguntados import menu_1, menu_2, OPCIONES,OPCIONES2


if __name__ == "__main__":
    incorrectos = 0
    correctos = 0
    desicion = menu_1(OPCIONES)
    if desicion == '1':
        while 20 < correctos:
            numero_random_1 = random.randint(1, 6)
            numero_random_2 = random.randint(1, 20)
            if numero_random_1 == 1:
                preguntas_deporte (numero_random_1,numero_random_2,correctos,incorrectos)
            elif numero_random_1 == 1:
                preguntas_deporte(numero_random_1, numero_random_2, correctos, incorrectos)