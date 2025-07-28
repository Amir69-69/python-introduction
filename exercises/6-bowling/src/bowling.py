def compute_score(game: str) -> int:
    """
    Calcule le score total d'une partie de bowling.
    :param game: Une chaîne représentant les lancers (ex : "X X X X X X X X X X X X")
    :return: Score total
    """
    rolls = []
    i = 0
    while i < len(game):
        if game[i] == 'X':
            rolls.append(10)
            i += 1
        elif game[i] == '/':
            rolls.append(10 - rolls[-1])
            i += 1
        elif game[i] == '-':
            rolls.append(0)
            i += 1
        elif game[i] == ' ':
            i += 1
        else:
            rolls.append(int(game[i]))
            i += 1

    score = 0
    roll_index = 0
    for frame in range(10):
        if rolls[roll_index] == 10:  # strike
            score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
            roll_index += 1
        elif sum(rolls[roll_index:roll_index + 2]) == 10:  # spare
            score += 10 + rolls[roll_index + 2]
            roll_index += 2
        else:
            score += sum(rolls[roll_index:roll_index + 2])
            roll_index += 2
    return score


