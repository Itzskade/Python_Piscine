#!/usr/bin/env python3

import alchemy
import alchemy.elements


def ft_sacred_scroll() -> None:
    """
    Show creating elements via module and
    package-level access, including metadata.
    """
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")

    print("alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")

    print("alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")

    print("alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")
    print()

    print("Testing package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): "
          f"{alchemy.elements.create_fire()}")

    print("alchemy.create_water(): "
          f"{alchemy.elements.create_water()}")

    try:
        print("alchemy.create_earth(): "
              f"{alchemy.elements.create_earth()}")

        print("alchemy.create_air(): "
              f"{alchemy.elements.create_air()}")
    except Exception:
        print("alchemy.create_earth(): AttributeError - not exposed")
        print("alchemy.create_air(): AttributeError - not exposed")
    print()

    print("Package metadata:")
    print(f"Version {alchemy.__version__}")
    print(f"Author {alchemy.__author__}")


if __name__ == '__main__':
    ft_sacred_scroll()
