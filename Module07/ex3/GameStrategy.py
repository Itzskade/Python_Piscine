from abc import ABC, abstractmethod
from typing import Any, List, Dict
from ex0.Card import Card


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: List[Card], battlefield: List[
                Card]) -> Dict[str, Any]:
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        ...

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Card]) -> List[Card]:
        ...
