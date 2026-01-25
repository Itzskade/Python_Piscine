#!/usr/bin/env python3

def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulator(increase):
        nonlocal total_power
        total_power += increase
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")
    return {
            'store': store,
            'recall': recall
            }


def main() -> None:
    print("=" * 40)
    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting enchantment factory...")
    sword = enchantment_factory("Flaming")
    shield = enchantment_factory("Frozen")
    print(sword("Sword"))
    print(shield("Shield"))

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    increase = 5
    for i in range(3):
        print(f"Power increased by {increase}: {accumulator(5)}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    data = {
            "quest": "Kill Ender Dragon",
            "level": 52,
            "hp": 1087,
            "weapon": "Flaming Sword"
            }

    for key, value in data.items():
        vault["store"](key, value)

    for key in ["quest", "level", "hp", "weapon", "mana"]:
        print(key, "→", vault["recall"](key))
    print()
    print("=" * 40)


if __name__ == '__main__':
    main()
