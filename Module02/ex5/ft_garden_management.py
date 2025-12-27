#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:29:15 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:29:18 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List, Dict

class GardenManager(Exception):
    pass

class AddPlants(GardenManager):
    pass


class WaterPlants(GardenManager):
    pass


class CheckHealth(GardenManager):
    pass

class GardenError(GardenManager):
    pass

def adding_plant_garden(plant_list: list, name: str, water: int, sunlight: int) -> None:
    plant_list.append({
            'name': name,
            'water': water,
            'sunlight': sunlight
    })
    print(f"Added {name} successfully")

def add_plant_garden(plant_list, values) -> None:
    try:
        if values is None:
            raise AddPlants("Error adding plant: Plant name cannot be empty!")
        adding_plant_garden(plant_list, values[0], values[1], values[2])
    except AddPlants as e:
        print(e)


def watering_plants(plant: dict, tank: dict, irrigate: int) -> None:
    if plant is None:
        raise WaterPlants(f"Cannot water invalid plant!")
    if tank['water'] < irrigate:
        raise WaterPlants(f"Not enough water! Need {irrigate}, have {tank['water']}")
    tank['water'] -= irrigate
    plant['water'] += irrigate
    print(f"Watering {plant['name']} - success")

def water_plants(plant_list: list, tank: dict, irrigate: int) -> None:
    print("Watering plants...")
    try:
        for plant in plant_list:
            watering_plants(plant, tank, irrigate)
    except WaterPlants as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)\n")


def sunlighting_plants(plant: dict, sunlight: int) -> None:
    if plant is None:
        raise CheckHealth("Invalid plant!")
    plant['sunlight'] += sunlight
    #print(f"{plant['name']} received {sunlight} hours of sunlight")

def sunlight_plants(plant_list: list, sunlight: int) -> None:
    try:
        for plant in plant_list:
            sunlighting_plants(plant, sunlight)
    except CheckHealth as e:
        print(e)


def check_tank(tank: dict, amount: int) -> None:
    if tank['water'] < 1:
        raise GardenError("Caught GardenError: Not enough water in tank")
    if tank['water'] + amount > 200:
        raise GardenError("Caught GardenError: Could not be filled due to the risk of overflow")
    print("Tank has enough water")

def fill_tank(tank: dict, amount: int) -> None:
    try:
        check_tank(tank, amount)
    except GardenError as e:
        print("Testing error recovery...")
        print (e)
        print("System recovered and continuing...\n")
    else:
        tank['water'] += amount
        print(f"Tank filled correctly!\nCurrent water: {tank['water']} liters")


def check_plant_health(plant: dict):
    if plant['name'] is None:
        raise CheckHealth("Error: Plant name cannot be empty!")
    if plant['water'] < 1:
        raise CheckHealth (f"Error checking {plant['name']}: Water level {plant['water']} is too low (min 1)")
    if plant['water'] > 10:
        raise CheckHealth (f"Error checking {plant['name']}: Water level {plant['water']} is too high (max 10)")
    if plant['sunlight'] < 2:
        raise CheckHealth (f"Error checking {plant['name']}: Sunlight hours {plant['sunlight']} is too low (min 2)")
    if plant['sunlight'] > 12:
        raise CheckHealth (f"Error checking {plant['name']}: Sunlight hours {plant['sunlight']} is too high (max 12)")
    print(f"{plant['name']} healthy (water: {plant['water']}, sun: {plant['sunlight']})")

def test_plant_checks(plant_list: list) -> None:
    print("Checking plant health...")
    for plant in plant_list:
        try:
            check_plant_health(plant)
        except CheckHealth as e:
            print(e)
    print()


def ft_garden_management():
    print("=== Garden Management System ===\n")

    tank = {'water': 10}
    plant_list = []

    print("Adding plants to garden...")
    for plant in (('tomato', 0, 0), ('lettuce', 10, 0), None):
            add_plant_garden(plant_list, plant)
    print()

    water_plants(plant_list, tank, 5)
    sunlight_plants(plant_list, 8)
    test_plant_checks(plant_list)
    fill_tank(tank, 10)
    
    print("Garden management system test complete!")


if __name__ == '__main__':
    ft_garden_management()

