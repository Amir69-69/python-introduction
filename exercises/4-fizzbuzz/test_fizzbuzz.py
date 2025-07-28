from src.fizzbuzz import fizzbuzz, compute

def test_fizzbuzz_example():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(7) == "7"

def test_compute_output_length(capsys):
    compute()
    out = capsys.readouterr().out.strip().split("\n")
    assert len(out) == 100
