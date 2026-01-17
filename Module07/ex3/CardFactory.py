from abc import ABC, abstractmethod
from typing import List, Dict
from ex0.Card import Card


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        ...

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        ...

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, List[Card]]:
        ...

    @abstractmethod
    def get_supported_types(self) -> List[str]:
        ...
