#!/usr/bin/env python3

import sys


def ft_command_quest() -> None:
    """Receive and print command-line arguments."""
    print("=== Command Quest ===")
    ac = len(sys.argv)
    if ac < 2:
        print("No arguments provided!")

    prog_name = sys.argv[0]
    print(f"Program name: {prog_name}")
    if ac > 1:
        print(f"Arguments received: {ac - 1}")

    i = 1
    while i < ac:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {ac}")


if __name__ == '__main__':
    ft_command_quest()
