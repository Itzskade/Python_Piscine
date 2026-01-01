# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:26:18 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:26:22 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_name = seed_type.capitalize()
    msg = f"{seed_name} seeds: {quantity} {unit}"
    if unit == "packets":
        print(f"{msg} available")
    elif unit == "grams":
        print(f"{msg} total")
    elif unit == "area":
        print(f"{msg} square meters")
    else:
        print("Unknown unit type")
