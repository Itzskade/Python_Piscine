from typing import Ant, Dict
from ex0.Card import card
from ex2.Combatable import Combatable
from ex3.CreatureCard import CreatureCard as Creature
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def play(self, game_state: Dict[]) -> Dict[]:

    def attack(self, target: Creature) -> Dict[]:
    
    def defend(self, incoming_damage: int) -> Dict[str, Any]:

    def get_combat_stats(self) -> Dict[str, Any]:

    def calculate_ratings(self) -> int:

    def get_tournament_stats(self) -> Dict[]:

    def calculate_rating(self) -> int:

    def update_wins(self, wins: int) -> None:

    def update_losses(self, losses: int) -> None:

    def get_rank_info(self) -> Dict[str, int]





