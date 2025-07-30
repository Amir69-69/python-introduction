# exercises/6-bowling/test_bowling.py


from src.bowling import BowlingGame, InvalidFrameError, TooManyRollsError

def test_1_score_all_zeros():
    game = BowlingGame()
    for _ in range(20):
        game.lancer(0)
    assert game.score() == 0

def test_2_score_all_ones():
    game = BowlingGame()
    for _ in range(20):
        game.lancer(1)
    assert game.score() == 20

def test_3_one_spare():
    game = BowlingGame()
    game.lancer(5)
    game.lancer(5)  # spare
    game.lancer(3)
    for _ in range(17):
        game.lancer(0)
    assert game.score() == 16  # 10 + 3

def test_4_one_strike():
    game = BowlingGame()
    game.lancer(10)  # strike
    game.lancer(3)
    game.lancer(4)
    for _ in range(16):
        game.lancer(0)
    assert game.score() == 24  # 10 + 3 + 4 + 3 + 4

def test_5_perfect_game():
    game = BowlingGame()
    for _ in range(12):  # 12 strikes
        game.lancer(10)
    assert game.score() == 300

def test_6_invalid_frame_too_many_quilles():
    game = BowlingGame()
    game.lancer(8)
    game.lancer(5)
    try:
        game.score()  # C’est ici que l’erreur doit se produire
        assert False, "Devrait lever une exception"
    except InvalidFrameError:
        pass
