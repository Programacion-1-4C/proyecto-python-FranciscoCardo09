from Preguntas_Preguntados import Preguntas_Ciencia,Preguntas_Deporte,Preguntas_Geografia,Preguntas_Historia,Preguntas_Arte,Preguntas_Entretenimiento

OPCIONES = ['Modo Normal',
            'De 2 a 4 jugadores',
            'Tematicas']
OPCIONES2 = ['Videojuegos',
             'Marvel',
             'Series']
Info_jugador_1 = {'Deporte':'No ganado',
                  'Ciencia':'No ganado',
                  'Geografia':'No ganado',
                  'Entretenimiento':'No ganado',
                  'Historia':'No ganado',
                  'Arte':'No ganado',
                  'Correctas':0,
                  'Incorrectas':0}
Info_jugador_2 = {'Deporte':'No ganado',
                  'Ciencia':'No ganado',
                  'Geografia':'No ganado',
                  'Entretenimiento':'No ganado',
                  'Historia':'No ganado',
                  'Arte':'No ganado',
                  'Correctas':0,
                  'Incorrectas':0}
Info_jugador_3 = {'Deporte':'No ganado',
                  'Ciencia':'No ganado',
                  'Geografia':'No ganado',
                  'Entretenimiento':'No ganado',
                  'Historia':'No ganado',
                  'Arte':'No ganado',
                  'Correctas':0,
                  'Incorrectas':0}
Info_jugador_4 = {'Deporte':'No ganado',
                  'Ciencia':'No ganado',
                  'Geografia':'No ganado',
                  'Entretenimiento':'No ganado',
                  'Historia':'No ganado',
                  'Arte':'No ganado',
                  'Correctas':0,
                  'Incorrectas':0}

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
lista_paises_oceania = ['Australia','Nueva Zelanda','Papúa Nueva Guinea','Fiyi','Islas Marshall','Islas Salomón','Kiribati',
                        'Tonga','Samoa','Tuvalu','Vanuatu','Micronesia','Nauru','Palaos']
lista_paises_africa = ['Angola','Argelia','Benín, Porto','Botsuana','Burkina Faso','Burundi','Cabo Verde','Camerún',
                       'Centroafricana','Comores','Costa de Marfil','Chad','Egipto','Eritrea','Etiopía','Gabón','Gambia','Ghana',
                       'Guinea','Guinea-Bissau','Guinea Ecuatorial','Kenia','Lesoto','Liberia','Libia','Madagascar','Malaui','Malí',
                       'Marruecos','Mauricio','Mauritania','Mozambique','Namibia','Níger','Nigeria','Ruanda','República del Congo',
                       'República Democrática del congo','Santo Tomé y Príncipe','Senegal','Seychelles','Sierra Leona','Somalia',
                       'Sudáfrica','Sudán','Sudán del Sur','Suazilandia','Tanzania','Túnez','Togo','Uganda','Yibuti','Zambia',
                       'Zimbabue']
lista_familia_simpsons = ['Homero','Maggie','Lisa','Bart','Marge','Abraham','Mona']

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
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Deporte[2])
            respuestas = input('1- Cavaliers\n'
                               '2- Lakers\n'
                               '3- Miami Heat\n'
                               '4- Todas son correctas\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Deporte[3])
            respuestas = input('1- 3.117\n'
                               '2- 2.143\n'
                               '3- 3.013\n'
                               '4- 3.500\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 4:
            print(Preguntas_Deporte[4])
            respuestas = input('1- Boston Celtics\n'
                               '2- Golden State\n'
                               '3- Lakers\n'
                               '4- Miami Heat\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 5:
            print(Preguntas_Deporte[5])
            respuestas = input('1- Facu Campazzo\n'
                               '2- Manu Ginobili\n'
                               '3- Luis Scola\n'
                               '4- Leandro Bolmmaro\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 6:
            print(Preguntas_Deporte[6])
            respuestas = input('1- 4\n'
                               '2- 8\n'
                               '3- 3\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 7:
            print(Preguntas_Deporte[7])
            respuestas = input('1- 2018/19\n'
                               '2- 2019/20\n'
                               '3- 2015/16\n'
                               '4- 2020/21\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 8:
            print(Preguntas_Deporte[8])
            respuestas = input('1- 10\n'
                               '2- 5\n'
                               '3- 7\n'
                               '4- 2\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 9:
            print(Preguntas_Deporte[9])
            respuestas = input('1- Barcelona\n'
                               '2- Roma\n'
                               '3- Boca\n'
                               '4- Argentinos Juniors\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 10:
            print(Preguntas_Deporte[10])
            respuestas = input('1- 1\n'
                               '2- 4\n'
                               '3- 2\n'
                               '4- 3\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 11:
            print(Preguntas_Deporte[11])
            respuestas = input('1- 18m\n'
                               '2- 20m\n'
                               '3- 12m\n'
                               '4- 15m\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 12:
            print(Preguntas_Deporte[12])
            respuestas = input('1- 2\n'
                               '2- 5\n'
                               '3- 6\n'
                               '4- 9\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 13:
            print(Preguntas_Deporte[13])
            respuestas = input('1- España-Holanda\n'
                               '2- Holanda-Portugal\n'
                               '3- España-Brasil\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 14:
            print(Preguntas_Deporte[14])
            respuestas = input('1- Croacia\n'
                               '2- USA\n'
                               '3- Francia\n'
                               '4- Argentina\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 15:
            print(Preguntas_Deporte[15])
            respuestas = input('1- Marta Fiedina\n'
                               '2- Yukiko Inui\n'
                               '3- Zopie Andrew Spitz\n'
                               '4- Caeleb Dressel\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 16:
            print(Preguntas_Deporte[16])
            respuestas = input('1- Rafael Nadal\n'
                               '2- Del Potro\n'
                               '3- Novak Djokovic\n'
                               '4- Roger Federer\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 17:
            print(Preguntas_Deporte[17])
            respuestas = input('1- 9 hs\n'
                               '2- 4 hs\n'
                               '3- 5 hs\n'
                               '4- 11 hs\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 18:
            print(Preguntas_Deporte[18])
            respuestas = input('1- Francia\n'
                               '2- Inglaterra\n'
                               '3- España\n'
                               '4- Italia\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 19:
            print(Preguntas_Deporte[19])
            respuestas = input('1- 6\n'
                               '2- 7\n'
                               '3- 9\n'
                               '4- 12\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 20:
            print(Preguntas_Deporte[20])
            respuestas = input('1- Lando Norris\n'
                               '2- Max Verstappen\n'
                               '3- Lewis Hamilton\n'
                               '4- Sebastian Vettel\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
    print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
    return correctos, incorrectos,respuestas

def preguntas_ciencia (numero_random_1,numero_random_2,correctos,incorrectos):
    if numero_random_1 == 2:
        if numero_random_2 == 1:
            print(Preguntas_Ciencia[1])
            respuestas = input('1- 32\n'
                               '2- 31\n'
                               '3- 50\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 2:
            print(Preguntas_Ciencia[2])
            respuestas = input('1- El intestino grueso\n'
                               '2- El intestino delgado\n'
                               '3- La piel\n'
                               '4- El riñon\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 3:
            print(Preguntas_Ciencia[3])
            respuestas = input('1- El pancreas\n'
                               '2- El corazon\n'
                               '3- El riñon\n'
                               '4- El oido\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 4:
            print(Preguntas_Ciencia[4])
            respuestas = input('1- H2O\n'
                               '2- O2\n'
                               '3- H2O2\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 5:
            print(Preguntas_Ciencia[5])
            respuestas = input('1- 234142\n'
                               '2- 143123\n'
                               '3- 131516\n'
                               '4- Ninguna de las anteriores\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 6:
            print(Preguntas_Ciencia[6])
            respuestas = input('1- La Dinamita\n'
                               '2- El Mercurio\n'
                               '3- La Gravedad\n'
                               '4- El Oro\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcta')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 7:
            print(Preguntas_Ciencia[7])
            respuestas = input('1- La Dinamita\n'
                               '2- El Mercurio\n'
                               '3- La Gravedad\n'
                               '4- El Oro\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 8:
            print(Preguntas_Ciencia[8])
            respuestas = input('1- H2O\n'
                               '2- El N2SO4\n'
                               '3- SO3\n'
                               '4- N2\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 9:
            print(Preguntas_Ciencia[9])
            respuestas = input('1- Hidrogeno\n'
                               '2- Oxigeno\n'
                               '3- Yodo\n'
                               '4- Hierro\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 10:
            print(Preguntas_Ciencia[10])
            respuestas = input('1- N2S\n'
                               '2- CH4\n'
                               '3- NH3\n'
                               '4- CO2\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 11:
            print(Preguntas_Ciencia[11])
            respuestas = input('1- 384,400 km\n'
                               '2- 320,000 km\n'
                               '3- 385,000 km\n'
                               '4- 384,960 km\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 12:
            print(Preguntas_Ciencia[12])
            respuestas = input('1- 38,400 km\n'
                               '2- 20,000 km\n'
                               '3- 10,742 km\n'
                               '4- 12,742 km\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 13:
            print(Preguntas_Ciencia[13])
            respuestas = input('1- masa x aceleracion\n'
                               '2- velocidad / tiempo\n'
                               '3- masa / tiempo\n'
                               '4- distancia x tiempo\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 14:
            print(Preguntas_Ciencia[14])
            respuestas = input('1- No hay una ley\n'
                               '2- Ley de accion reaccion\n'
                               '3- Ley de Inercia\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '3':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 15:
            print(Preguntas_Ciencia[15])
            respuestas = input('1- distancia / aceleracion\n'
                               '2- potencia^2\n'
                               '3- masa x aceleracion\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 16:
            print(Preguntas_Ciencia[16])
            respuestas = input('1- No hay una ley\n'
                               '2- Ley de accion reaccion\n'
                               '3- Ley de Inercia\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '2':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 17:
            print(Preguntas_Ciencia[17])
            respuestas = input('1- Sol, CO2, Clorofila, Agua y Sales minerales\n'
                               '2- Sol, CO2, Clorofila\n'
                               '3- Agua\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 18:
            print(Preguntas_Ciencia[18])
            respuestas = input('1- 110\n'
                               '2- 120\n'
                               '3- 145\n'
                               '4- Ninguna es correcta\n>>>')
            if respuestas == '1':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 19:
            print(Preguntas_Ciencia[19])
            respuestas = input('1- Bobina de Tesla\n'
                               '2- Motor eléctrico\n'
                               '3- La corriente alterna\n'
                               '4- Todas son correctas\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
        elif numero_random_2 == 20:
            print(Preguntas_Ciencia[20])
            respuestas = input('1- Teoría de la relatividad especial\n'
                               '2- Teoría de campo unificado\n'
                               '3- E=mc2\n'
                               '4- Todas son correctas\n>>>')
            if respuestas == '4':
                respuestas = 'Correcto'
                print('Correcto')
                correctos += 1
            else:
                respuestas = 'Incorrecto'
                print('Incorrecto')
                incorrectos += 1
    print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
    return correctos, incorrectos,respuestas

def preguntas_geografia (numero_random_1,numero_random_2,correctos,incorrectos):
    if numero_random_1 == 3:
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
            if respuestas in lista_paises_europa:
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
            if respuestas == '4':
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
    print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
    return correctos,incorrectos,respuestas

def preguntas_entretenimiento(numero_random_1,numero_random_2,correctos,incorrectos):
    if numero_random_1 == 4:
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
    print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
    return correctos, incorrectos, respuestas

def preguntas_historia(numero_random_1,numero_random_2,correctos,incorrectos):
    if numero_random_1 == 5:
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
    print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
    return correctos, incorrectos, respuestas

def preguntas_arte(numero_random_1,numero_random_2,correctos,incorrectos):
    if numero_random_1 == 6:
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
    print(f'Respuestas correctas: {correctos}/20. Respuestas incorrectas: {incorrectos}/3')
    return correctos, incorrectos, respuestas