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
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int = 1) -> None:
        self.height += cm
        print(f"{self.name} grew {cm}cm")

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, points: int) -> None:
        super().__init__(name, height, age, color)
        self.points = points

class GardenManager:
    total_gardens = 0

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants: list[Plant] = []
        self.growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self, cm: int) -> None:
        print(f"{self.owner_name} is helping all plants grow...")
        for p in self.plants:
            p.grow(cm)
            self.growth += cm

    def report(self) -> None:
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        for p in self.plants:
            desc = f"- {p.name}: {p.height}cm"
            if isinstance(p, FloweringPlant):
                desc += f", {p.color} flowers (blooming)"
            if isinstance(p, PrizeFlower):
                desc += f", Prize points: {p.points}\n"
            print(desc)
        print(f"Plants added: {len(self.plants)}, Total growth: {self.growth}cm")
        types = {"regular":0,"flowering":0,"prize":0}
        for p in self.plants:
            if isinstance(p, PrizeFlower): 
                types["prize"]+=1
            elif isinstance(p, FloweringPlant): 
                types["flowering"]+=1
            else: 
                types["regular"]+=1
        print(f"Types: {types['regular']} regular, {types['flowering']} flowering, {types['prize']} prize flowers")

    @staticmethod
    def validate_height(h: int) -> bool:
        return h > 0

    @classmethod
    def network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    def score(self) -> int:
        s = 0
        for p in self.plants:
            s += p.height
            if isinstance(p, FloweringPlant): s += 20
        return s

def ft_garden_analytics() -> None:
    print(f"=== Garden Management System Demo ===")
    print() 
    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak",100,365))
    alice.add_plant(FloweringPlant("Rose",25,30,"red"))
    alice.add_plant(PrizeFlower("Sunflower",50,45,"yellow",10))
    
    bob = GardenManager("Bob")
    bob.add_plant(FloweringPlant("Tulip", 72, 10, "pink"))
    print()
    alice.grow_all(1)
    alice.report()
    print()
    print(f"Height validation test: {GardenManager.validate_height(101)}")
    print(f"Garden scores: - Alice: {alice.score()}, Bob: {bob.score()}")
    GardenManager.network()

if __name__ == "__main__":
    ft_garden_analytics()
