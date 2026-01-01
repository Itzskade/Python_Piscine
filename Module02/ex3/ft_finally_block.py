#!/usr/bin/env python3

class WateringError(Exception):
    pass


def watering_plant(plant: str) -> None:
    if plant is None:
        raise WateringError(f"Error: Cannot water {plant} - invalid plant!")
    print(f"Watering {plant}")


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            watering_plant(plant)
    except WateringError as e:
        print(e)
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None: 
    plant_list = ['tomato', 'lettuce', 'carrots']
    error_list = ['tomato', None, 'carrots']

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_list)
    print()
    print("Testing with errors...")
    water_plants(error_list)
    print()
    print("Cleanup always happens, even with errors!")

if __name__ == '__main__':
    test_watering_system()
