#!/usr/bin/env python3

class Plant:
    """Represents a plant with height (cm) and age (days)."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        """Display the plant's info."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory() -> None:
    """Create plants and display their info and total count."""
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 15, 20),
        ("Cactus", 10, 25),
        ("Sunflower", 20, 18),
        ("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    total_plants = 0
    for data in plant_data:
        new_plant = Plant(*data)
        new_plant.display_info()
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")


if __name__ == "__main__":
    ft_plant_factory()
