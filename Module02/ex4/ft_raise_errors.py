#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Check valid name & plant health based on water & sunlight levels."""
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")
    print(f"Plant {plant_name} is healthy!")


def test_plant_checks() -> None:
    """Test plant health checks with valid & invalid values."""
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health('tomato', 3, 5)
    except ValueError as e:
        print(e)
    print()

    print("Testing empty plant name...")
    try:
        check_plant_health('', 3, 5)
    except ValueError as e:
        print(e)
    print()

    print("Testing bad water level...")
    try:
        check_plant_health('tomato', 15, 5)
    except ValueError as e:
        print(e)
    print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health('tomato', 3, 0)
    except ValueError as e:
        print(e)
    print()

    print("All error raising tests completed!")


if __name__ == '__main__':
    test_plant_checks()
