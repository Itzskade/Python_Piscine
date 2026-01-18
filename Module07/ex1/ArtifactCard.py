from typing import Any, Dict
from ex0.Card import Card


class ArtifactError(Exception):
    pass


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    @property
    def durability(self):
        return self._durability

    @durability.setter
    def durability(self, new_durability):
        if new_durability is None:
            self._durability = None
            return

        if not isinstance(new_durability, int):
            raise ValueError("Durability must be an integer value")
        if new_durability <= 0:
            raise ValueError("Durability must be a positive integer")
        self._durability = new_durability

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        available_mana: int = game_state.get('available_mana', 0)
        if self.is_playable(available_mana):
            artifact = {
                    'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': self.effect
                    }
        else:
            raise ArtifactError("No enough mana to play this artifact")
        return artifact

    def active_ability(self) -> Dict[str, Any]:
        effect = {
                'durability': self.durability,
                'effect': self.effect
                }
        return effect
