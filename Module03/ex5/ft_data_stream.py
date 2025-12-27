#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:30:30 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/27 13:38:13 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from typing import Generator

character_db = {
    'alice': 5,
    'bob': 12,
    'charlie': 7,
    'dave': 15,
    'eve': 3,
    'frank': 8,
    'grace': 9,
    'heidi': 6,
    'ivan': 2,
    'judy': 1,
    'karl': 1,
    'laura': 1,
    'mallory': 2,
    'nancy': 4,
    'oscar': 1,
    'peggy': 6,
    'quentin': 2,
    'roger': 5,
    'skade': 1,
    'trent': 5,
    'ursula': 4,
    'victor': 3,
    'wendy': 5,
    'xavier': 1,
    'yvonne': 6,
    'zack': 4
}

def level_up(player: str) -> Generator[str, None, None]:
    if character_db[player] < 20:
        character_db[player] += 1
        yield f"Player {player} (level {character_db[player]}) leveled up"

def monster_defeat(player: str)-> Generator[str, None, None]:
    level = character_db[player]
    yield f"Player {player} (level {level}) killed monster"

def found_treasure(player: str) -> Generator[str, None, None]:
    level = character_db[player]
    yield f"Player {player} (level {level}) found treasure"


def event_generator(total_events) -> Generator[tuple[str, str], None, None]:
    players = list(character_db.keys())

    for count in range (total_events):
        player = players[count % len(players)]        
        mod = count % 7
        if  mod in (0, 1, 2, 3):
            event_func = monster_defeat
        elif mod in (4, 5):
            event_func = level_up
        else:
            event_func = found_treasure
        for msg in event_func(player):
            yield (f"Event {count+1}: {msg}", player)


def fibonacci(size: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    for _ in range(size):
        yield a
        tmp = a
        a = b
        b = tmp + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(size: int) -> None:
    n = 2
    i = 0
    while i < size:
        if is_prime(n):
            yield n
            i += 1
        n += 1


def game_events_processor() -> None:
    total_events = 1000
    print(f"Processing {total_events} game events...\n")

    start = time.perf_counter()

    high_level_count = 0
    treasure_count = 0
    level_up_count = 0

    for msg, player in event_generator(total_events):
        print(msg)
        if character_db[player] >= 10:
            high_level_count += 1 
        if 'found treasure' in msg:
            treasure_count += 1
        if 'leveled up' in msg:
            level_up_count += 1
    
    end = time.perf_counter()
    elapsed = end - start

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}\n")
    
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {elapsed:.3f} seconds")


def ft_data_stream():
    print("=== Game Data Stream Processor ===\n")
    game_events_processor()

    print("\n=== Generator Demostration ===")
    size = 10
    print(f"Fibonacci sequence: (first {size}):", end=" ")
    first = True
    for x in fibonacci(size):
        if not first:
            print(", ", end="")
        print(x, end="")
        first = False
    print()

    size  = 5
    first = True
    print(f"Prime numbers (first {size}):", end=" ")
    for p in prime_generator(5):
        if not first:
            print(", ", end="")
        print(p, end="")
        first = False

if __name__ == '__main__':
    ft_data_stream()
