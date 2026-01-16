from .Card import Card
from typing import Any, Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be > 0")
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        played = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': "Creature summoned to battlefield"
                }
        return played

    def attack_target(self, target) -> Dict[str, Any]:
        attack_result = {
                'attacker': self.name,
                'target': target.name if isinstance(
                    target, CreatureCard) else str(target),
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
