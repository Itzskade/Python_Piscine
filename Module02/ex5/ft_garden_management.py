#!/usr/bin/env python3

class GardenError(Exception):
    pass


class EmptyName(GardenError):
    pass


class WaterPlants(GardenError):
    pass


class CheckHealth(GardenError):
    pass


class GardenManager:
    """Manages garden operations."""
    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name
        self.plants: list[dict] = []

    def add_plant(self, plant: dict) -> None:
        """Add a plant safely, catching errors if invalid."""
        try:
            if plant is None:
                raise EmptyName("Error adding plant: "
                                "Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant['name']} successfully")
        except EmptyName as e:
            print(e)

    def water_plants(self, tank: dict, amount: int) -> dict:
        """Water all plants, handling errors and cleanup."""
        print("Watering plants...")
        try:
            for plant in self.plants:
                try:
                    if plant is None:
                        raise WaterPlants("Cannot water invalid plant!")
                    if tank['water'] < amount:
                        raise WaterPlants(f"Not enough water! {tank['water']} "
                                          "remaining")
                    plant['water'] += amount
                    tank['water'] -= amount
                    print(f"Watering {plant['name']} - success")
                except WaterPlants as e:
                    print(e)
        finally:
            print("Closing watering system (cleanup)\n")
        return tank

    def check_health(self) -> None:
        """Check a plant's water and sunlight levels and report."""
        for plant in self.plants:
            try:
                if plant is None:
                    raise CheckHealth("Invalid plant!")
                if plant['water'] < 1:
                    raise CheckHealth(f"Error checking {plant['name']}: "
                                      f"Water level {plant['water']} "
                                      "is too low (min 1)")
                if plant['water'] > 10:
                    raise CheckHealth(f"Error checking {plant['name']}: "
                                      f"Water level {plant['water']} "
                                      "is too high (max 10)")
                if plant['sunlight'] < 2:
                    raise CheckHealth(f"Error checking {plant['name']}: "
                                      f"Sunlight hours {plant['sunlight']} "
                                      "is too low (min 2)")
                if plant['sunlight'] > 12:
                    raise CheckHealth(f"Error checking {plant['name']}: "
                                      f"Sunlight hours {plant['sunlight']} "
                                      "is too high (max 12)")
                print(f"{plant['name']}: healthy (water: {plant['water']}, "
                      f"sun: {plant['sunlight']})")
            except CheckHealth as e:
                print(e)

    def check_tank(self, tank: dict, amount: int) -> None:
        """Check if tank can supply and receive water safely."""
        if tank['water'] + amount > 200:
            raise GardenError("Caught GardenError: Could not be "
                              "filled due to the risk of overflow")
        print("Tank could be filled")

    def fill_tank(self, tank: dict, amount: int) -> None:
        """Fill the tank safely, recovering from errors."""
        try:
            self.check_tank(tank, amount)
        except GardenError as e:
            print("Testing error recovery...")
            print(e)
            print("System recovered and continuing...\n")
        else:
            tank['water'] += amount
            print("Tank filled correctly! "
                  f"Current water: {tank['water']} liters")


def ft_garden_demo() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager("Alice")
    tank = {'water': 10}

    plant_list = [
        {'name': 'tomato', 'water': 0, 'sunlight': 8},
        {'name': 'lettuce', 'water': 10, 'sunlight': 1},
        None
    ]

    print("Adding plants to garden...")
    for plant in plant_list:
        manager.add_plant(plant)
    print()

    tank = manager.water_plants(tank, 5)
    manager.check_health()
    print()

    manager.fill_tank(tank, 201)
    manager.fill_tank(tank, 50)

    print("Garden management system test complete!")


if __name__ == "__main__":
    ft_garden_demo()
