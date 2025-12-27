#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:27:58 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:27:59 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int, shade: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.shade} square meters of shade\n")

class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str, is_blooming: bool = True) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def bloom(self) -> None:
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} is not blooming right now.\n")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutrition: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrition = nutrition

    def nutritional_value(self) -> None:
        print(f"{self.name}, is rich in {self.nutrition}\n")

def ft_plant_types() -> None:
    trees = [
        Tree("Oak", 500, 1825, 50, 78),
        Tree("Pine", 400, 1500, 45, 66)
    ]

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 45, "yellow", is_blooming=False)
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 35, 60, "spring", "beta-carotene")
    ]

    print("=== Garden Plant Types ===\n")
    
    for flower in flowers:
        print(f"{flower.name} (Flower): {flower.height}cm, {flower.age} days, {flower.color} color")
        flower.bloom()

    for tree in trees:
        print(f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, {tree.trunk_diameter} diameter")
        tree.produce_shade()

    for vegetable in vegetables:
        print(f"{vegetable.name} (Vegetable): {vegetable.height}cm, {vegetable.age} days, {vegetable.harvest_season} harvest")
        vegetable.nutritional_value()

if __name__ == "__main__":
    ft_plant_types()
