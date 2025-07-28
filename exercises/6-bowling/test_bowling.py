from src.bowling import compute_score

def test_perfect_game():
    assert compute_score("X X X X X X X X X X X X") == 300

def test_all_nines():
    assert compute_score("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-") == 90

def test_all_spares_with_5():
    assert compute_score("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5") == 150




