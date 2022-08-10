OPCIONES = ['Modo Normal',
            'De 2 a 4 jugadores',
            'Tematicas']
OPCIONES2 = ['Videojuegos',
             'Marvel',
             'Series']

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