#!/usr/bin/env python3

class Plant:
    """Represents name, height(cm) and age(days) of a plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Increase height by cm."""
        self.height += cm
        print(f"{self.name} grew {cm}cm")


class FloweringPlant(Plant):
    """Plant with flowers and color."""
    def __init__(self, name: str, height: int,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    """Flowering plant with prize points"""
    def __init__(self, name: str, height: int,
                 age: int, color: str, points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = points


class GardenManager:
    """Manages a garden and plant statistics"""
    total_gardens = 0

    class GardenStats:
        """Analytics for a garden."""
        def calculate_score(self, plants) -> int:
            """Compute total score of plants."""
            score = 0
            for plant in plants:
                score += plant.height
                if isinstance(plant, FloweringPlant):
                    score += 20
            return score

        def count_types(self, plants) -> dict[str, int]:
            """Count plant types"""
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    counts["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    counts["flowering"] += 1
                else:
                    counts["regular"] += 1
            return counts

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        self.total_growth = 0
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        """Add a plant."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self, cm: int) -> None:
        """Grow all plants by cm."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)
            self.total_growth += cm

    def get_report(self) -> None:
        """Print garden summary."""
        print(f"=== {self.owner_name}'s Garden Report ===")
        count = 0
        for plant in self.plants:
            count += 1
            info = f"- {plant.name}: {plant.height}cm"
            if isinstance(plant, FloweringPlant):
                info += f", {plant.color} flowers (blooming)"
            if isinstance(plant, PrizeFlower):
                info += f", prize points: {plant.prize_points}"
            print(info)
        print()
        print(f"Plants added: {count}, Total growth: {self.total_growth}cm")
        types = self.stats.count_types(self.plants)
        print(
            f"Plant types: {types['regular']} regular, {types['flowering']} "
            f"flowering, {types['prize']} prize flowers"
        )
        print()

    @staticmethod
    def validate_height(plants: list) -> bool:
        """Check if all plants have positive height."""
        for plant in plants:
            if plant.height <= 0:
                return False
        return True

    @classmethod
    def create_garden_network(cls) -> None:
        """Show total gardens managed"""
        print(f"Total gardens managed: {cls.total_gardens}")


def ft_garden_analytics() -> None:
    """Demo of GardenManager system."""
    print("=== Garden Management System Demo ===")
    print()

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")
    alice.add_plant(Plant("Oak", 100, 365))
    alice.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 45, "yellow", 10))
    bob.add_plant(FloweringPlant("Tulip", 72, 10, "pink"))
    print()
    alice.grow_all(1)
    print()
    alice.get_report()
    print(
        "Height validation test: "
        f"{GardenManager.validate_height(alice.plants)}"
    )
    alice_score = alice.stats.calculate_score(alice.plants)
    bob_score = bob.stats.calculate_score(bob.plants)
    print(f"Garden scores Alice: {alice_score}, Bob: {bob_score}")
    GardenManager.create_garden_network()


if __name__ == "__main__":
    ft_garden_analytics()
