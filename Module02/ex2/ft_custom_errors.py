#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_tank(tank: dict) -> None:
    if tank['water'] < 5:
        raise WaterError("Not enough water in the tank!")
    if tank['water'] > 200:
        raise WaterError("Tank overflow! Cannot exceed 200 liters")
    print(f"Tank has enough water: Current: {tank['water']}")


def fill_tank(tank: dict, amount: int) -> None:
    if tank['water'] + amount > 200:
        raise WaterError("Could not be filled due to the risk of overflow.")
    tank['water'] += amount
    print("Tank filled correctly!")
    print(f"Current: {tank['water']}")


def check_plant(plant: dict, irrigate: int, tank) -> None:
    if tank['water'] < irrigate:
        raise PlantError(f"Not enough water to irrigate {plant['name']}!")
    if irrigate < 2:
        raise PlantError(f"{plant['name']} is wilting!")
    if irrigate > 4:
        raise PlantError(f"{plant['name']} has drowned.")
    tank['water'] -= irrigate
    print("The plant was watered correctly!")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    tank = {'water': 0}

    tomato = {'name': 'Tomato Plant'}

    print("Testing WaterError...")
    try:
        check_tank(tank)
    except WaterError as e:
        print("Caught WaterError:", e)
        print()

    print("Testing PlantError...")
    try:
        check_plant(tomato, 3, tank)
    except PlantError as e:
        print("Caught PlantError:", e)
        print()

    print("Testing catching all garden errors...")
    try:
        check_tank(tank)
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        check_plant(tomato, 3, tank)
    except GardenError as e:
        print("Caught a garden error:", e)

    print()
    print("All custom error types work correctly!")


if __name__ == '__main__':
    ft_custom_errors()
