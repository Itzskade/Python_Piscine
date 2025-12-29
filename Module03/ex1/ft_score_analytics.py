#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:29:44 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:29:48 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def put_numbers_on_list() -> int:
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
    print("=== Player Score Analytics ===")
    scores = put_numbers_on_list()
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}" )
        print(f"Total players: {len(scores)}")
        print(f"Total score = {sum(scores)}")
        print(f"Avarage score: {sum(scores) / len(scores)}") 
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range:{max(scores) - min(scores)}\n")

if __name__ == '__main__':
    ft_score_analytics()
