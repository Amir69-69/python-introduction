from src import score
from src.BowlingGame import BowlingGame

def test_score_0():
    assert score("-- -- -- -- -- -- -- -- -- -- -- -- -- -- --") == 0


def test_only_strike():
    assert score("X X X X X X X X X X X X") == 300

def test_only_spare():
    assert score("3/ 2/ 4/ 6/ 7/ 2/ 4/ 5/ 7/ 9/ 2") == 148

def test_random():
    assert score("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-") == 90
    assert score("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5") == 150
    assert score("45 63 27 9/ X 8/ X 9- 7/ 81 9") == 142

def test_without_strike_and_spare():
    assert score("12 34 45 54 36 27 63 18 09 90") == 82

def test_with_class_score_0():
    game = BowlingGame("-- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
    assert game.score() == 0

def test_with_class_only_strike():
    game = BowlingGame("X X X X X X X X X X X X")
    assert game.score() == 300

def test_with_class_only_spare():
    game = BowlingGame("3/ 2/ 4/ 6/ 7/ 2/ 4/ 5/ 7/ 9/ 2")
    assert game.score() == 148

def test_with_class_random():
    game1 = BowlingGame("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-")
    assert game1.score() == 90

    game2 = BowlingGame("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5")
    assert game2.score() == 150

    game3 = BowlingGame("45 63 27 9/ X 8/ X 9- 7/ 81 9")
    assert game3.score() == 142

def test_with_class_without_strike_and_spare():
    game = BowlingGame("12 34 45 54 36 27 63 18 09 90")
    assert game.score() == 82