from Preguntas_Preguntados import Preguntas_Ciencia,Preguntas_Deporte,Preguntas_Geografia,Preguntas_Historia,Preguntas_Arte,Preguntas_Entretenimiento

OPCIONES = ['Modo Normal',
            'De 2 a 4 jugadores',
            'Tematicas']
OPCIONES2 = ['Videojuegos',
             'Marvel',
             'Series']
lista_paises_europa = ['Albania','Alemania','Andorra','Austria','Bélgica','Bielorrusia','Bosnia y Herzegovina','Bulgaria',
                        'Chipre','Ciudad del Vaticano','Croacia','Dinamarca','Eslovaquia','Eslovenia','España','Estonia',
                        'Finlandia','Francia','Grecia','Hungría','Irlanda','Islandia','Italia','Letonia','Liechtenstein','Lituania',
                        'Luxemburgo','Malta','Moldavia','Mónaco','Montenegro','Noruega','Países Bajos','Polonia','Portugal','Reino Unido'
                        'República Checa','República de Macedonia','Rumania','Rusia','San Marino','Serbia','Suecia','Suiza','Ucrania']
lista_paises_asia = ['Afganistan','Arabia Saudita','Armenia','Azerbaiyán','Bangladés','Baréin','Birmania','Brunéi','Bután',
                       'Camboya','Catar','China','Corea del Norte','Corea del Sur','Emiratos Árabes Unidos','Filipinas','Georgia',
                       'India','Indonesia','Irak','Irán','Israel','Japón','Jordania','Kazajistán','Kirguistán','Kuwait','Laos',
                       'Líbano','Maldivas','Malasia','Mongolia','Nepal','Omán','Pakistán','Rusia','Singapur','Siria','Sri Lanka',
                       'Tayikistán','Tailandia','Timor Oriental','Turquía','Turkmenistán','Uzbekistán','Vietnam','Yemen']
lista_paises_america = ['Antigua y Barbuda','Aruba','Bahamas','Barbados','Cuba','Dominica','Grenada','Guadalupe','Haití','Islas Caimán',
                        'Islas Turcas y Caicos','Islas Vírgenes','Jamaica','Martinica','Puerto Rico','República Dominicana',
                        'San Bartolomé','San Cristóbal y Nieves','San Vicente y las Granadinas','Santa Lucía','Trinidad y Tobago',
                        'Belice','Costa Rica','El Salvador','Guatemala','Honduras','Nicaragua','Panamá','Argentina','Bolivia','Brasil','Chile',
                        'Colombia','Ecuador','Guyana','Guyana Francesa','Paraguay','Perú','Suriname','Uruguay','Venezuela','México']
lista_paises_oceania = []

def menu_1 (OPCIONES):
    for num, opciones in enumerate(OPCIONES):
        print(f'{num + 1}. {opciones}')
    decision = input(f'Elija un modo (1-{len(OPCIONES)}): ')
    return decision

def menu_2 (OPCIONES2):
    for num, opciones in enumerate(OPCIONES2):
        print(f'{num + 1}. {opciones}')
    decision_2 = input(f'Elija una tematica (1-{len(OPCIONES2)}): ')
    return decision_2

def preguntas_deporte (numero_random_1,numero_random_2,correctos,incorrectos):
    if numero_random_1 == 1:
        if numero_random_2 == 1:
            print(Preguntas_Deporte[1])
            respuestas = input('1- 4\n'
                               '2- 5\n'
                               '3- 6\n'
                               '4- 9\n>>>')
            if respuestas == '2':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Deporte[2])
            respuestas = input('1- Cavaliers\n'
                               '2- Lakers\n'
                               '3- Miami Heat\n'
                               '4- Todas son correctas\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Deporte[3])
            respuestas = input('1- 3.117\n'
                               '2- 2.143\n'
                               '3- 3.013\n'
                               '4- 3.500\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 4:
            print(Preguntas_Deporte[4])
            respuestas = input('1- Boston Celtics\n'
                               '2- Golden State\n'
                               '3- Lakers\n'
                               '4- Miami Heat\n>>>')
            if respuestas == '2':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 5:
            print(Preguntas_Deporte[5])
            respuestas = input('1- Facu Campazzo\n'
                               '2- Manu Ginobili\n'
                               '3- Luis Scola\n'
                               '4- Leandro Bolmmaro\n>>>')
            if respuestas == '2':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 6:
            print(Preguntas_Deporte[6])
            respuestas = input('1- 4\n'
                               '2- 8\n'
                               '3- 3\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 7:
            print(Preguntas_Deporte[7])
            respuestas = input('1- 2018/19\n'
                               '2- 2019/20\n'
                               '3- 2015/16\n'
                               '4- 2020/21\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 8:
            print(Preguntas_Deporte[8])
            respuestas = input('1- 10\n'
                               '2- 5\n'
                               '3- 7\n'
                               '4- 2\n>>>')
            if respuestas == '3':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 9:
            print(Preguntas_Deporte[9])
            respuestas = input('1- Barcelona\n'
                               '2- Roma\n'
                               '3- Boca\n'
                               '4- Argentinos Juniors\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 10:
            print(Preguntas_Deporte[10])
            respuestas = input('1- 1\n'
                               '2- 4\n'
                               '3- 2\n'
                               '4- 3\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 11:
            print(Preguntas_Deporte[11])
            respuestas = input('1- 18m\n'
                               '2- 20m\n'
                               '3- 12m\n'
                               '4- 15m\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 12:
            print(Preguntas_Deporte[12])
            respuestas = input('1- 2\n'
                               '2- 5\n'
                               '3- 6\n'
                               '4- 9\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 13:
            print(Preguntas_Deporte[13])
            respuestas = input('1- España-Holanda\n'
                               '2- Holanda-Portugal\n'
                               '3- España-Brasil\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 14:
            print(Preguntas_Deporte[14])
            respuestas = input('1- Croacia\n'
                               '2- USA\n'
                               '3- Francia\n'
                               '4- Argentina\n>>>')
            if respuestas == '3':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 15:
            print(Preguntas_Deporte[15])
            respuestas = input('1- Marta Fiedina\n'
                               '2- Yukiko Inui\n'
                               '3- Zopie Andrew Spitz\n'
                               '4- Caeleb Dressel\n>>>')
            if respuestas == '2':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 16:
            print(Preguntas_Deporte[16])
            respuestas = input('1- Rafael Nadal\n'
                               '2- Del Potro\n'
                               '3- Novak Djokovic\n'
                               '4- Roger Federer\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 17:
            print(Preguntas_Deporte[17])
            respuestas = input('1- 9 hs\n'
                               '2- 4 hs\n'
                               '3- 5 hs\n'
                               '4- 11 hs\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 18:
            print(Preguntas_Deporte[18])
            respuestas = input('1- Francia\n'
                               '2- Inglaterra\n'
                               '3- España\n'
                               '4- Italia\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 19:
            print(Preguntas_Deporte[19])
            respuestas = input('1- 6\n'
                               '2- 7\n'
                               '3- 9\n'
                               '4- 12\n>>>')
            if respuestas == '2':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 20:
            print(Preguntas_Deporte[20])
            respuestas = input('1- Lando Norris\n'
                               '2- Max Verstappen\n'
                               '3- Lewis Hamilton\n'
                               '4- Sebastian Vettel\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
    print(f'Respuestas correctas: {correctos}. Respuestas incorrectas: {incorrectos}')
    return correctos, incorrectos

def preguntas_ciencia (numero_random_1,numero_random_2,correctos,incorrectos):
    if numero_random_1 == 2:
        if numero_random_2 == 1:
            print(Preguntas_Ciencia[1])
            respuestas = input('1- 32\n'
                               '2- 31\n'
                               '3- 50\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Ciencia[2])
            respuestas = input('1- El intestino grueso\n'
                               '2- El intestino delgado\n'
                               '3- La piel\n'
                               '4- El riñon\n>>>')
            if respuestas == '3':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Ciencia[3])
            respuestas = input('1- El pancreas\n'
                               '2- El corazon\n'
                               '3- El riñon\n'
                               '4- El oido\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 4:
            print(Preguntas_Ciencia[4])
            respuestas = input('1- H2O\n'
                               '2- O2\n'
                               '3- H2O2\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 5:
            print(Preguntas_Ciencia[5])
            respuestas = input('1- 234142\n'
                               '2- 143123\n'
                               '3- 131516\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 6:
            print(Preguntas_Ciencia[6])
            respuestas = input('1- La Dinamita\n'
                               '2- El Mercurio\n'
                               '3- La Gravedad\n'
                               '4- El Oro\n>>>')
            if respuestas == '1':
                print('Correcta')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 7:
            print(Preguntas_Ciencia[7])
            respuestas = input('1- La Dinamita\n'
                               '2- El Mercurio\n'
                               '3- La Gravedad\n'
                               '4- El Oro\n>>>')
            if respuestas == '3':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 8:
            print(Preguntas_Ciencia[8])
            respuestas = input('1- H2O\n'
                               '2- El N2SO4\n'
                               '3- SO3\n'
                               '4- N2\n>>>')
            if respuestas == '2':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 9:
            print(Preguntas_Ciencia[9])
            respuestas = input('1- Hidrogeno\n'
                               '2- Oxigeno\n'
                               '3- Yodo\n'
                               '4- Hierro\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 10:
            print(Preguntas_Ciencia[10])
            respuestas = input('1- N2S\n'
                               '2- CH4\n'
                               '3- NH3\n'
                               '4- CO2\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 11:
            print(Preguntas_Ciencia[11])
            respuestas = input('1- 384,400 km\n'
                               '2- 320,000 km\n'
                               '3- 385,000 km\n'
                               '4- 384,960 km\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 12:
            print(Preguntas_Ciencia[12])
            respuestas = input('1- 38,400 km\n'
                               '2- 20,000 km\n'
                               '3- 10,742 km\n'
                               '4- 12,742 km\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 13:
            print(Preguntas_Ciencia[13])
            respuestas = input('1- masa x aceleracion\n'
                               '2- velocidad / tiempo\n'
                               '3- masa / tiempo\n'
                               '4- distancia x tiempo\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 14:
            print(Preguntas_Ciencia[14])
            respuestas = input('1- No hay una ley\n'
                               '2- Ley de accion reaccion\n'
                               '3- Ley de Inercia\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 15:
            print(Preguntas_Ciencia[15])
            respuestas = input('1- distancia / aceleracion\n'
                               '2- potencia^2\n'
                               '3- masa x aceleracion\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 16:
            print(Preguntas_Ciencia[16])
            respuestas = input('1- No hay una ley\n'
                               '2- Ley de accion reaccion\n'
                               '3- Ley de Inercia\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 17:
            print(Preguntas_Ciencia[17])
            respuestas = input('1- Sol, CO2, Clorofila, Agua y Sales minerales\n'
                               '2- Sol, CO2, Clorofila\n'
                               '3- Agua\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 18:
            print(Preguntas_Ciencia[18])
            respuestas = input('1- 110\n'
                               '2- 120\n'
                               '3- 145\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 19:
            print(Preguntas_Ciencia[19])
            respuestas = input('1- Bobina de Tesla\n'
                               '2- Motor eléctrico\n'
                               '3- La corriente alterna\n'
                               '4- Todas son correctas\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 20:
            print(Preguntas_Ciencia[20])
            respuestas = input('1- Teoría de la relatividad especial\n'
                               '2- Teoría de campo unificado\n'
                               '3- E=mc2\n'
                               '4- Todas son correctas\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
    print(f'Respuestas correctas: {correctos}. Respuestas incorrectas: {incorrectos}')
    return correctos, incorrectos

def preguntas_geografia (numero_random_1,numero_random_2,correctos,incorrectos):
    if numero_random_1 == 1:
        if numero_random_2 == 1:
            print(Preguntas_Geografia[1])
            respuestas = input('1- 195\n'
                               '2- 197\n'
                               '3- 132\n'
                               '4- 235\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Geografia[2])
            respuestas = input('1- 25\n'
                               '2- 22\n'
                               '3- 23\n'
                               '4- 19\n>>>')
            if respuestas == '3':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Geografia[3])
            respuestas = input('1- Rio Tiber\n'
                               '2- Rio Cuarto\n'
                               '3- Rio Nilo\n'
                               '4- Rio Amazonas\n>>>')
            if respuestas == '4':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 4:
            print(Preguntas_Geografia[4])
            respuestas = input('1- Rusia\n'
                               '2- España\n'
                               '3- Noruega\n'
                               '4- Polonia\n>>>')
            if respuestas == '1':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 5:
            print(Preguntas_Geografia[5])
            respuestas = input('1- 5\n'
                               '2- 3\n'
                               '3- 6\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 6:
            print(Preguntas_Geografia[6])
            respuestas = input('>>>')
            if respuestas in lista_paises_europa:
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
        if numero_random_2 == 7:
            print(Preguntas_Geografia[7])
            respuestas = input('>>>')
            if respuestas in lista_paises_america:
                print('Correcto')
                correctos += 1
            else:
                print('Incorrecto')
                incorrectos += 1
    print(f'Respuestas correctas: {correctos}. Respuestas incorrectas: {incorrectos}')
    return correctos,incorrectos