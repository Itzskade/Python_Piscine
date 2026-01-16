#!/usr/bin/env python3

from alchemy.transmutation import basic, advanced


def ft_pathway_debate() -> None:
    """Test creating some things"""
    print("=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {basic.lead_to_gold()}")
    print(f"stone_to_gem(): {basic.stone_to_gem()}")
    print()

    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {advanced.philosophers_stone()}")
    print(f"elixir_of_life(): {advanced.elixir_of_life()}")
    print()

    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{basic.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{advanced.philosophers_stone()}")
    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == '__main__':
    ft_pathway_debate()
