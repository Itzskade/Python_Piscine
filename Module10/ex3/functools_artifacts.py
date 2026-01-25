#!/usr/bin/env python3

import operator
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
            'add': operator.add,
            'multiply': operator.mul,
            'max': max,
            'min': min
            }

    if operation not in operations:
        raise ValueError("Unknown operation")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
            'fire_enchant': partial(base_enchantment, 50, 'fire'),
            'ice_enchant': partial(base_enchantment, 50, 'ice'),
            'lightning_enchant': partial(base_enchantment, 50, 'lightning')
            }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Incorrect position must be positive")
    if 0 <= n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(arg):
        raise TypeError(f"Cannot handle type {type(arg)}")

    @spell.register
    def _(damage: int):
        return f"Damage spells deals {damage} damage"

    @spell.register
    def _(enchant: str):
        return f"Enchantment spell {enchant}"

    @spell.register
    def _(spells: list):
        result = [spell(s) for s in spells]
        return result

    return spell


def main():
    print("=" * 40)
    print("\nTesting spell reducer...")
    spells = [40, 20, 10, 30]
    add = 'add'
    mul = 'multiply'
    top = 'max'

    try:
        print("Sum:", spell_reducer(spells, add))
        print("Product:", spell_reducer(spells, mul))
        print("Max:", spell_reducer(spells, top))

    except ValueError as e:
        print(e)

    print("\nTesting partial enchanter...")
    try:
        def base_enchantment(power, element, target):
            return f"Enchanted {target} with {power} {element}"
        enchant = partial_enchanter(base_enchantment)
        print(enchant['fire_enchant']('Knight'))
        print(enchant['ice_enchant']('Goblin'))
        print(enchant['lightning_enchant']('Dragon'))
        print(enchant['dark_enchant']('Demon'))

    except KeyError:
        print("Enchantment doesn't exist")

    print("\nTesting memoized fibonacci...")
    try:
        position = 10
        position2 = 15
        print(f"Fib({position}):", memoized_fibonacci(position))
        print(f"Fib({position2}):", memoized_fibonacci(position2))

    except ValueError as e:
        print(e)

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    try:
        print(spell(50))
        print()
        print(spell('fire Aura'))
        print()
        for s in spell([50, 'blizzard', 30, 'lightning']):
            print(s)
        print()

    except TypeError as e:
        print(e)
    print("=" * 40)


if __name__ == '__main__':
    main()
