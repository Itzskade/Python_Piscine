from typing import Any, Dict, List
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        spell = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': f"Spell cast: {self.effect_type}"
                }
        return spell

    def resolve_effects(self, targets: List[str]) -> Dict[str, Any]:
        effect = {
                'target': targets,
                'effect_type': self.effect_type
                }
        return effect
