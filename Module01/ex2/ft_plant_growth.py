#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:27:33 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:27:33 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def grow(self, cm):
        self.height += cm
    def age_one_day(self):
        self.age += 1
    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth():
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())

    for day in range (2, 8):
        rose.age_one_day()
        rose.grow(1)

    print("=== Day 7 ===")
    print(rose.get_info())

    growth = rose.height - rose.initial_height
    print(f"Growth this week: +{growth}cm")

if __name__ == "__main__":
    ft_plant_growth()
