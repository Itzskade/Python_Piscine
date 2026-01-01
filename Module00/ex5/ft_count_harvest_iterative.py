#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:25:52 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:25:52 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for day in range(1, days + 1):
        print(f"Day {day}")
    print("Harvest time!")

if __name__ == '__main__':
    ft_count_harvest_iterative()
