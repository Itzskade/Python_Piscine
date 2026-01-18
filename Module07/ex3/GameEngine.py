from typing import Any, Dict
from ex3.CardFactory import CardFactory as Factory
from ex3.GameStrategy import GameStrategy as Strategy


class GameEngine():
    """Engine that runs turns using a factory and a strategy."""
    def __init__(self):
        """Initialize the engine without factory or strategy."""
        self.factory: Factory | None = None
        self.strategy: Strategy | None = None

    def configure_engine(self, factory: Factory, strategy: Strategy) -> None:
        """Load the factory and strategy into the engine."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        """Simulate a turn using the configured factory and strategy."""
        if self.factory is None or self.strategy is None:
            raise RuntimeError(
                "Engine not configured ""with factory and strategy"
                )
        hand = self.factory.create_themed_deck(5)["deck"]
        battlefield = self.factory.create_themed_deck(3)["deck"]

        result = self.strategy.execute_turn(hand, battlefield)
        return result

    def get_engine_status(self) -> Dict[str, Any]:
        """Return whether the engine has a factory and strategy loaded."""
        return {
            'factory_loaded': self.factory is not None,
            'strategy_loaded': self.strategy is not None
        }
