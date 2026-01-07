#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with a name, height(cm), and age(days)."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Increase the plant's height by "
        "the specified number of centimeters."""
        self.height += cm

    def age_up(self) -> None:
        """Increment the plant's age by one day."""
        self.age += 1

    def get_info(self) -> None:
        """Display plant info"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth():
    """Simulate a week's growth and show the plant's info and weeks growth"""
    rose = Plant('Rose', 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)

    plants = (rose, sunflower, cactus)

    selected = sunflower
    days = 7
    grow = 1
    initial_height = selected.height

    print("=== Day 1 ===")
    selected.get_info()

    for day in range(2, days + 1):
        for plant in plants:
            plant.grow(grow)
            plant.age_up()
        if day % 7 == 0:
            print(f"=== Day {day} ===")
            selected.get_info()
            growth = selected.height - initial_height
            initial_height = selected.height
            print(f"Growth this week: +{growth}cm")


if __name__ == '__main__':
    ft_plant_growth()
