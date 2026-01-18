from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str,
                   targets: List[str]) -> Dict[str, Any]:
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        ...

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        ...
