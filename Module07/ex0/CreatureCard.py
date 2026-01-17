from __future__ import annotations
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature
from typing import Any, Dict


class CreatureCard(Card):
    TYPE_ALIAS = "Creature"

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
            ) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    @property
    def attack(self) -> int:
        return self._attack

    @attack.setter
    def attack(self, new_attack: int) -> None:
        if not isinstance(new_attack, int):
            raise ValueError("Attack must be an integer value")
        if new_attack <= 0:
            raise ValueError("Attack must be positive integer")
        self._attack = new_attack

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, new_health: int) -> None:
        if not isinstance(new_health, int):
            raise ValueError("Health must be an integer value")
        if new_health <= 0:
            raise ValueError("Health must be positive")
        self._health = new_health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        played = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': "Creature summoned to battlefield"
                }
        return played

    def attack_target(self, target: Creature) -> Dict[str, Any]:
        target_name = getattr(target, "name", str(target))
        attack_result = {
                'attacker': self.name,
                'target': target_name,
                'damage_dealt': self.attack,
                'combat_resolved': True
                }
        return attack_result

    def get_card_info(self) -> Dict[str, Any]:
        base_info = super().get_card_info()
        base_info.update({
            'attack': self.attack,
            'health': self.health
            })
        return base_info
