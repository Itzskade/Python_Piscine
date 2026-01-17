from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        ...

    @abstractmethod
    def get_rank_info(self) -> Dict[str, int]:
        ...
