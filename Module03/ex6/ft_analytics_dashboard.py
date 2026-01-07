#!/usr/bin/env python3


def data_base():
    """
    Creates data_base based on
    data_generator given on the exercise
    """
    data = {
        'players': {
            'alice': {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5
            },
            'bob': {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2
            },
            'charlie': {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7
            },
            'diana': {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4
            },
            'eve': {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7
            },
            'frank': {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1
            }
        },
        'sessions': [
            {
                'player': 'bob',
                'duration_minutes': 94,
                'score': 1831,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'bob',
                'duration_minutes': 32,
                'score': 1478,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 17,
                'score': 1570,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 98,
                'score': 1981,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 15,
                'score': 2361, 'mode':
                'competitive',
                'completed': False
            },
            {
                'player': 'eve',
                'duration_minutes': 29,
                'score': 2985,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 34,
                'score': 1285,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'alice',
                'duration_minutes': 53,
                'score': 1238,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 1555,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'frank',
                'duration_minutes': 92,
                'score': 2754, 'mode':
                'casual',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 98,
                'score': 1102,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'diana',
                'duration_minutes': 39,
                'score': 2721,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 46,
                'score': 329,
                'mode': 'casual',
                'completed': True
                },
            {
                'player': 'charlie',
                'duration_minutes': 56,
                'score': 1196,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 117,
                'score': 1388,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'diana',
                'duration_minutes': 118,
                'score': 2733,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'charlie',
                'duration_minutes': 22,
                'score': 1110,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'frank',
                'duration_minutes': 79,
                'score': 1854,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'charlie',
                'duration_minutes': 33,
                'score': 666,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 101,
                'score': 292,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 25,
                'score': 2887,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 53,
                'score': 2540,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'eve',
                'duration_minutes': 115,
                'score': 147,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 118,
                'score': 2299,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 42,
                'score': 1880,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 97,
                'score': 1178,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 18,
                'score': 2661,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 761,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 46,
                'score': 2101,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'charlie',
                'duration_minutes': 117,
                'score': 1359,
                'mode': 'casual',
                'completed': True
            }
        ],
        'game_modes': [
            'casual',
            'competitive',
            'ranked'
        ],
        'achievements': [
            'first_blood',
            'level_master',
            'speed_runner',
            'treasure_seeker',
            'boss_hunter',
            'pixel_perfect',
            'combo_king',
            'explorer'
        ]
    }
    return data


def list_comprehension(data: dict) -> None:
    """Show list comprehension examples."""
    print("=== List Comprehension Examples ===")
    high_scores = [
        player for player, details in data['players'].items()
        if details['total_score'] > 2000
    ]
    print("High scores (>2000):", high_scores)
    scores_doubled = [
        details['total_score'] * 2
        for details in data['players'].values()]
    print("Scores doubled:", scores_doubled)
    active_players = [
        player for player, details in data['players'].items()
        if details['sessions_played'] > 10]
    print("Active players:", sorted(active_players))
    print()


def dict_comprehension(data: dict) -> None:
    """Show dict comprehension examples."""
    print("=== Dict Comprehension Examples ===")
    player_scores = {
        player: details['total_score']
        for player, details in data['players'].items()}
    print("Players scores:", player_scores)
    categories = {
        'low': len([player for player, details in data['players'].items()
                    if details['total_score'] <= 1000]),
        'medium': len([player for player, details in data['players'].items()
                       if 1000 < details['total_score'] <= 5000]),
        'high': len([player for player, details in data['players'].items()
                     if details['total_score'] > 5000])
    }
    print("Score categories:", categories)
    achievements_count = {
        player: details['achievements_count']
        for player, details in data['players'].items()
    }
    print("Achievements counts:", achievements_count)
    print()


def set_comprehension(data: dict) -> None:
    """Show set comprehension examples."""
    print("=== Set Comprehension Examples ===")
    unique_players = {player for player in data['players'].keys()}
    print("Unique players:", unique_players)
    unique_game_modes = {session['mode'] for session in data['sessions']}
    print("Unique game modes:", unique_game_modes)
    unique_achievements = {achievement for achievement in data['achievements']}
    print("Unique achievements:", unique_achievements)
    print()


def combined_analysis(data: dict) -> None:
    """Show summary stats and top performer."""
    print("=== Combined Analysis ===")
    print("Total players:", len(data['players']))
    print("Total unique achievements:", len(data['achievements']))
    average_score = sum(details['total_score'] for details in
                        data['players'].values()) / len(data['players'])
    print(f"Average score: {average_score:.1f}")

    top_player = None
    for name, details in data['players'].items():
        if top_player is None or details[
                'total_score'] > top_player['total_score']:
            top_name = name
            top_player = details

    top_score = top_player['total_score']
    top_achievements = top_player['achievements_count']
    print(f"Top performer: {top_name} ({top_score} points, "
          f"{top_achievements} achievements)")


def ft_analytics_dashboard() -> None:
    """Run full analytics dashboard."""
    print("=== Game Analytics Dashboard ===\n")
    data = data_base()
    list_comprehension(data)
    dict_comprehension(data)
    set_comprehension(data)
    combined_analysis(data)


if __name__ == '__main__':
    ft_analytics_dashboard()
