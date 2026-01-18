from __future__ import annotations
from ex0.Card import Card
from typing import Any, Dict


class CreatureCard(Card):
    """A card representing a creature with attack and health."""
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
            ) -> None:
        """Initialize creature with stats."""
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    @property
    def attack(self) -> int:
        """Return creature attack value."""
        return self._attack

    @attack.setter
    def attack(self, new_attack: int) -> None:
        """Set creature attack, must be positive integer."""
        if not isinstance(new_attack, int):
            raise ValueError("Attack must be an integer value")
        if new_attack <= 0:
            raise ValueError("Attack must be positive integer")
        self._attack = new_attack

    @property
    def health(self) -> int:
        """Return creature health value."""
        return self._health

    @health.setter
    def health(self, new_health: int) -> None:
        """Set creature health, must be positive integer."""
        if not isinstance(new_health, int):
            raise ValueError("Health must be an integer value")
        if new_health <= 0:
            raise ValueError("Health must be positive")
        self._health = new_health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Return effect of playing the creature."""
        played = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': "Creature summoned to battlefield"
                }
        return played

    def attack_target(self, target: CreatureCard) -> Dict[str, Any]:
        """Attack another creature and return combat info."""
        target_name = getattr(target, "name", str(target))
        attack_result = {
                'attacker': self.name,
                'target': target_name,
                'damage_dealt': self.attack,
                'combat_resolved': True
                }
        return attack_result

    def get_card_info(self) -> Dict[str, Any]:
        """Return full creature info including stats."""
        base_info = super().get_card_info()
        base_info.update({
            'attack': self.attack,
            'health': self.health
            })
        return base_info
