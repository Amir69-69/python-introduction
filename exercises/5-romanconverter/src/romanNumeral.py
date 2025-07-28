def to_roman(n: int) -> str:
    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""
    for value, symbol in roman_map:
        while n >= value:
            result += symbol
            n -= value
    return result


def from_roman(s: str) -> int:
    roman_map = {
        "I": 1,    "V": 5,    "X": 10,
        "L": 50,   "C": 100,  "D": 500,
        "M": 1000
    }
    result = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value
    return result

def compute() -> None:
    """
    Affiche la conversion des nombres de 1 à 100 en chiffres romains,
    sous la forme : 1 => I, 2 => II, etc.
    """
    for i in range(1, 101):
        print(f"{i} => {to_roman(i)}")

if __name__ == "__main__":
    compute()
