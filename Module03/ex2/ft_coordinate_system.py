#!/usr/bin/env python3

import sys
import math


def parse_coordinates(string: str) -> tuple | None:
    """Convert "x,y,z" string to (x, y, z) tuple; returns None if invalid."""
    try:
        parts = string.split(",")
        if len(parts) != 3:
            print("Error parsing coordinates: Invalid coordinate format")
            return None
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        return None


def euclidean_distance(origin: tuple, point: tuple) -> float:
    """Return the Euclidean distance between origin and point in 3D."""
    x1, y1, z1 = origin
    x2, y2, z2 = point
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def ft_coordinate_system() -> None:
    """
    Process sys.argv coordinates,
    calculate distances,
    and show the last valid point.
    """
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
        print(f"Position created: {pos}")
        dist = euclidean_distance(origin, pos)
        print(f"Distance between {origin} and {pos}: {dist:.2f}\n")

    if pos is None:
        x, y, z = pos
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Z={z}, Y={y}")


if __name__ == "__main__":
    ft_coordinate_system()
