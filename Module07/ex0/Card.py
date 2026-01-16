from abc import ABC, abstractmethod
from typing import Any, Dict
from enum import Enum


class Rarity(str, Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if cost < 0:
            raise ValueError("Can't be negative integer")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        ...

    def get_card_info(self) -> Dict[str, Any]:
        info = {
                'name': self.name,
                'cost': self.cost,
                'rarity': self.rarity
                }
        return info

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
