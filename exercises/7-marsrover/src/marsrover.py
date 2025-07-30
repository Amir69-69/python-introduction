# exercises/7-marsrover/src/rover.py

DIRECTIONS = ['N', 'E', 'S', 'W']

EMOJIS = {
    'N': '⬆️',
    'E': '➡️',
    'S': '⬇️',
    'W': '⬅️',
    'obstacle': '🌳',
    'vide': '🟩'
}

class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def tourner_droite(self):
        idx = (DIRECTIONS.index(self.direction) + 1) % 4
        self.direction = DIRECTIONS[idx]

    def tourner_gauche(self):
        idx = (DIRECTIONS.index(self.direction) - 1) % 4
        self.direction = DIRECTIONS[idx]

    def get_next_position(self):
        dx, dy = {
            'N': (0, -1),
            'E': (1, 0),
            'S': (0, 1),
            'W': (-1, 0),
        }[self.direction]
        return self.x + dx, self.y + dy

    def avancer(self, map_obj):
        new_x, new_y = self.get_next_position()
        if map_obj.is_valid(new_x, new_y):
            self.x, self.y = new_x, new_y

class Map:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, x, y):
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            return self.grid[y][x] != EMOJIS['obstacle']
        return False

    def afficher(self, rover):
        for y, ligne in enumerate(self.grid):
            ligne_str = ''
            for x, case in enumerate(ligne):
                if x == rover.x and y == rover.y:
                    ligne_str += EMOJIS[rover.direction]
                else:
                    ligne_str += case
            print(ligne_str)
        print()
