# Starter Code for Testing and Debugging Assignment

# Task 1: Implement validation and test functions

def is_prime(number):
    """Return True if number is prime, otherwise False."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    assert isinstance(numbers, list), "Input must be a list of numbers."
    assert len(numbers) > 0, "The list must contain at least one number."
    return sum(numbers) / len(numbers)


def validate_password(password):
    """Return True if the password meets the rules, otherwise False."""
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if password.islower() or password.isupper():
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


# Task 2: Fix the broken divide_numbers function

def divide_numbers(a, b):
    """Divide a by b and return the result."""
    assert b != 0, "Division by zero is not allowed."
    return a / b


# Task 1 Example Tests

def run_tests():
    assert is_prime(2) is True
    assert is_prime(9) is False
    assert is_prime(17) is True

    assert calculate_average([10, 20, 30]) == 20
    try:
        calculate_average([])
    except AssertionError:
        pass
    else:
        raise AssertionError("calculate_average should assert on empty list")

    assert validate_password("Strong123") is True
    assert validate_password("weak") is False
    assert validate_password("ALLUPPER123") is False
    assert validate_password("alllower123") is False

    assert divide_numbers(10, 2) == 5
    try:
        divide_numbers(5, 0)
    except AssertionError:
        pass
    else:
        raise AssertionError("divide_numbers should assert on zero divisor")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
