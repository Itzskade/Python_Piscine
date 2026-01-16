from typing import Any, Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: Any, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        available_mana: int = game_state.get('available_mana', 0)
        if self.is_playable(available_mana):
            artifact = {
                    'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': self.effect
                    }
        else:
            artifact = {
                    'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': self.effect
                    }
        return artifact

    def active_ability(self) -> Dict[str, Any]:
        effect = {
                'durability': self.durability,
                'effect': self.effect
                }
        return effect
