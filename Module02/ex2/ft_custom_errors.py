#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:28:42 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:28:43 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Dict

class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

#check tank water func
def check_tank(tank Dict[str, int]): -> None:
    if tank['water'] < 5:
        raise WaterError("Not enough water in the tank!")
    if tank['water'] > 200:
        raise WaterError("Tank overflow! Cannot exceed 200 liters")
    print(f"Tank has enough water: Current: {tank['water']}")

#fill tank water func
def fill_tank(tank: Dict[str, int], amount: int): -> None:
    if tank['water'] + amount > 200:
        raise WaterError("Could not be filled due to the risk of overflow.")
    tank['water'] += amount
    print(f"Tank filled correctly!\nCurrent: {tank['water']}")
    
#check plant status by water
def check_plant(plant: Dict[str, str], irrigate: int, tank): -> None:
    if tank['water'] < irrigate:
        raise PlantError(f"Not enough water to irrigate {plant['name']}!")
    if irrigate < 2:
        raise PlantError(f"{plant['name']} is wilting!")
    if irrigate > 4:
        raise PlantError(f"{plant['name']} has drowned.")
    tank['water'] -= irrigate
    print("The plant was watered correctly!")
    
#tester
def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    
    #create tank (dictionary)
    tank = {'water': 0}

    #create plants (dictionary)
    tomato = {'name': 'Tomato Plant'}
    lettuce = {'name': 'Lettuce Plant'}

    #WaterError Test
    print("Testing WaterError...") 
    try:
        check_tank(tank)
    except WaterError as e:
        print("Caught WaterError:", e)
        print()

    #PlantError Test
    print("Testing PlantError...")
    try:
        check_plant(tomato, 3, tank)
    except PlantError as e:
        print("Caught PlantError:", e)
        print()

    #GardenError Test
    print("Testing catching all garden errors...")
    try:
        check_tank(tank)
    except GardenError as e:
        print("Caught a garden error:", e)
    
    try:
        check_plant(tomato, 3, tank)
    except GardenError as e:
        print("Caught a garden error:", e)

    print()
    print("All custom error types work correctly!")

if __name__ == '__main__':
    ft_custom_errors()
