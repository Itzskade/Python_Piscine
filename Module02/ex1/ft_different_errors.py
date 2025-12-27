#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:28:30 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:28:33 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Dict, Callable

def test_error_types(value: int, a: int, b: int, filename: str, dictionary: Dict[str, int], key: str) -> None:
    operations = garden_operations()
    
    print("=== Garden Error Types Error ===\n")
    try:
        print("Testing ValueError...")
        operations["value_error"](value)
    except ValueError as e:
        print(f"Caught ValueError:", e)
    print()

    try:
        print("Testing ZeroDivisionError...")
        operations["zero_division"](a, b)
    except ZeroDivisionError as e:
        print("Caught ZerorDivisionError:",e )
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

    print("\nAll Error types tested successfully!")


def garden_operations() -> Dict[str, Callable]:
    def garden_value_error(value):
        int(value)

    def garden_zero_division(a, b):
        a / b

    def garden_file_error(filename):
        open(filename)

    def garden_key_error(dictionary, key):
        dictionary[key]

    return {
            "value_error": garden_value_error, 
            "zero_division": garden_zero_division,
            "file_error": garden_file_error, 
            "key_error": garden_key_error 
    }

def ft_different_errors():
    value = "abc"
    a = 10
    b = 0
    filename = "missing.txt"
    dictionary = {"Rose": 1, "Tulip": 2}
    key = "Oak"

    test_error_types(value, a, b, filename, dictionary, key)


if __name__ == "__main__":
    ft_different_errors()
