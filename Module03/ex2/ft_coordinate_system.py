#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:29:54 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:29:57 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math
from typing import Tuple

def parse_coordinates(string: str):
    numbers = string.split(',')
    tmp = []
    i = 0
    try:
        while i < 3:
            tmp.append(int(numbers[i]))
            i += 1
    except ValueError as e:
        print(f"Error parsing coordinates:", e)
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
    coordinates = tuple(tmp)
    return coordinates

def euclidean_distance(coordinates: tuple):
    position = (0, 0, 0)
    x2, y2, z2 = coordinates
    x1, y1, z1 = position
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance

def ft_coordinate_system():
    print("=== Game Coordinate System ===\n")
 
    position = (0, 0, 0)
    test1 = "10,20,5"
    test2 = "3,4,0"
    test3 = "abc,def,ghi"
    coordinates1 = parse_coordinates(test1)
    coordinates2 = parse_coordinates(test2)
 
    x, y, z = coordinates2

    print(f"Position created: {coordinates1}")
    print(f"Distance between {position} and {coordinates1}: {euclidean_distance(coordinates1):.2f}")
    print()
    
    print(f"Parsing coordinates: \"{test2}\"")
    print(f"Position created: {coordinates2}")
    print(f"Distance between {position} and {coordinates2}: {euclidean_distance(coordinates2)}")
    print()
    
    print(f"Parsing invalid coordinates: \"{test3}\"")
    coordinates3 = parse_coordinates(test3)
    print()
    
    print(f"Unpacking demostration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == '__main__':
    ft_coordinate_system()
