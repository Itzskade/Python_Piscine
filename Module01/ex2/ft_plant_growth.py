#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with a name, height in cm, and age in days."""
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def grow(self, cm: int) -> None:
        """Increase the plant's height by the specified number of centimeters."""
        self.height += cm

    def age_one_day(self) -> None:
        """Increment the plant's age by one day."""
        self.age += 1

    def get_info(self) -> str:
        """Return a string summarizing the plant's name, height, and age."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_plant_growth() -> None:
    """Simulate a week's growth and show the plant's info and total growth.""""
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())

    for day in range(1, 7):
        rose.age_one_day()
        rose.grow(1)

    print("=== Day 7 ===")
    print(rose.get_info())

    growth = rose.height - rose.initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
