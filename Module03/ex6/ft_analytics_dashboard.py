#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_analytics_dashboard.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:32:31 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:32:56 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

players = [
    {
        'name': 'alice',
        'score': 2300,
        'region': 'north',
        'active': True,
        'achievements': ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon', 'explorer']
    },
    {
        'name': 'bob',
        'score': 1800,
        'region': 'east',
        'active': True,
        'achievements': ['first_kill', 'level_10', 'speed_demon']
    },
    {
        'name': 'charlie',
        'score': 2150,
        'region': 'central',
        'active': True,
        'achievements': ['first_kill', 'strategist', 'level_10', 'treasure_hunter', 'boss_slayer', 'collector', 'explorer']
    },
    {
        'name': 'diana',
        'score': 2050,
        'region': 'north',
        'active': False,
        'achievements': ['treasure_hunter', 'explorer', 'collector']
    }
]


def list_comprehension():
    print("=== List Comprehension Examples ===")
    high_scores = [player['name'] for player in players if player['score'] > 2000]
    print("High scores (>2000):", high_scores)
    scores_doubled = [player['score'] * 2 for player in players]
    print("Scores doubled:", scores_doubled)
    active_players = [player['name'] for player in players if player['active'] == True]
    print("Active players:", sorted(active_players))
    print()


def dict_comprehension():
    print("=== Dict Comprehension Examples ===")
    player_scores = {player['name']: player['score'] for player in players}
    print("Players scores:", player_scores)
    categories = ['low' if player['score'] <= 1000 else 'medium' if player['score'] <= 2000 else 'high' for player in players]
    scores_categories = {categorie: sum(1 for cat in categories if cat == categorie) for categorie in {'high', 'medium', 'low'}}
    print("Score categories:", scores_categories) 
    achievements_count = {player['name']: len(player['achievements']) for player in players}
    print("Achievements counts:", achievements_count)
    print()


def set_comprehension():
    print("=== Set Comprehension Examples ===")
    unique_players = {player['name'] for player in players}
    print("Unique players:", unique_players)
    unique_achievements = {achievement for player in players for achievement in player['achievements']}
    print("Unique achievements:", unique_achievements)
    active_regions = {player['region'] for player in players if player['active'] == True}
    print("Active regions:", active_regions)
    print()


def combined_analysis():
    print ("=== Combined Analysis ===")
    print("Total players:", len(players))
    total_achievements = {achievement for player in players for achievement in player['achievements']}
    print("Total unique achivements:", len(total_achievements))
    average_score = sum(player['score'] for player in players) / len(players)
    print("Average score:", average_score)

    top_player = players[0]
    for player in players:
        if player['score'] > top_player['score']:
            top_player = player

    top_name = top_player['name']
    top_score = top_player['score']
    top_achievements = len(top_player['achievements'])
    print(f"Top performer: {top_name} ({top_score} points, {top_achievements} achievements)")


def ft_analytics_dashboard():
    print("=== Game Analytics Dashboard ===\n")
    list_comprehension()
    dict_comprehension()
    set_comprehension()
    combined_analysis()


if __name__ == '__main__':
ft_analytics_dashboard()

