#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()

    dragon = CreatureCard('Fire Dragon', 5, "Legendary", 7, 5)
    lightning_bolt = SpellCard('Lightning Bolt', 3, 'Rare',
                               "Deal 3 damage to target")
    crystal = ArtifactCard('Mana Crystal', 2, 'Epic', 'Permanent',
                           "Permanent: +1 mana per turn")

    deck.add_card(dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(crystal)

    deck.shuffle()

    print("Deck stats:", deck.get_deck_stats())
    print()
    print("Drawing and playing cards:")
    print()
    while deck.cards:
        drawn = deck.draw_card()
        card_type = drawn.__class__.__name__
        print(f"Drew: {drawn.name} ({card_type})")
        result = drawn.play({"mana": 5})
        print("Play result:", result)
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
