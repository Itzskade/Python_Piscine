from typing import Any, Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
import random


class EliteCard(Card, Combatable, Magical):
    """
    EliteCard combines combat and magical
    abilities with robust validation of stats.
    """
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int, mana: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power or random.randint(2, 4)
        self.max_health = max(0, health)
        self.max_mana = max(0, mana)
        self.health = self.max_health
        self.mana = self.max_mana
        self.spell_costs = {
                "Fireball": 4,
                "Ice Lance": 3,
                "Arcane Blast": 5
                }

    @property
    def attack_power(self) -> int:
        """Get attack power."""
        return self._attack_power

    @attack_power.setter
    def attack_power(self, value: int) -> None:
        """Ensure attack power is positive."""
        if value <= 0:
            raise ValueError("Attack power must be greater than 0")
        self._attack_power = value

    @property
    def health(self) -> int:
        """Get current health"""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Ensure health is non-negative"""
        if value < 0:
            self._health = 0
        elif value > self.max_health:
            self._health = self.max_health
        else:
            self._health = value

    @property
    def mana(self) -> int:
        """Get current mana"""
        return self._mana

    @mana.setter
    def mana(self, value: int) -> None:
        """Ensure mana is non-negative"""
        if value < 0:
            self._mana = 0
        elif value > self.max_mana:
            self._mana = self.max_mana
        else:
            self._mana = value

    def attack(self, target) -> Dict[str, Any]:
        attack = {
                'attacker': self.name,
                'target': str(target),
                'damage': self.attack_power,
                'combat_type': 'melee'
                }
        return attack

    def defend(self, incoming_damage) -> Dict[str, Any]:
        damage_blocked = random.randint(0, 2)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken
        defend = {
                'defender': self.name,
                'damage_taken': damage_taken,
                'damage_blocked': damage_blocked,
                'still_alive': self.health > 0
                }
        return defend

    def get_combat_stats(self) -> Dict[str, Any]:
        combat_stats = {
                'attack_power': self.attack_power,
                'health': self.health
                }
        return combat_stats

    def cast_spell(self, spell_name: str,
                   targets: List[str]) -> Dict[str, Any]:
        if spell_name not in self.spell_costs:
            raise ValueError(f"Spell '{spell_name}' "
                             "not available for this card")

        cost = self.spell_costs[spell_name]
        if self.mana >= cost:
            self.mana -= cost
            spell = {
                    'caster': self.name,
                    'spell': spell_name,
                    'targets': targets,
                    'mana_used': cost
                    }
        else:
            spell = {
                    'caster': self.name,
                    'spell': spell_name,
                    'targets': targets,
                    'mana_used': 0,
                    'error': "Insufficient mana for this card"
                    }
        return spell

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        channeled = {
                'channeled': amount,
                'total_mana': self.mana
                }
        return channeled

    def get_magic_stats(self) -> Dict[str, Any]:
        magic_stats = {
                'mana': self.mana,
                'spells': list(self.spell_costs.keys())
                }
        return magic_stats

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        available_mana = game_state.get('available_mana', 0)
        if self.is_playable(available_mana):
            played = {
                    'card_used': self.name,
                    'mana_used': self.cost,
                    'effect': "Elite card enters the battlefield"
                    }
        else:
            played = {
                    'card_used': self.name,
                    'mana_used': 0,
                    'effect': "Not enough mana to play"
                    }
        return played
