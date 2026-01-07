import time


def all_events() -> dict:
    """
    Creates events data_base based on
    data_generator given on the exercise.
    """
    events = [
        {
            'id': 1,
            'player': 'frank',
            'event_type': 'login',
            'timestamp': '2024-01-01T23:17',
            'data': {
                'level': 16,
                'score_delta': 128,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 2,
            'player': 'frank',
            'event_type': 'login',
            'timestamp': '2024-01-22T23:57',
            'data': {
                'level': 35,
                'score_delta': -11,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 3,
            'player': 'diana',
            'event_type': 'login',
            'timestamp': '2024-01-01T02:13',
            'data': {
                'level': 15,
                'score_delta': 417,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 4,
            'player': 'alice',
            'event_type': 'level_up',
            'timestamp': '2024-01-07T22:41',
            'data': {
                'level': 45,
                'score_delta': 458,
                'zone': 'pixel_zone_4'
            }
        },
        {
            'id': 5,
            'player': 'bob',
            'event_type': 'death',
            'timestamp': '2024-01-19T08:51',
            'data': {
                'level': 1,
                'score_delta': 63,
                'zone': 'pixel_zone_4'
            }
        },
        {
            'id': 6,
            'player': 'charlie',
            'event_type': 'kill',
            'timestamp': '2024-01-05T06:48',
            'data': {
                'level': 22,
                'score_delta': 4,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 7,
            'player': 'diana',
            'event_type': 'login',
            'timestamp': '2024-01-12T11:38',
            'data': {
                'level': 17,
                'score_delta': -56,
                'zone': 'pixel_zone_4'
            }
        },
        {
            'id': 8,
            'player': 'eve',
            'event_type': 'login',
            'timestamp': '2024-01-30T12:05',
            'data': {
                'level': 36,
                'score_delta': 200,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 9,
            'player': 'charlie',
            'event_type': 'level_up',
            'timestamp': '2024-01-07T22:04',
            'data': {
                'level': 3,
                'score_delta': 133,
                'zone': 'pixel_zone_3'
            }
        },
        {
            'id': 10,
            'player': 'alice',
            'event_type': 'logout',
            'timestamp': '2024-01-28T03:24',
            'data': {
                'level': 18,
                'score_delta': 364,
                'zone': 'pixel_zone_3'
            }
        },
        {
            'id': 11,
            'player': 'bob',
            'event_type': 'kill',
            'timestamp': '2024-01-12T06:42',
            'data': {
                'level': 18,
                'score_delta': -27,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 12,
            'player': 'frank',
            'event_type': 'logout',
            'timestamp': '2024-01-18T23:15',
            'data': {
                'level': 11,
                'score_delta': 373,
                'zone': 'pixel_zone_4'
            }
        },
        {
            'id': 13,
            'player': 'charlie',
            'event_type': 'item_found',
            'timestamp': '2024-01-23T17:14',
            'data': {
                'level': 44,
                'score_delta': 232,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 14,
            'player': 'bob',
            'event_type': 'login',
            'timestamp': '2024-01-26T10:25',
            'data': {
                'level': 18,
                'score_delta': -33,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 15,
            'player': 'eve',
            'event_type': 'item_found',
            'timestamp': '2024-01-11T06:41',
            'data': {
                'level': 32,
                'score_delta': 305,
                'zone': 'pixel_zone_4'
            }
        },
        {
            'id': 16,
            'player': 'bob',
            'event_type': 'kill',
            'timestamp': '2024-01-05T07:47',
            'data': {
                'level': 36,
                'score_delta': 451,
                'zone': 'pixel_zone_3'
            }
        },
        {
            'id': 17,
            'player': 'frank',
            'event_type': 'level_up',
            'timestamp': '2024-01-14T18:25',
            'data': {
                'level': 24,
                'score_delta': 124,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 18,
            'player': 'eve',
            'event_type': 'death',
            'timestamp': '2024-01-03T01:55',
            'data': {
                'level': 8,
                'score_delta': 56,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 19,
            'player': 'frank',
            'event_type': 'death',
            'timestamp': '2024-01-20T02:24',
            'data': {
                'level': 25,
                'score_delta': 379,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 20,
            'player': 'charlie',
            'event_type': 'level_up',
            'timestamp': '2024-01-28T00:43',
            'data': {
                'level': 47,
                'score_delta': 17,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 21,
            'player': 'charlie',
            'event_type': 'item_found',
            'timestamp': '2024-01-11T03:18',
            'data': {
                'level': 28,
                'score_delta': 61,
                'zone': 'pixel_zone_4'
            }
        },
        {
            'id': 22,
            'player': 'alice',
            'event_type': 'item_found',
            'timestamp': '2024-01-29T23:16',
            'data': {
                'level': 33,
                'score_delta': 82,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 23,
            'player': 'alice',
            'event_type': 'item_found',
            'timestamp': '2024-01-10T20:32',
            'data': {
                'level': 39,
                'score_delta': 103,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 24,
            'player': 'charlie',
            'event_type': 'logout',
            'timestamp': '2024-01-18T16:58',
            'data': {
                'level': 1,
                'score_delta': 231,
                'zone': 'pixel_zone_4'
            }
        },
        {
            'id': 25,
            'player': 'alice',
            'event_type': 'login',
            'timestamp': '2024-01-30T11:56',
            'data': {
                'level': 20,
                'score_delta': 145,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 26,
            'player': 'bob',
            'event_type': 'level_up',
            'timestamp': '2024-01-03T02:46',
            'data': {
                'level': 32,
                'score_delta': -30,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 27,
            'player': 'bob',
            'event_type': 'logout',
            'timestamp': '2024-01-22T15:35',
            'data': {
                'level': 11,
                'score_delta': 171,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 28,
            'player': 'eve',
            'event_type': 'death',
            'timestamp': '2024-01-07T17:48',
            'data': {
                'level': 47,
                'score_delta': 105,
                'zone': 'pixel_zone_3'
            }
        },
        {
            'id': 29,
            'player': 'diana',
            'event_type': 'item_found',
            'timestamp': '2024-01-21T11:28',
            'data': {
                'level': 34,
                'score_delta': 362,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 30,
            'player': 'bob',
            'event_type': 'logout',
            'timestamp': '2024-01-03T10:01',
            'data': {
                'level': 38,
                'score_delta': 467,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 31,
            'player': 'eve',
            'event_type': 'logout',
            'timestamp': '2024-01-01T02:45',
            'data': {
                'level': 41,
                'score_delta': -40,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 32,
            'player': 'alice',
            'event_type': 'login',
            'timestamp': '2024-01-28T10:04',
            'data': {
                'level': 33,
                'score_delta': 143,
                'zone': 'pixel_zone_3'
            }
        },
        {
            'id': 33,
            'player': 'frank',
            'event_type': 'death',
            'timestamp': '2024-01-07T17:08',
            'data': {
                'level': 47,
                'score_delta': 484,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 34,
            'player': 'diana',
            'event_type': 'logout',
            'timestamp': '2024-01-26T15:51',
            'data': {
                'level': 27,
                'score_delta': 94,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 35,
            'player': 'alice',
            'event_type': 'item_found',
            'timestamp': '2024-01-14T11:27',
            'data': {
                'level': 27,
                'score_delta': 378,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 36,
            'player': 'frank',
            'event_type': 'item_found',
            'timestamp': '2024-01-21T03:03',
            'data': {
                'level': 26,
                'score_delta': 247,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 37,
            'player': 'bob',
            'event_type': 'logout',
            'timestamp': '2024-01-07T17:28',
            'data': {
                'level': 9,
                'score_delta': 332,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 38,
            'player': 'charlie',
            'event_type': 'death',
            'timestamp': '2024-01-08T02:28',
            'data': {
                'level': 36,
                'score_delta': 0,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 39,
            'player': 'frank',
            'event_type': 'level_up',
            'timestamp': '2024-01-27T00:05',
            'data': {
                'level': 49,
                'score_delta': 142,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 40,
            'player': 'diana',
            'event_type': 'death',
            'timestamp': '2024-01-16T06:55',
            'data': {
                'level': 26,
                'score_delta': -40,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 41,
            'player': 'diana',
            'event_type': 'login',
            'timestamp': '2024-01-13T08:59',
            'data': {
                'level': 30,
                'score_delta': 192,
                'zone': 'pixel_zone_4'
            }
        },
        {
            'id': 42,
            'player': 'frank',
            'event_type': 'item_found',
            'timestamp': '2024-01-26T17:42',
            'data': {
                'level': 46,
                'score_delta': 398,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 43,
            'player': 'bob',
            'event_type': 'kill',
            'timestamp': '2024-01-07T01:37',
            'data': {
                'level': 48,
                'score_delta': 455,
                'zone': 'pixel_zone_1'
            }
        },
        {
            'id': 44,
            'player': 'frank',
            'event_type': 'kill',
            'timestamp': '2024-01-02T01:37',
            'data': {
                'level': 31,
                'score_delta': 414,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 45,
            'player': 'bob',
            'event_type': 'login',
            'timestamp': '2024-01-17T02:54',
            'data': {
                'level': 12,
                'score_delta': -30,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 46,
            'player': 'alice',
            'event_type': 'item_found',
            'timestamp': '2024-01-28T07:25',
            'data': {
                'level': 8,
                'score_delta': 483,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 47,
            'player': 'eve',
            'event_type': 'level_up',
            'timestamp': '2024-01-02T19:05',
            'data': {
                'level': 27,
                'score_delta': 497,
                'zone': 'pixel_zone_5'
            }
        },
        {
            'id': 48,
            'player': 'eve',
            'event_type': 'kill',
            'timestamp': '2024-01-30T08:13',
            'data': {
                'level': 43,
                'score_delta': 221,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 49,
            'player': 'charlie',
            'event_type': 'death',
            'timestamp': '2024-01-05T21:41',
            'data': {
                'level': 20,
                'score_delta': 368,
                'zone': 'pixel_zone_3'
            }
        },
        {
            'id': 50,
            'player': 'alice',
            'event_type': 'login',
            'timestamp': '2024-01-15T19:36',
            'data': {
                'level': 7,
                'score_delta': -25,
                'zone': 'pixel_zone_5'
            }
        }
    ]
    return events


def login_event(player: str, timestamp: str):
    """Yields a message indicating player has logged in."""
    yield f"Player {player} logged in at {timestamp}"


def logout_event(player: str, timestamp: str):
    """Yields a message indicating player has logged out."""
    yield f"Player {player} logged out at {timestamp}"


def death_event(player: str, level: int, timestamp: str):
    """Yields a message indicating player died at a specific level."""
    yield f"Player {player} died on level {level} at {timestamp}"


def level_up_event(player: str, level: int, timestamp: str):
    """Yields a message indicating player leveled up."""
    yield f"Player {player} leveled up to level {level} at {timestamp}"


def kill_event(player: str, level: int, timestamp: str):
    """Yields a message indicating player
    defeated an enemy at a specific level."""
    yield f"Player {player} defeated an enemy on level {level} at {timestamp}"


def item_found_event(player: str, timestamp: str):
    """Yields a message indicating player found an item."""
    yield f"Player {player} found an item at {timestamp}"


def event_generator(events: dict):
    """Iterates over game events and
    yields formatted messages with metadata."""
    count = 0
    for event_data in events:
        player = event_data['player']
        event_type = event_data['event_type']
        timestamp = event_data['timestamp']

        if 'level' in event_data['data']:
            level = event_data['data']['level']
        else:
            level = 1

        if event_type == 'login':
            event_func = login_event
        elif event_type == 'logout':
            event_func = logout_event
        elif event_type == 'death':
            event_func = death_event
        elif event_type == 'level_up':
            event_func = level_up_event
        elif event_type == 'kill':
            event_func = kill_event
        elif event_type == 'item_found':
            event_func = item_found_event
        else:
            continue

        count += 1
        if event_type in ['login', 'logout', 'item_found']:
            for msg in event_func(player, timestamp):
                yield (f"Event {count}: {msg}", player, event_type, timestamp)
        else:
            for msg in event_func(player, level, timestamp):
                yield (f"Event {count}: {msg}", player, event_type, timestamp)


def game_events_processor(events: dict) -> None:
    """
    Processes game events, prints messages,
    displays event counts and analytics.
    """
    total_events = len(events)
    print(f"Processing {total_events} game events...\n")

    start = time.perf_counter()

    treasure_count = 0
    level_up_count = 0
    kill_count = 0
    death_count = 0
    login_count = 0
    logout_count = 0

    for msg, player, event_type, timestamp in event_generator(events):
        print(msg)

        if event_type == 'level_up':
            level_up_count += 1
        if event_type == 'item_found':
            treasure_count += 1
        if event_type == 'kill':
            kill_count += 1
        if event_type == 'death':
            death_count += 1
        if event_type == 'login':
            login_count += 1
        if event_type == 'logout':
            logout_count += 1

    end = time.perf_counter()
    elapsed = end - start

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print(f"Kill events: {kill_count}")
    print(f"Death events: {death_count}\n")
    print(f"Login events: {login_count}")
    print(f"Logout events: {logout_count}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {elapsed:.3f} seconds")


def fibonacci(size: int):
    """Yield first 'size' Fibonacci numbers."""
    a = 0
    b = 1
    for _ in range(size):
        yield a
        tmp = a
        a = b
        b = tmp + b


def is_prime(n: int) -> bool:
    """Return True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(size: int):
    """Yield first 'size' prime numbers."""
    n = 2
    i = 0
    while i < size:
        if is_prime(n):
            yield n
            i += 1
        n += 1


def ft_data_stream() -> None:
    """Process game events and demonstrate Fibonacci and prime generators."""
    print("=== Game Data Stream Processor ===\n")
    events = all_events()
    game_events_processor(events)

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

    size = 5
    first = True
    print(f"Prime numbers (first {size}):", end=" ")
    for prime in prime_generator(size):
        if not first:
            print(", ", end="")
        print(prime, end="")
        first = False
    print()


if __name__ == '__main__':
    ft_data_stream()
