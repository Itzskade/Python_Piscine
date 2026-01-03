#!/usr/bin/env python3

def check_temperature(temp_str: str) -> None:
    """Check if temperature is valid for plants (0-40ºC)."""
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} no es un número")
        return None

    if temp < 0:
        print(f"Error: {temp}ºC is too cold for plants (min 0ºC)\n")
    elif temp > 40:
        print(f"Error: {temp}ºC is too hot for plants (max 40ºC)\n")
    else:
        print(f"Temperature {temp}ºC is perfect for plants!\n")


def ft_first_exception():
    """Test temperature checks with various inputs."""
    print("=== Garden Temperature Checker ===\n")
    tests = [20, 100, -50, "abc"]
    for test in tests:
        print(f"Testing temperature: {test}")
        check_temperature(test)
    print("\nAll test completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
