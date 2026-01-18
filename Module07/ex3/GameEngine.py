from typing import Any, Dict
from ex3.CardFactory import CardFactory as Factory
from ex3.GameStrategy import GameStrategy as Strategy


class GameEngine():
    def __init__(self):
        self.factory: Factory | None = None
        self.strategy: Strategy | None = None

    def configure_engine(self, factory: Factory, strategy: Strategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise RuntimeError(
                "Engine not configured ""with factory and strategy"
                )
        hand = self.factory.create_themed_deck(5)["deck"]
        battlefield = self.factory.create_themed_deck(3)["deck"]

        result = self.strategy.execute_turn(hand, battlefield)
        return result

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            'factory_loaded': self.factory is not None,
            'strategy_loaded': self.strategy is not None
        }
