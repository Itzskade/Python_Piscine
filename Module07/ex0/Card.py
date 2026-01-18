from abc import ABC, abstractmethod
from typing import Any, Dict


class Card(ABC):
    """Base class for all cards."""
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Create a card with name, cost and rarity."""
        if cost < 0:
            raise ValueError("Can't be negative integer")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Apply the card effect to the game state."""
        ...

    def get_card_info(self) -> Dict[str, Any]:
        """Return card info as a dictionary."""
        info = {
                'name': self.name,
                'cost': self.cost,
                'rarity': self.rarity
                }
        return info

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with given mana."""
        return available_mana >= self.cost
