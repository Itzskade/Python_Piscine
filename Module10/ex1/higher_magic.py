#!/usr/bin/env python3

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs), spell2(*args, **kwargs)
        )


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args, **kwargs: (
        spell(*args, **kwargs)
        if condition(*args, **kwargs)
        else "Spell fizzled"
        )


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args, **kwargs: [s(*args, **kwargs) for s in spells]


def main() -> None:
    def fireball(target) -> str:
        return f"Fireball hits {target}"

    def heal(target) -> str:
        return f"Heals {target}"

    def lightning(target) -> str:
        return f"{target} was electrified"

    def blizzard(target) -> str:
        return f"{target} was frozen"

    def base_spell() -> int:
        return 10

    def condition(target=None) -> bool:
        return target is not None and target != ""

    print("=" * 40)
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    amplified_fireball = power_amplifier(base_spell, 3)
    result = amplified_fireball()
    print(f"Original: {base_spell()}, Amplified: {amplified_fireball()}")

    print("\nTesting conditional caster...")
    cast_if_dragon = conditional_caster(condition, fireball)
    print(cast_if_dragon("Dragon"))
    print(cast_if_dragon())

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning, blizzard])
    result = sequence("Knight")
    for i in result:
        print("-", i)
    print()
    print("=" * 40)


if __name__ == "__main__":
    main()
