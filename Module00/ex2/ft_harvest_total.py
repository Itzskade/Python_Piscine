# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:25:11 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:25:13 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
    first = int(input("Day 1 harvest: "))
    second = int(input("Day 2 harvest: "))
    third = int(input("Day 3 harvest: "))
    print(f"Total harvest: {first + second + third}")
