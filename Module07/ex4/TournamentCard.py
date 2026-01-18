from typing import Any, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
import random


class TournamentCard(Card, Combatable, Rankable):
    """Tournament card with combat and ranking capabilities."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        attack_power: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power or random.randint(2, 10)
        self.max_health = max(1, health)
        self.health = self.max_health
        self.wins = 0
        self.losses = 0
        self.rating = 1000

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Play the card if enough mana is available."""
        mana = game_state.get("available_mana", 0)
        if mana >= self.cost:
            return {
                "card_used": self.name,
                "mana_used": self.cost,
                "effect": "Tournament card enters the battlefield"
            }
        return {
            "card_used": self.name,
            "mana_used": 0,
            "effect": "Not enough mana"
        }

    @property
    def health(self) -> int:
        """Return health value."""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Set health, must be positive integer."""
        if value < 0:
            self._health = 0
        elif value > self.max_health:
            self._health = self.max_health
        else:
            self._health = value

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

    def attack(self, target: Creature) -> Dict[str, Any]:
        """Return attack result."""
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Apply damage, block part of it, and report survival."""
        damage_blocked = random.randint(0, 5)
        damage_taken = max(0, incoming_damage - damage_blocked)
        self.health = max(0, self.health - damage_taken)

        return {
            "name": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        """Return combat statistics."""
        return {
            "attack_power": self.attack_power,
            "health": self.health
        }

    def update_wins(self, wins: int) -> None:
        """Increase wins count."""
        self.wins += wins
        self.rating += 20

    def update_losses(self, losses: int) -> None:
        """Increase losses count."""
        self.losses += losses
        self.rating -= 15

    def calculate_rating(self) -> int:
        """Calculate and return rating."""
        return self.rating

    def get_rank_info(self) -> Dict[str, int]:
        """Return ranking information."""
        return {
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses
        }
