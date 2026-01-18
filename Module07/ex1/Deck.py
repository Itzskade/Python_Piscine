from typing import Any, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature
from ex1.SpellCard import SpellCard as Spell
from ex1.ArtifactCard import ArtifactCard as Artifact
import random


class DeckError(Exception):
    """Raised when a deck operation fails."""
    pass


class Deck():
    """A collection of cards that can be drawn, shuffled or inspected."""
    def __init__(self) -> None:
        """Create an empty deck."""
        self.cards = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw and return the top card, or raise error if empty."""
        if self.cards:
            return self.cards.pop()
        raise DeckError("No more cards to draw")

    def get_deck_stats(self) -> Dict[str, Any]:
        """Return deck statistics: counts and average cost."""
        total_cards = len(self.cards)
        num_creatures = sum(1 for card in self.cards if
                            isinstance(card, Creature))
        num_spells = sum(1 for card in self.cards if
                         isinstance(card, Spell))
        num_artifacts = sum(1 for card in self.cards if
                            isinstance(card, Artifact))

        avg_cost = 0
        if total_cards > 0:
            total_cost = 0
            for card in self.cards:
                total_cost += card.cost
            avg_cost = total_cost / total_cards
        else:
            avg_cost = 0

        total = {
                'total_cards': total_cards,
                'creatures': num_creatures,
                'spells': num_spells,
                'artifacts': num_artifacts,
                'avg_cost': avg_cost
                }
        return total
