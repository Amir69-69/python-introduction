class RegularFrame:
    def __init__(self, lancers):
        self.lancers = lancers

    def is_strike(self, index):
        return self.lancers[index] == 10

    def is_spare(self, index):
        return self.lancers[index] + self.lancers[index + 1] == 10

    def score(self):
        score = 0
        index = 0
        l = self.lancers

        for frame in range(10):
            if self.is_strike(index):
                bonus1 = l[index + 1] if index + 1 < len(l) else 0
                bonus2 = l[index + 2] if index + 2 < len(l) else 0
                score += 10 + bonus1 + bonus2
                index += 1
            elif self.is_spare(index):
                bonus = l[index + 2] if index + 2 < len(l) else 0
                score += 10 + bonus
                index += 2
            else:
                score += l[index] + l[index + 1]
                index += 2

        return score
