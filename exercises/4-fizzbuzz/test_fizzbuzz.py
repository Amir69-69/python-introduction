from src.fizzbuzz import fizzbuzz

def test_classic_number():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"

def test_fizz_only():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"

def test_buzz_only():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_contains_three():
    assert fizzbuzz(13) == "Fizz"
    assert fizzbuzz(31) == "Fizz"
    assert fizzbuzz(33) == "Fizz"  # contient 3 ET % 3

def test_contains_five():
    assert fizzbuzz(52) == "Buzz"
    assert fizzbuzz(59) == "Buzz"
    assert fizzbuzz(55) == "Buzz"

def test_contains_both():
    assert fizzbuzz(35) == "FizzBuzz"
    assert fizzbuzz(53) == "FizzBuzz"
    assert fizzbuzz(15) == "FizzBuzz"  # %3 et %5

def test_neither():
    assert fizzbuzz(7) == "7"
    assert fizzbuzz(8) == "8"
