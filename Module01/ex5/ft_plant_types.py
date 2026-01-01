#!/usr/bin/env python3

class Plant:
    """Represents name, height(cm) and age(days) of a plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Tree(Plant):
    """Represents name, height(cm), age(days), trunk diameter(cm) and shade(m²) of a tree."""
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Prints how many shade tree provides"""
        print(f"{self.name} provides {self.trunk_diameter * 1.5} square meters of shade\n")


class Flower(Plant):
    """Represents name, height(cm), age(days), color and blooming status of a flower."""
    def __init__(self, name: str, height: int, age: int, color: str, is_blooming: bool = True) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def bloom(self) -> None:
        """Prints the blooming status of the flower."""
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} is not blooming right now.\n")


class Vegetable(Plant):
    """Represents name, height(cm), age(days), harvest season and nutrition value of a vegetable."""
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutrition: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrition = nutrition

    def nutritional_value(self) -> None:
        """Prints the nutritional value of the vegetable."""
        print(f"{self.name}, is rich in {self.nutrition}\n")


def ft_plant_types() -> None:
    """Demonstrate different plant types and their properties."""
    plants = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 1500, 45),
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 45, "yellow", is_blooming=False),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 35, 60, "spring", "beta-carotene")
    ]

    print("=== Garden Plant Types ===\n")
    
    for plant in plants:
        if plant.__class__.__name__ == "Tree":
            print(f"{plant.name} (Tree): {plant.height}cm, {plant.age} days, {plant.trunk_diameter} diameter")
            plant.produce_shade()
        elif plant.__class__.__name__ == "Flower":
            print(f"{plant.name} (Flower): {plant.height}cm, {plant.age} days, {plant.color} color")
            plant.bloom()
        elif plant.__class__.__name__ == "Vegetable":
            print(f"{plant.name} (Vegetable): {plant.height}cm, {plant.age} days, {plant.harvest_season} harvest")
            plant.nutritional_value()


if __name__ == "__main__":
    ft_plant_types()
