#!/usr/bin/env python3

class Plant():
    """Represents Plant.
    Include name, height(cm) and age(days).
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flower.
    Includes name, height(cm), age(days), color & blooming status.
    """
    def __init__(self, name: str, height: int, age: int,
                 color: str, bloom: bool) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def blooming(self):
        """Prints the blooming status of the flower."""
        if self.bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not blooming yet")

    def display_info(self):
        """Display all info of flower"""
        print()
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")
        self.blooming()


class Tree(Plant):
    """
    Represents a tree.
    Includes name, height(cm), age(days), trunk diameter(cm) & shade(m²).
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Prints how many shade tree provides"""
        print(f"{self.name} provides {self.trunk_diameter * 1.56:.0f} "
              "square meters of shade")

    def display_info(self):
        """Display all info of tree"""
        print()
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    """Represents a vegetable.
    Includes name, height(cm), age(days), harvest season & nutrition value.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutrition: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrition = nutrition

    def display_nutritional_value(self) -> None:
        """Prints the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutrition}")

    def display_info(self):
        """Display all info of vegetable"""
        print()
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        self.display_nutritional_value()


def ft_plant_types() -> None:
    """Demonstrate different plant types and their properties."""
    plants_data = [
        Flower('Rose', 25, 30, 'red', True),
        Flower('Tulip', 20, 35, 'yellow', False),
        Tree('Oak', 500, 1825, 50),
        Tree('Pine', 400, 1000, 40),
        Vegetable('Tomato', 80, 90, 'summer', 'vitamine C'),
        Vegetable('Carrot', 50, 50, 'spring', 'vitamine A')
    ]

    print("=== Garden Plant Types ===")

    for plant in plants_data:
        plant.display_info()


if __name__ == '__main__':
    ft_plant_types()
