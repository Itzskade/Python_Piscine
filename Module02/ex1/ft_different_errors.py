#!/usr/bin/env python3

def garden_operations() -> dict:
    """Return dictionary of functions that raise common errors."""
    def garden_value_error(value):
        int(value)

    def garden_zero_division(a, b):
        a / b

    def garden_file_error(filename):
        open(filename)

    def garden_key_error(dictionary, key):
        dictionary[key]

    operations = {
        "value_error": garden_value_error,
        "zero_division": garden_zero_division,
        "file_error": garden_file_error,
        "key_error": garden_key_error
    }
    return operations


def test_error_types(value: int, a: int, b: int, filename: str,
                     dictionary: dict, key: str) -> None:
    """Test different Python error types and handle them."""
    operations = garden_operations()

    print("=== Garden Error Types Error ===")
    print()
    try:
        print("Testing ValueError...")
        operations["value_error"](value)
    except ValueError as e:
        print("Caught ValueError:", e)
    print()

    try:
        print("Testing ZeroDivisionError...")
        operations["zero_division"](a, b)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    print()

    try:
        print("Testing FileNotFoundError...")
        operations["file_error"](filename)
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    print()

    try:
        print("Testing KeyError...")
        operations["key_error"](dictionary, key)
    except KeyError as e:
        print("Caught KeyError:", e)
    print()

    try:
        print("Testing multiple errors together...")
        operations["value_error"](value)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()
    print("All Error types tested successfully!")


def ft_different_errors() -> None:
    """Run all error type tests."""
    value = "abc"
    a = 10
    b = 0
    filename = "missing.txt"
    dictionary = {"Rose": 1, "Tulip": 2}
    key = "Oak"

    test_error_types(value, a, b, filename, dictionary, key)


if __name__ == "__main__":
    ft_different_errors()
