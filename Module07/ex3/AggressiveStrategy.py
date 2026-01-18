from __future__ import annotations
from typing import Any, List, Dict
from ex0.Card import Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    DEFAULT_MANA = 10

    def execute_turn(self, hand: List[Card], battlefield: List[
                        Card]) -> Dict[str, Any]:
        available_mana = self.DEFAULT_MANA

        sorted_hand = self.sort_hand_by_cost(hand)
        cards_played, mana_used = self.play_cards(sorted_hand, available_mana)
        damage_dealt = self.calculate_damage(cards_played)
        if battlefield:
            prioritized = self.prioritize_targets(battlefield)
            target_name = prioritized[0].name
        else:
            target_name = "Enemy Player"
        return self.build_turn_result(
            cards_played, mana_used, target_name, damage_dealt)

    def sort_hand_by_cost(self, hand: List[Card]) -> List[Card]:
        return sorted(hand, key=lambda card: card.cost)

    def play_cards(self, sorted_hand: List[Card], available_mana: int):
        cards_played = []
        mana_used = 0

        for card in sorted_hand:
            if mana_used + card.cost <= available_mana:
                cards_played.append(card)
                mana_used += card.cost
        return cards_played, mana_used

    def calculate_damage(self, cards_played: List[Card]) -> int:
        damage_dealt = 0

        for card in cards_played:
            if hasattr(card, "attack"):
                damage_dealt += card.attack
            elif getattr(card, "effect_type", "") == "damage":
                damage_dealt += 3
        return damage_dealt

    def build_turn_result(
        self, cards_played: List[Card], mana_used: int,
        target_name: str, damage_dealt: int
            ) -> Dict[str, Any]:

        card_names = [card.name for card in cards_played]
        return {
            "cards_played": card_names,
            "mana_used": mana_used,
            "targets_attacked": [target_name],
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: List[Card]) -> List[Card]:
        return sorted(available_targets, key=lambda card: card.health)
