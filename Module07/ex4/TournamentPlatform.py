from typing import Any, List, Dict
import random
from ex4.TournamentCard import TournamentCard as Tournament


class TournamentPlatform:
    """Platform that manages tournament cards and matches."""
    def __init__(self) -> None:
        """Initialize an empty tournament platform."""
        self.cards: Dict[str, Tournament] = {}
        self.matches_played = 0

    def register_card(self, card: Tournament) -> str:
        """Register a card and return its generated ID."""
        card_id = card.name.lower() + '_001'
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        """Simulate a match between two registered cards."""
        player1 = self.cards.get(card1_id)
        player2 = self.cards.get(card2_id)
        player1.health = player1.max_health
        player2.health = player2.max_health

        if not player1 or not player2:
            return {"error": "One or both card IDs not found"}

        while player1.health > 0 and player2.health > 0:
            result = random.randint(0, 1)
            if result == 1:
                player1.defend(player2.attack(player1)['damage'])
            else:
                player2.defend(player1.attack(player2)['damage'])
        if player2.health == 0:
            winner = player1
            loser = player2
            player1.update_wins(1)
            player2.update_losses(1)
        else:
            winner = player2
            loser = player1
            player2.update_wins(1)
            player1.update_losses(1)

        self.matches_played += 1
        return {
            'player1': player1.name,
            'player2': player2.name,
            'winner': winner.name,
            'loser': loser.name,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> List[str]:
        """Return a sorted leaderboard by rating."""
        leaderboard = sorted(
            self.cards.values(),
            key=lambda c: c.rating
        )
        result = []
        for index, card in enumerate(leaderboard, start=1):
            line = (f"{index}. {card.name}"
                    f"- Rating: {card.rating} ({card.wins}-{card.losses})")
            result.append(line)
        return result

    def generate_tournament_report(self) -> Dict[str, Any]:
        """Return basic statistics about the tournament platform."""
        total_rating = sum(c.rating for c in self.cards.values())
        avg_rating = total_rating / len(self.cards) if self.cards else 0
        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
