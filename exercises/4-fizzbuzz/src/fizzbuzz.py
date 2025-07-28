def fizzbuzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

def fizzbuzz(number: int) -> str:
    is_fizz = number % 3 == 0 or '3' in str(number)
    is_buzz = number % 5 == 0 or '5' in str(number)

    if is_fizz and is_buzz:
        return "FizzBuzz"
    elif is_fizz:
        return "Fizz"
    elif is_buzz:
        return "Buzz"
    else:
        return str(number)
