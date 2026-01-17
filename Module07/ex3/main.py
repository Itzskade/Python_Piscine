from ex3.FantasyCardFactory import FantasyCardFactory as Factory
from ex3.AggressiveStrategy import AggressiveStrategy as Strategy
from ex3.GameEngine import GameEngine


def format_card_list(cards):
    """Transform cards in format: Name (cost)."""
    return [f"{card.name} ({card.cost})" for card in cards]


def main():
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = Factory()
    strategy = Strategy()
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())

    generator = factory.generator

    available_types = {
        'creatures': [card['name'] for card in generator.get_all_creatures()],
        'spells': [card['name'] for card in generator.get_all_spells()],
        'artifacts': [card['name'] for card in generator.get_all_artifacts()]
    }

    print("Available types:", available_types)

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")
    hand = factory.create_themed_deck(3)['deck']
    print("Hand:", format_card_list(hand))

    print("\nTurn Execution:")
    print("Strategy:", strategy.get_strategy_name())
    result = strategy.execute_turn(hand, [])

    print("Actions:", result)

    report = {
        'turns_simulated': 1,
        'strategy_used': strategy.get_strategy_name(),
        'total_damage': result['damage_dealt'],
        'cards_created': len(hand)
    }

    print("\nGame Report:\n", report)
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == '__main__':
    main()
