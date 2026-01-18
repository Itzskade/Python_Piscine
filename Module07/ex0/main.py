#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard as Creature


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    game_state = {"available_mana": 6}

    fire_dragon = Creature(
            'Fire Dragon',
            cost=5,
            rarity='Legendary',
            attack=7,
            health=5
            )

    goblin = Creature(
            'Goblin Warrior',
            cost=2,
            rarity='Common',
            attack=3,
            health=2
            )

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print()

    print(f"Playing {fire_dragon.name} with "
          f"{game_state['available_mana']} mana available:")
    print("Playable:", fire_dragon.is_playable(game_state['available_mana']))
    result_play = fire_dragon.play(game_state)
    print("Play result:", result_play)
    print()

    print(f"{fire_dragon.name} attacks {goblin.name}:")
    attack_result = fire_dragon.attack_target(goblin)
    print("Attack result:", attack_result)
    print()

    print("Testing insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(3))
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == '__main__':
    main()
