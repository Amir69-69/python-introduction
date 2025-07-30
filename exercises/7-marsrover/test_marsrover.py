from src import Rover, Map, EMOJIS


def test_1_affichage_initial():
    carte = [[EMOJIS['vide']] * 5 for _ in range(5)]
    map_obj = Map(carte)
    rover = Rover(2, 2, 'N')
    map_obj.afficher(rover)


def test_2_avancer_sans_obstacle():
    carte = [[EMOJIS['vide']] * 5 for _ in range(5)]
    map_obj = Map(carte)
    rover = Rover(2, 2, 'N')

    rover.avancer(map_obj)
    map_obj.afficher(rover)
    assert (rover.x, rover.y) == (2, 1)


def test_3_avancer_vers_obstacle():
    carte = [[EMOJIS['vide']] * 5 for _ in range(5)]
    carte[1][2] = EMOJIS['obstacle']

    map_obj = Map(carte)
    rover = Rover(2, 2, 'N')

    rover.avancer(map_obj)
    map_obj.afficher(rover)
    assert (rover.x, rover.y) == (2, 2)


def test_4_rotation():
    rover = Rover(0, 0, 'N')
    rover.tourner_droite()
    assert rover.direction == 'E'
    rover.tourner_droite()
    assert rover.direction == 'S'
    rover.tourner_gauche()
    assert rover.direction == 'E'


def test_5_sequence_complete():
    carte = [[EMOJIS['vide']] * 5 for _ in range(5)]
    carte[2][3] = EMOJIS['obstacle']
    map_obj = Map(carte)
    rover = Rover(2, 2, 'E')

    commandes = ['⬆️', '⬅️', '⬆️', '➡️', '⬆️']
    for cmd in commandes:
        if cmd == '⬆️':
            rover.avancer(map_obj)
        elif cmd == '➡️':
            rover.tourner_droite()
        elif cmd == '⬅️':
            rover.tourner_gauche()
        map_obj.afficher(rover)


def test_6_avancer_en_bordure():
    carte = [[EMOJIS['vide']] * 5 for _ in range(5)]
    map_obj = Map(carte)
    rover = Rover(0, 0, 'N')
    rover.avancer(map_obj)
    assert (rover.x, rover.y) == (0, 0)
