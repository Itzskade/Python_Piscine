#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:27:45 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:27:45 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class   Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return (f"Created: {self.name}: ({self.height}cm, {self.age} days)")


def ft_plant_factory() -> None:
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 15, 20),
        ("Cactus", 10 , 25),
        ("Sunflower", 20, 18),
        ("Fern", 15, 120) 
    ]

    print("=== Plant Factory Output ===")
    total_plants = 0
    for data in plant_data:
        new_plant = Plant(*data)
        print(new_plant.get_info())
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")

if __name__ == "__main__":
    ft_plant_factory()

