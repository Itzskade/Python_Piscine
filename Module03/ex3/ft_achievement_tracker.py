#!/usr/bin/env python3

data = {
        'alice': [
            'first_blood',
            'pixel_perfect',
            'speed_runner',
            'first_blood',
            'first_blood'
            ],
        'bob': [
            'level_master',
            'boss_hunter',
            'treasure_seeker',
            'level_master',
            'first_blood'
            ],
        'charlie': [
            'treasure_seeker',
            'boss_hunter',
            'combo_king',
            'first_blood',
            'boss_hunter',
            'first_blood',
            'boss_hunter',
            'first_blood'
            ],
        'diana': [
            'first_blood',
            'combo_king',
            'level_master',
            'treasure_seeker',
            'speed_runner',
            'combo_king',
            'combo_king',
            'level_master'
            ],
        'eve': [
            'level_master',
            'treasure_seeker',
            'first_blood',
            'treasure_seeker',
            'first_blood',
            'treasure_seeker'
            ],
        'frank': [
            'explorer',
            'boss_hunter',
            'first_blood',
            'explorer',
            'first_blood',
            'boss_hunter'
            ]
}


def build_player_sets(data: dict) -> dict:
    player_achievements = dict()
    for name in data:
        player_achievements[name] = set(data[name])
    return player_achievements


def compute_achievements(player_achievements: dict) -> set:
    achievements = set()
    for name in player_achievements:
        achievements = achievements.union(player_achievements[name])
    return achievements


def compute_common_achievements(player_achievements: dict) -> set:
    names = list(player_achievements)
    common = set(player_achievements[names[0]])
    for name in names:
        common = common.intersection(player_achievements[name])
    return common


def compute_rare_achievements(player_achievements: dict,
                              achievements: set) -> set:
    all_seen = set()
    repeated = set()
    for ach in player_achievements.values():
        repeated = repeated.union(all_seen.intersection(ach))
        all_seen = all_seen.union(ach)
    return achievements.difference(repeated)


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    player_achievements = build_player_sets(data)
    for name in player_achievements:
        print(f"Player {name} achievements: {player_achievements[name]}")
    print()

    print("=== Achievement Analytics ===")
    achievements = compute_achievements(player_achievements)
    print(f"All unique achievements: {achievements}")
    print(f"Total unique achievements: {len(achievements)}\n")

    common = compute_common_achievements(player_achievements)
    print(f"Common to all players: {common}")

    rare = compute_rare_achievements(player_achievements, achievements)
    print(f"Rare achievements (1 player): {rare}\n")

    alice = player_achievements['alice']
    bob = player_achievements['bob']
    charlie = player_achievements['charlie']
    diana = player_achievements['diana']
    print(f"Charlie vs Diana common: {charlie.intersection(diana)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
