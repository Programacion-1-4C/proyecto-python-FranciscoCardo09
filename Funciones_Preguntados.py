from Preguntas_Preguntados import preguntas_cat, preguntas_tematica_1
import random

OPCIONES = ['Modo Normal',
            'De 2 a 4 jugadores',
            'Tematicas']
OPCIONES2 = ['Videojuegos',
             'Series']

CATEGORIAS_TEMATICAS = ['Videojuegos',
                        'Series']

CATEGORIAS = [
    'Deporte',
    'Ciencia',
    'Geografia',
    'Entretenimiento',
    'Historia',
    'Arte'
              ]


def menu_1(OPCIONES):
    for num, opciones in enumerate(OPCIONES):
        print(f'{num + 1}. {opciones}')
    decision = input(f'Elija un modo (1-{len(OPCIONES)}): ')
    return decision


def menu_2(OPCIONES2):
    for num, opciones in enumerate(OPCIONES2):
        print(f'{num + 1}. {opciones}')
    decision_2 = int(input(f'Elija una tematica (1-{len(OPCIONES2)}): '))
    decision_2 -= 1
    return decision_2


def mostrar_info_jugador(jugador, num_jugador):
    print(f"datos del jugador {num_jugador}")
    for categoria, valor in jugador.items():
        print(f"{categoria}: {'Ganado' if valor else 'No ganado'}")


def preguntas(categoria):
    preguntas_categoria = preguntas_cat[categoria]
    if len(preguntas_categoria) == 0:
        return True
    numero_random_2 = random.randint(0, len(preguntas_categoria)-1)
    pregunta = preguntas_categoria[numero_random_2]
    print(pregunta["nombre"])
    texto_opciones = ""
    for i, opcion in enumerate(pregunta["opciones"]):
        texto_opciones += f"{i+1}- {opcion}\n"
    respuesta = int(input(texto_opciones + "\n>>>")) == pregunta["respuesta"]
    print("Correcto" if respuesta else "Incorrecto")
    return respuesta


def preguntas_tematicas(categoria):
    preguntas_tematica = preguntas_tematica_1[categoria]
    if len(preguntas_tematica) == 0:
        return True
    numero_random_2 = random.randint(0, len(preguntas_tematica) - 1)
    pregunta = preguntas_tematica[numero_random_2]
    print(pregunta["nombre"])
    texto_opciones = ""
    for i, opcion in enumerate(pregunta["opciones"]):
        texto_opciones += f"{i + 1}- {opcion}\n"
    respuesta = int(input(texto_opciones + "\n>>>")) == pregunta["respuesta"]
    print("Correcto" if respuesta else "Incorrecto")
    return respuesta


def categorias_faltan(info_jugador):
    lista = []
    for cat, valor in info_jugador.items():
        if not valor:
            lista.append(cat)
    return lista


def elegir_categoria(correctos, info_jugador):
    if correctos == 3:
        print('Elegí la categoria')
        lista_categorias = categorias_faltan(info_jugador)
        print(lista_categorias)
        eleccion = input('>>>').capitalize()
        if eleccion in lista_categorias:
            respuesta = preguntas(eleccion)
            if respuesta:
                info_jugador[eleccion] = True
        return info_jugador
    return False
