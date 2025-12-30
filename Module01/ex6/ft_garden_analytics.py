#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:28:08 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:28:10 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int = 1) -> None:
        self.height += cm
        print(f"{self.name} grew {cm}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, points: int):
        super().__init__(name, height, age, color)
        self.prize_points = points


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def calculate_score(self, plants) -> int:
            score = 0
            for plant in plants:
                score += plant.height
                if isinstance(plant, FloweringPlant):
                    score += 20
            return score

        def count_types(self, plants) -> dict:
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    counts["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    counts["flowering"] += 1
                else:
                    counts["regular"] += 1
            return counts

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.plants = []
        self.total_growth = 0
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self, cm: int) -> None:
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)
            self.total_growth += cm

    def get_report(self) -> None:
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        count = 0
        for plant in self.plants:
            count += 1
            info = f"- {plant.name}: {plant.height}cm"
            if isinstance(plant, FloweringPlant):
                info += f", {plant.color} flowers (blooming)"
            if isinstance(plant, PrizeFlower):
                info += f", prize points: {plant.prize_points}"
            print(info)
        print(f"\nPlants added: {count}, Total growth: {self.total_growth}cm")
        types = self.stats.count_types(self.plants)
        print(f"Plant types: {types['regular']} regular, {types['flowering']} flowering, {types['prize']} prize flowers\n")

    @staticmethod
    def validate_height(plants: int) -> bool:
        for plant in plants:
            if plant.height <= 0:
                return False
        return True

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    alice.add_plant(Plant("Oak", 100, 365))
    alice.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 45, "yellow", 10))
    bob.add_plant(FloweringPlant("Tulip", 72, 10, "pink"))

    alice.grow_all(1)

    alice.get_report()

    alice_score = alice.stats.calculate_score(alice.plants)
    bob_score   = bob.stats.calculate_score(bob.plants)

    print(f"Height validation test: {GardenManager.validate_height(alice.plants)}")
    print(f"Garden scores Alice: {alice_score}, Bob: {bob_score}")
    GardenManager.create_garden_network()

if __name__ == "__main__":
    ft_garden_analytics()
