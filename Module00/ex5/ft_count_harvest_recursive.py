#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:25:58 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:25:59 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    
    def countdown(day: int) -> None:
        if day > days:
            print ("Harvest time!")
            return
        print(f"Day {day}")
        countdown(day + 1)
    countdown(1)

if __name__ == '__main__':
    ft_count_harvest_recursive()
