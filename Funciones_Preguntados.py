from Preguntas_Preguntados import Preguntas_Geografia, Preguntas_Historia, \
    Preguntas_Arte, Preguntas_Entretenimiento, preguntas_cat
import random

OPCIONES = ['Modo Normal',
            'De 2 a 4 jugadores',
            'Tematicas']
OPCIONES2 = ['Videojuegos',
             'Marvel',
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
    decision_2 = input(f'Elija una tematica (1-{len(OPCIONES2)}): ')
    return decision_2


def mostrar_info_jugador(jugador):
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


def preguntas_geografia(numero_random_1, numero_random_2, correctos, incorrectos):
    global respuestas
    if numero_random_1 != 7:
        if numero_random_2 == 1:
            print(Preguntas_Geografia[1])
            respuestas = input('1- 195\n'
                               '2- 197\n'
                               '3- 132\n'
                               '4- 235\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Geografia[2])
            respuestas = input('1- 25\n'
                               '2- 22\n'
                               '3- 23\n'
                               '4- 19\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Geografia[3])
            respuestas = input('1- Rio Tiber\n'
                               '2- Rio Cuarto\n'
                               '3- Rio Nilo\n'
                               '4- Rio Amazonas\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 4:
            print(Preguntas_Geografia[4])
            respuestas = input('1- Rusia\n'
                               '2- España\n'
                               '3- Noruega\n'
                               '4- Polonia\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 5:
            print(Preguntas_Geografia[5])
            respuestas = input('1- 5\n'
                               '2- 3\n'
                               '3- 6\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                respuestas = 'Incorrecto'
                incorrectos += 1
        if numero_random_2 == 6:
            print(Preguntas_Geografia[6])
            respuestas = input('>>>')
            if respuestas in lista_paises_asia:
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 7:
            print(Preguntas_Geografia[7])
            respuestas = input('>>>')
            if respuestas in lista_paises_america:
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 8:
            print(Preguntas_Geografia[8])
            respuestas = input('>>>')
            if respuestas in lista_paises_oceania:
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 9:
            print(Preguntas_Geografia[9])
            respuestas = input('>>>')
            if respuestas in lista_paises_europa:
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 10:
            print(Preguntas_Geografia[10])
            respuestas = input('>>>')
            if respuestas in lista_paises_africa:
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 11:
            print(Preguntas_Geografia[11])
            respuestas = input('1- Atlantico\n'
                               '2- Pacifico\n'
                               '3- Indico\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 12:
            print(Preguntas_Geografia[12])
            respuestas = input('1- Londres\n'
                               '2- Paris\n'
                               '3- Buenos Aires\n'
                               '4- Moscú\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 13:
            print(Preguntas_Geografia[13])
            respuestas = input('1- New York\n'
                               '2- Washington DC\n'
                               '3- California\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 14:
            print(Preguntas_Geografia[14])
            respuestas = input('1- Rio Cuarto\n'
                               '2- Venecia\n'
                               '3- Roma\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 15:
            print(Preguntas_Geografia[15])
            respuestas = input('1- Asia Y Oceania\n'
                               '2- Europa\n'
                               '3- Asia Y Europa\n'
                               '4- Africa\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 16:
            print(Preguntas_Geografia[16])
            respuestas = input('1- America\n'
                               '2- Oceania\n'
                               '3- Africa\n'
                               '4- Asia\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 17:
            print(Preguntas_Geografia[17])
            respuestas = input('1- Brasil\n'
                               '2- Egipto\n'
                               '3- Mexico\n'
                               '4- Chile\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                incorrectos += 1
                print('Incorrecto')
        if numero_random_2 == 18:
            print(Preguntas_Geografia[18])
            respuestas = input('1- Peru\n'
                               '2- Mexico\n'
                               '3- Canadá\n'
                               '4- Estados Unidos\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 19:
            print(Preguntas_Geografia[19])
            respuestas = input('1- Peru\n'
                               '2- Italia\n'
                               '3- Canadá\n'
                               '4- Estados Unidos\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 20:
            print(Preguntas_Geografia[20])
            respuestas = input('1- Andorra\n'
                               '2- Luxemburgo\n'
                               '3- Ciudad del Vaticano\n'
                               '4- Chipre\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                incorrectos += 1
                print('Incorrecto')
    return correctos, incorrectos, respuestas


def preguntas_entretenimiento(numero_random_1, numero_random_2, correctos, incorrectos):
    global respuestas
    if numero_random_1 != 7:
        if numero_random_2 == 1:
            print(Preguntas_Entretenimiento[1])
            respuestas = input('>>>')
            if respuestas in lista_familia_simpsons:
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Entretenimiento[2])
            respuestas = input('1- Guiding Light\n'
                               '2- Doctor Who\n'
                               '3- One Piece\n'
                               '4- Friends\n>>>')
            if respuestas == '1':
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Entretenimiento[3])
            respuestas = input('1- Atlanta\n'
                               '2- Titanic\n'
                               '3- Evolution of a Filipino Family\n'
                               '4- Out 1\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 4:
            print(Preguntas_Entretenimiento[4])
            respuestas = input('1- Volver al Futuro\n'
                               '2- Star Wars III\n'
                               '3- Titanic\n'
                               '4- El Señor de los Anillos: el retorno del Rey\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 5:
            print(Preguntas_Entretenimiento[5])
            respuestas = input('1- Taxi Driver\n'
                               '2- Forrest Gump\n'
                               '3- El Irlandes\n'
                               '4- Casino\n>>>')
            if respuestas == '2':
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 6:
            print(Preguntas_Entretenimiento[6])
            respuestas = input('1- Naufrago\n'
                               '2- Forrest Gump\n'
                               '3- Elvis Presley\n'
                               '4- Todas son correctas\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 7:
            print(Preguntas_Entretenimiento[7])
            respuestas = input('1- my time has come\n'
                               '2- life had just begun\n'
                               '3- pulled my trigger\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 8:
            print(Preguntas_Entretenimiento[8])
            respuestas = input('1- 1\n'
                               '2- 2\n'
                               '3- 3\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 9:
            print(Preguntas_Entretenimiento[9])
            respuestas = input('1- Granizo\n'
                               '2- Mi obra maestra\n'
                               '3- El robo del siglo\n'
                               '4- Todas correcta\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                respuestas = 'Incorrecto'
                incorrectos += 1
        if numero_random_2 == 10:
            print(Preguntas_Entretenimiento[10])
            respuestas = input('1- 8\n'
                               '2- 7\n'
                               '3- 9\n'
                               '4- 10\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 11:
            print(Preguntas_Entretenimiento[11])
            respuestas = input('1- 9\n'
                               '2- 11\n'
                               '3- 10\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                respuestas = 'Incorrecto'
                incorrectos += 1
        if numero_random_2 == 12:
            print(Preguntas_Entretenimiento[12])
            respuestas = input('1- La Venganza de los Sith\n'
                               '2- El retorno del Jedi\n'
                               '3- Una nueva esperanza\n'
                               '4- El ultimo Jedi\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 13:
            print(Preguntas_Entretenimiento[13])
            respuestas = input('1- 2014\n'
                               '2- 2016\n'
                               '3- 2012\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 14:
            print(Preguntas_Entretenimiento[14])
            respuestas = input('1- Tom Hardy\n'
                               '2- Paul Anderson\n'
                               '3- Cillian Murphy\n'
                               '4- Finn Cole\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 15:
            print(Preguntas_Entretenimiento[15])
            respuestas = input('1- Arnold Schwarzenegger\n'
                               '2- Chris Pratt\n'
                               '3- Chris Evans\n'
                               '4- Chris Hemswort\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 16:
            print(Preguntas_Entretenimiento[16])
            respuestas = input('1- Cristopher Nolan\n'
                               '2- Vince Gilligan\n'
                               '3- Martin Scorsese\n'
                               '4- Quentin Tarantino\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 17:
            print(Preguntas_Entretenimiento[17])
            respuestas = input('1- 2\n'
                               '2- 4\n'
                               '3- 6\n'
                               '4- 8\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 18:
            print(Preguntas_Entretenimiento[18])
            respuestas = input('1- 1999\n'
                               '2- 1977\n'
                               '3- 1985\n'
                               '4- 1995\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 19:
            print(Preguntas_Entretenimiento[19])
            respuestas = input('1- I never wanna hear you say\n'
                               '2- Tell me why\n'
                               '3- Aint nothin but a mistake\n'
                               '4- Am I your fire?\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 20:
            print(Preguntas_Entretenimiento[20])
            respuestas = input('1- Tom Hanks\n'
                               '2- Robert Dawney Jr.\n'
                               '3- Robert De Niro\n'
                               '4- Harrison Ford\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                incorrectos += 1
                respuestas = 'Incorrecto'
                print('Incorrecto')
    return correctos, incorrectos, respuestas


def preguntas_historia(numero_random_1, numero_random_2, correctos, incorrectos):
    global respuestas
    if numero_random_1 != 7:
        if numero_random_2 == 1:
            print(Preguntas_Historia[1])
            respuestas = input('1- 1912\n'
                               '2- 1913\n'
                               '3- 1914\n'
                               '4- 1915\n>>>')
            if respuestas == '3':
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Historia[2])
            respuestas = input('1- Cristobal Colon\n'
                               '2- Americano Vespuccio\n'
                               '3- Ezio Auditore\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '1':
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Historia[3])
            respuestas = input('1- Siglo XIII\n'
                               '2- Siglo XVIII\n'
                               '3- Siglo XX\n'
                               '4- Siglo XVI\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 4:
            print(Preguntas_Historia[4])
            respuestas = input('1- Siglo XIII\n'
                               '2- Siglo XVIII\n'
                               '3- Siglo XX\n'
                               '4- Siglo XVI\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 5:
            print(Preguntas_Historia[5])
            respuestas = input('1- 1760\n'
                               '2- 1775\n'
                               '3- 1865\n'
                               '4- 1765\n>>>')
            if respuestas == '4':
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 6:
            print(Preguntas_Historia[6])
            respuestas = input('1- 1995\n'
                               '2- 1991\n'
                               '3- 1980\n'
                               '4- 1989\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 7:
            print(Preguntas_Historia[7])
            respuestas = input('1- 1597\n'
                               '2- 1492\n'
                               '3- 1355\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 8:
            print(Preguntas_Historia[8])
            respuestas = input('1- 4 años\n'
                               '2- 5 años\n'
                               '3- 10 años\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 9:
            print(Preguntas_Historia[9])
            respuestas = input('1- 1797\n'
                               '2- 1853\n'
                               '3- 1815\n'
                               '4- 1880\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                respuestas = 'Incorrecto'
                incorrectos += 1
        if numero_random_2 == 10:
            print(Preguntas_Historia[10])
            respuestas = input('1- 1776\n'
                               '2- 1820\n'
                               '3- 1770\n'
                               '4- 1786\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 11:
            print(Preguntas_Historia[11])
            respuestas = input('1- 1815\n'
                               '2- 1816\n'
                               '3- 1836\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                respuestas = 'Incorrecto'
                incorrectos += 1
        if numero_random_2 == 12:
            print(Preguntas_Historia[12])
            respuestas = input('1- 3.500.000 a.C.\n'
                               '2- 2.000.000 a.C.\n'
                               '3- 2.500.000 a.C.\n'
                               '4- 3.000.000 a.C.\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 13:
            print(Preguntas_Historia[13])
            respuestas = input('1- Un alien\n'
                               '2- Un volcán\n'
                               '3- Un meteorito\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 14:
            print(Preguntas_Historia[14])
            respuestas = input('1- Peste Bubonica\n'
                               '2- Covis-19\n'
                               '3- Peste Negra\n'
                               '4- Peste de Galeno\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 15:
            print(Preguntas_Historia[15])
            respuestas = input('1- Se suicido\n'
                               '2- Perdio la guerra\n'
                               '3- Enfermedad\n'
                               '4- Vejez\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 16:
            print(Preguntas_Historia[16])
            respuestas = input('1- Cocinero Frances\n'
                               '2- Cónsul y emperador de Francia.\n'
                               '3- Presidente de los EEUU\n'
                               '4- Libertador de America\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 17:
            print(Preguntas_Historia[17])
            respuestas = input('1- Siglos XIV y XVI.\n'
                               '2- Siglos XIV y XV.\n'
                               '3- Siglos XV y XVI.\n'
                               '4- Siglos XIV y XXI.\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 18:
            print(Preguntas_Historia[18])
            respuestas = input('1- Avellaneda\n'
                               '2- Mitre\n'
                               '3- Roca\n'
                               '4- Perón\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 19:
            print(Preguntas_Historia[19])
            respuestas = input('1- La caida del muro de Berlin\n'
                               '2- La Llegada a America\n'
                               '3- La Independencia de Argentina\n'
                               '4- La independencia de USA\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 20:
            print(Preguntas_Historia[20])
            respuestas = input('1- San Martín\n'
                               '2- Perón\n'
                               '3- Mitre\n'
                               '4- Belgrano\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                incorrectos += 1
                respuestas = 'Incorrecto'
                print('Incorrecto')
    return correctos, incorrectos, respuestas


def preguntas_arte(numero_random_1, numero_random_2, correctos, incorrectos):
    global respuestas
    if numero_random_1 != 7:
        if numero_random_2 == 1:
            print(Preguntas_Arte[1])
            respuestas = input('1- Piedra del Sol\n'
                               '2- Monolito de Tlaltecuhtli\n'
                               '3- Frida y Dirgo Rivera\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Arte[2])
            respuestas = input('1- 205 obras de arte\n'
                               '2- 225 obras de arte\n'
                               '3- 250 obras de arte\n'
                               '4- 195 obras de arte\n>>>')
            if respuestas == '1':
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Arte[3])
            respuestas = input('1- Donatello\n'
                               '2- Miguel Angel\n'
                               '3- Da Vinci\n'
                               '4- Theodore Gericault\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 4:
            print(Preguntas_Arte[4])
            respuestas = input('1- Un escultor japonés\n'
                               '2- Un pintor y grabador japonés\n'
                               '3- Inventor de la pintura al oleo\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 5:
            print(Preguntas_Arte[5])
            respuestas = input('1- Romeo y Julieta\n'
                               '2- Hamlet\n'
                               '3- Machbet\n'
                               '4- Todas son correctas\n>>>')
            if respuestas == '4':
                print('Correcto')
                respuestas = 'Correcto'
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 6:
            print(Preguntas_Arte[6])
            respuestas = input('1- Saint-Rémy-de-Provence\n'
                               '2- Londres\n'
                               '3- Paris\n'
                               '4- Clermont-Ferrand\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 7:
            print(Preguntas_Arte[7])
            respuestas = input('1- Salvador Dalí\n'
                               '2- Anthony Abdel Karim\n'
                               '3- Takashi Murakami\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 8:
            print(Preguntas_Arte[8])
            respuestas = input('1- Jorge Luis Borges\n'
                               '2- Julio Verne\n'
                               '3- José Hernández\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 9:
            print(Preguntas_Arte[9])
            respuestas = input('1- Ojo\n'
                               '2- Brazo\n'
                               '3- Oreja\n'
                               '4- Ninguna\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                respuestas = 'Incorrecto'
                incorrectos += 1
        if numero_random_2 == 10:
            print(Preguntas_Arte[10])
            respuestas = input('1- Amarillo\n'
                               '2- Rojo\n'
                               '3- Violeta\n'
                               '4- Azul\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 11:
            print(Preguntas_Arte[11])
            respuestas = input('1- Miguel Angel\n'
                               '2- Leonardo da Vinci\n'
                               '3- Donatello\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                respuestas = 'Incorrecto'
                incorrectos += 1
        if numero_random_2 == 12:
            print(Preguntas_Arte[12])
            respuestas = input('1- Rojo\n'
                               '2- Naranja\n'
                               '3- Violeta\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 13:
            print(Preguntas_Arte[13])
            respuestas = input('1- DO,RE,MI,LA,SI\n'
                               '2- DO,MI,FA,SOL,LA,SI\n'
                               '3- DO,RE,MI,FA,SOL,LA,SI\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 14:
            print(Preguntas_Arte[14])
            respuestas = input('1- 1 sinfonía\n'
                               '2- 5 sinfonías\n'
                               '3- 7 sinfonías\n'
                               '4- 9 sinfonías\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 15:
            print(Preguntas_Arte[15])
            respuestas = input('1- Beethoven\n'
                               '2- Mozart\n'
                               '3- Debussy\n'
                               '4- Luis César Amadori.\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 16:
            print(Preguntas_Arte[16])
            respuestas = input('1- Elvis Presley\n'
                               '2- B. B. King\n'
                               '3- Michael Jackson\n'
                               '4- Eric Clapton\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 17:
            print(Preguntas_Arte[17])
            respuestas = input('1- Michael Jackson\n'
                               '2- Queen\n'
                               '3- Elvis Presley\n'
                               '4- Madonna\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 18:
            print(Preguntas_Arte[18])
            respuestas = input('1- Azul,Amarillo,Violeta\n'
                               '2- Azul,Verde,Rojo\n'
                               '3- Rojo,Amarillo,Azul\n'
                               '4- Roj,Violeta\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 19:
            print(Preguntas_Arte[19])
            respuestas = input('1- Primario\n'
                               '2- Secundario\n'
                               '3- Terciario\n'
                               '4- No es un color\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 20:
            print(Preguntas_Arte[20])
            respuestas = input('1- Leonardo Da Vinci\n'
                               '2- Rafael Sanzio\n'
                               '3- Van Gohg\n'
                               '4- Filippo Brunelleschi\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                incorrectos += 1
                respuestas = 'Incorrecto'
                print('Incorrecto')
    return correctos, incorrectos, respuestas
