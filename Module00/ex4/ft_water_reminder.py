#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:25:34 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:25:35 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder() -> None:
    days = 4
    print(f"Days since last watering: {days}"))
    if (days > 2):
        print("Water the plants")
    else:
        print("Plants are fine")

if __name__ == '__main__':
    ft_water_reminder()
