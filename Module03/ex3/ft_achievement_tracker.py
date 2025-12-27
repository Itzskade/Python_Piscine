#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:30:03 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:30:04 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_achievement_tracker():
    print("=== Achievement Tracker System ===\n")

    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")
    
    repeats = set().union(alice.intersection(bob), alice.intersection(charlie), bob.intersection(charlie))
    rare = all_achievements.difference(repeats)
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()

