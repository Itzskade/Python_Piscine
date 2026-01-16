from alchemy.elements import create_fire, create_water
from alchemy.elements import create_air, create_earth


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    return ("Invisibility potion brewed with "
            f"{create_air()} and {create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: {create_fire()} "
            f"{create_water()}) {create_earth()} {create_air()}")
