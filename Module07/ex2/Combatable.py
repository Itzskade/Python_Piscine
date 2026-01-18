from abc import ABC, abstractmethod
from typing import Any, Dict


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Any) -> Dict[str, Any]:
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        ...

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        ...
