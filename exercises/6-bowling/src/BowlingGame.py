from src.RegularFrame import RegularFrame


class BowlingGame:
    def __init__(self, sequence):
        self.sequence = sequence
        self.lancers = self.parse_sequence()

    def parse_sequence(self):
        lancers = []
        i = 0
        while i < len(self.sequence):
            char = self.sequence[i]
            if char == 'X':
                lancers.append(10)
                i += 1
            elif char == '/':
                lancers.append(10 - lancers[-1])
                i += 1
            elif char == '-':
                lancers.append(0)
                i += 1
            elif char == ' ':
                i += 1
            else:
                lancers.append(int(char))
                i += 1
        return lancers

    def score(self):
        calcul = RegularFrame(self.lancers)
        return calcul.score()
