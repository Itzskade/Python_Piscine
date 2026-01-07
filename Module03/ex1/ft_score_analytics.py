#!/usr/bin/env python3

import sys


def new_list() -> int:
    """Return integer scores parsed from command-line arguments."""
    scores = []
    i = 1
    while i < len(sys.argv):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError as e:
            print(e)
        i += 1
    return scores


def ft_score_analytics() -> None:
    """Print basic statistics for given scores."""
    print("=== Player Score Analytics ===")
    scores = new_list()
    if len(sys.argv) < 2:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score = {sum(scores)}")
        print(f"Avarage score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range:{max(scores) - min(scores)}\n")


if __name__ == '__main__':
    ft_score_analytics()
