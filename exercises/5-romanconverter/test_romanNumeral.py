from src.romanNumeral import to_roman, from_roman

# --- Tests to_roman ---

def test_1():
    assert to_roman(1) == "I"

def test_4():
    assert to_roman(4) == "IV"

def test_9():
    assert to_roman(9) == "IX"

def test_58():
    assert to_roman(58) == "LVIII"  # 50 + 5 + 3

def test_1994():
    assert to_roman(1994) == "MCMXCIV"  # 1000 + (1000-100) + (100-10) + (5-1)

# --- Tests from_roman ---

def test_from_I():
    assert from_roman("I") == 1

def test_from_IV():
    assert from_roman("IV") == 4

def test_from_LVIII():
    assert from_roman("LVIII") == 58

def test_from_MCMXCIV():
    assert from_roman("MCMXCIV") == 1994

def test_round_trip():
    for i in range(1, 4000):
        assert from_roman(to_roman(i)) == i  # aller-retour


