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
from typing import Optional, Tuple

def parse_coordinates(string: str) -> Optional[Tuple[int, int, int]]:
    try:
        parts = string.split(",")
        if len(parts) != 3:
            print("Error parsing coordinates: Invalid coordinate format")
            return None
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        return None


def euclidean_distance(origin: Tuple[int, int, int], point: Tuple[int, int, int]) -> float:
    x1, y1, z1 = origin
    x2, y2, z2 = point
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)

    if len(sys.argv) <= 1:
        print("No coordinates provided via command line.\n")
        return

    for arg in sys.argv[1:]:
        print(f"Parsing coordinates: \"{arg}\"")
        pos = parse_coordinates(arg)
        if pos is None:
            print()
            continue
        x, y, z = pos
        print(f"Position created: {pos}")
        d = euclidean_distance(origin, pos)
        print(f"Distance between {origin} and {pos}: {euclidean_distance(origin, pos):.2f}\n")

    print("Unpacking demonstration:")
    print(f"Player at x={x}, y ={y}, z={z}")
    print(f"Coordinates: X={x}, Z={z}, Y={y}")

if __name__ == "__main__":
    ft_coordinate_system()

