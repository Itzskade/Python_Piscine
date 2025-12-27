#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:28:52 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:28:54 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List

class WateringError(Exception):
    pass


def watering_plant(plant: str) -> None:
    if plant is None:
        raise WateringError(f"Error: Cannot water {plant} - invalid plant!")
    print(f"Watering {plant}")


def water_plants(plant_list: List[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            watering_plant(plant)
    except WateringError as e:
        print(e)
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system(): 
    plant_list = ['tomato', 'lettuce', 'carrots']
    error_list = ['tomato', None, 'carrots']

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_list)
    print()
    print("Testing with errors...")
    water_plants(error_list)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == '__main__':
    test_watering_system()
