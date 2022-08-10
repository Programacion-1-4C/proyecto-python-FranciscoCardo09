from Preguntas_Preguntados import Preguntas_Ciencia,Preguntas_Deporte,Preguntas_Geografia,Preguntas_Historia,Preguntas_Arte,preguntas,Preguntas_Entretenimiento
from Funciones_Preguntados import menu_1, menu_2, OPCIONES,OPCIONES2
import random


if __name__ == "__main__":
    incorrectos = 0
    correctos = 0
    numero_random_1 = random.randint(1, 7)
    numero_random_2 = random.randint(1, 20)

    desicion = menu_1(OPCIONES)
    if desicion == '1':
        while 20 < correctos:
            preguntas(numero_random_1, numero_random_2, correctos, incorrectos)