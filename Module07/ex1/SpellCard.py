from __future__ import annotations
from typing import Any, Dict, List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature


class UnknownEffect(Exception):
    """Raised when a spell effect type is not recognized."""
    pass


class TargetError(Exception):
    """Raised when a spell has no valid targets."""
    pass


class SpellCard(Card):
    """A spell card with a specific effect type."""
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """Create a spell with its effect type."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Return basic info when the spell is cast."""
        spell = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': f"Spell cast: {self.effect_type}"
                }
        return spell

    def resolve_effects(self, targets: List[Creature]) -> Dict[str, Any]:
        """Apply the spell effect to the given targets."""
        if not targets:
            raise TargetError("No targets to apply effects")
        target_name = ", ".join(target.name for target in targets)

        if self.effect_type == "damage":
            effect = f"Deals 3 damage to {target_name}"
        elif self.effect_type == "heal":
            effect = f"Heals 3 health for {target_name}"
        elif self.effect_type == "buff":
            effect = f"Buff stats of {target_name}"
        elif self.effect_type == "debuff":
            effect = f"Debuffs stats of {target_name}"
        else:
            raise UnknownEffect("Unknown effect cannot be applied")
        return {
            'effect': effect,
            'targets': target_name
        }
