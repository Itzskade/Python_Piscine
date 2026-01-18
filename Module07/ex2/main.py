#!/usr/bin/env python3

from ex2.EliteCard import EliteCard as Elite


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    arcane_warrior = Elite(
        'Arcane Warrior',
        cost=5,
        rarity="Legendary",
        attack_power=5,
        health=10,
        mana=6
        )

    goblin_mage = Elite(
        'Goblin Mage',
        cost=2,
        rarity="Rare",
        attack_power=7,
        health=5,
        mana=10
        )

    try:
        print(f"\nPlaying {arcane_warrior.name} (Elite Card):")
        print(arcane_warrior.play({'available_mana': 13}))

        print("\nCombat phase:")
        attack_result = arcane_warrior.attack("Enemy")
        print("Attack result:", attack_result)
        defend_result = goblin_mage.defend(5)
        print("Defense result:", defend_result)

        print("\nMagic phase:")
        spell_result = arcane_warrior.cast_spell(
                "Fireball", ["Enemy1", "Enemy2"])
        print("Spell cast:", spell_result)
        mana_result = arcane_warrior.channel_mana(5)
        print("Mana channel:", mana_result)
        print()

    except Exception as e:
        print(e)
        print("Summon not performed")


if __name__ == '__main__':
    main()
