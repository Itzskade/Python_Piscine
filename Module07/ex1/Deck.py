from typing import Any, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck():
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop()
        else:
            return None

    def get_deck_stats(self) -> Dict[str, Any]:
        total_cards = len(self.cards)
        num_creatures = sum(1 for card in self.cards if
                            isinstance(card, CreatureCard))
        num_spells = sum(1 for card in self.cards if
                         isinstance(card, SpellCard))
        num_artifacts = sum(1 for card in self.cards if
                            isinstance(card, ArtifactCard))

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
