from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()

    dragon = TournamentCard('Fire Dragon', 5, 'Legendary', 5, 10)
    wizard = TournamentCard('Ice Wizard', 5, 'Legendary', 7, 8)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    interfaces = [base.__name__ for base in TournamentCard.__bases__]
    for card, card_id in [(dragon, dragon_id), (wizard, wizard_id)]:
        print(f"{card.name} (ID: {card_id})")
        print("- Interfaces:", f"[{", ".join(interfaces)}]")
        print("- Rating: ", card.rating)
        print(f"- Record: {card.wins}-{card.losses}\n")

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(match_result)

    print("\nTounament Leaderboard:")
    for line in platform.get_leaderboard():
        print(line)

    print("\nPlatform Report\n", platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == '__main__':
    main()

