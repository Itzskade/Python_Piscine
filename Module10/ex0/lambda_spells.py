#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    most = max(powers, key=lambda p: p)
    less = min(powers, key=lambda p: p)
    avg = sum(powers) / len(powers)
    return {
        'max_power': most,
        'min_power': less,
        'avg_power': avg
    }


def main():
    artifacts = [
        {
            'name': 'Shadow Blade',
            'power': 87,
            'type': 'relic'
            },
        {
            'name': 'Wind Cloak',
            'power': 71,
            'type': 'weapon'
            },
        {
            'name': 'Wind Cloak',
            'power': 97,
            'type': 'armor'
            },
        {
            'name': 'Wind Cloak',
            'power': 103,
            'type': 'weapon'
            }
            ]

    mages = [
        {
            'name': 'Nova',
            'power': 95,
            'element': 'ice'
            },
        {
            'name': 'Luna',
            'power': 91,
            'element': 'fire'
            },
        {
            'name': 'Zara',
            'power': 74,
            'element': 'shadow'
            },
        {
            'name': 'Luna',
            'power': 97,
            'element': 'ice'
            },
        {
            'name': 'Sage',
            'power': 98,
            'element': 'lightning'
            }
            ]

    spells = ['heal', 'lightning', 'tsunami', 'darkness']

    print("=" * 40)
    print("\nTesting artifact sorter...")
    print(artifact_sorter(artifacts))

    print("\nTesting spell transformer...")
    transformer = spell_transformer(spells)
    for spell in transformer:
        print(spell, end=" ")
    print()

    print("\nTesting power filter...")
    print(power_filter(mages, 97))

    print("\nTesting mage stats...")
    print(mage_stats(mages))
    print()
    print("=" * 40)


if __name__ == '__main__':
    main()
