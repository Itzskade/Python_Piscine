#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard as Creature
from ex1.SpellCard import SpellCard as Spell, UnknownEffect
from ex1.ArtifactCard import ArtifactCard as Artifact, ArtifactError
from ex1.Deck import Deck, DeckError


def main():
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    cards = []
    try:
        dragon = Creature('Fire Dragon', 5, "Legendary", 7, 5)
        cards.append(dragon)

        lightning_bolt = Spell('Lightning Bolt', 3, 'Rare', "damage")
        cards.append(lightning_bolt)

        crystal = Artifact(
            'Mana Crystal', 2, 'Epic', None, "Permanent: +1 mana per turn")
        cards.append(crystal)

    except UnknownEffect as e:
        print("UknownEffect Error", e)
    except ArtifactError as e:
        print("ArtifactError", e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

    try:
        for card in cards:
            deck.add_card(card)
        deck.shuffle()
    except DeckError as e:
        print("DeckError", e)

    print("Deck stats:", deck.get_deck_stats())
    print()
    print("Drawing and playing cards:")
    print()
    while deck.cards:
        drawn = deck.draw_card()
        card_type = drawn.TYPE_ALIAS
        print(f"Drew: {drawn.name} ({card_type})")
        result = drawn.play({"available_mana": 5})
        print("Play result:", result)
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
