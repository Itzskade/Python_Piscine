#!/usr/bin/env python3

from alchemy.grimoire import record_spell, validate_ingredients


def ft_circular_curse() -> None:
    """Test ingredient validation and spell recording functionality."""
    print("=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")
    print("validate_ingredients('fire air'): "
          f"{validate_ingredients('fire air')}")
    print("validate_ingredients('dragon scales'): "
          f"{validate_ingredients('dragon scales')}")
    print()

    print("Testing spell recording with validation:")
    print(f"record_spell('Fireball', 'fire air'): "
          f"{record_spell('Fireball', 'fire air')}")
    print(f"record_spell('Dark magic', 'shadow'): "
          f"{record_spell('Drak Magic', 'shadow')}")
    print()

    print("Testing late import technique:")
    print(f"record_spell('Lightning', 'air'): "
          f"{record_spell('Lightning', 'air')}")
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == '__main__':
    ft_circular_curse()
