# exercises/6-bowling/src/bowling.py

class InvalidFrameError(Exception):
    pass

class TooManyRollsError(Exception):
    pass

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def lancer(self, quilles):
        if quilles < 0 or quilles > 10:
            raise ValueError("Le nombre de quilles doit être entre 0 et 10")

        self.rolls.append(quilles)

    def score(self):
        total = 0
        i = 0
        for frame in range(10):
            if self._is_strike(i):
                if i + 2 >= len(self.rolls):
                    raise TooManyRollsError("Pas assez de lancers pour calculer le bonus du strike")
                total += 10 + self.rolls[i + 1] + self.rolls[i + 2]
                i += 1
            elif self._is_spare(i):
                if i + 2 >= len(self.rolls):
                    raise TooManyRollsError("Pas assez de lancers pour calculer le bonus du spare")
                total += 10 + self.rolls[i + 2]
                i += 2
            else:
                if i + 1 >= len(self.rolls):
                    raise TooManyRollsError("Pas assez de lancers pour un frame normal")
                frame_score = self.rolls[i] + self.rolls[i + 1]
                if frame_score > 10:
                    raise InvalidFrameError("Un frame ne peut pas dépasser 10 quilles")
                total += frame_score
                i += 2
        return total

    def _is_strike(self, i):
        return i < len(self.rolls) and self.rolls[i] == 10

    def _is_spare(self, i):
        return (
            i + 1 < len(self.rolls) and
            self.rolls[i] + self.rolls[i + 1] == 10
        )
