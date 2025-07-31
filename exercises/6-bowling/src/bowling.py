def score(sequence):
    lancers = []
    i = 0
    while i < len(sequence):
        char = sequence[i]
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

    score = 0
    index = 0


    for frame in range(10):
        if lancers[index] == 10:
            bonus1 = lancers[index + 1] if index + 1 < len(lancers) else 0
            bonus2 = lancers[index + 2] if index + 2 < len(lancers) else 0
            score += 10 + bonus1 + bonus2
            index += 1
        elif lancers[index] + lancers[index + 1] == 10:
            bonus = lancers[index + 2] if index + 2 < len(lancers) else 0
            score += 10 + bonus
            index += 2
        else:
            score += lancers[index] + lancers[index + 1]
            index += 2

    return score