#!/usr/bin/env python3

from functools import wraps
import inspect
import time
import random


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> callable:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.10f} seconds")
        return print("Result:", result)
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator_factory(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> callable:
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            power = bound.arguments['power']
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator_factory


def retry_spell(max_attempts: int) -> callable:
    def retry_decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs) -> callable:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    print(f"Spell failed, retrying...({i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return retry_decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if all(i.isalpha() or i.isspace() for i in name) and len(name) >= 3:
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("=" * 40)

    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        return "Fireball cast!"
    fireball()

    print("\nTesting power validator...")

    @power_validator(10)
    def spell(name: str, power: int) -> str:
        return f"{name} cast with {power} power!"
    print(spell('Fireball', 5))
    print(spell('Lightning', 20))

    print("\nTesting retry spell...")

    @retry_spell(3)
    def spell(spell_name: str) -> str:
        if random.random() > 0.7:
            return f"{spell_name} cast!"
        else:
            raise ValueError("Spell failed")
    print(spell('Blizzard'))

    print("\nTesting MageGuild...")

    guild = MageGuild()
    print(guild.validate_mage_name('Roger'))
    print(guild.validate_mage_name('Al'))
    print(guild.cast_spell('Lightning', 15))
    print(guild.cast_spell('Blizzard', 5))

    print()
    print("=" * 40)


if __name__ == '__main__':
    main()
