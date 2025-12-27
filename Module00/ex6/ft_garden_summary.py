# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:26:08 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:26:09 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary() -> None:
    name = input("Enter garden name: ")
    nplants = input("Enter number of plants: ")
    print(f"Garden: {name}")
    print(f"Plants: {nplants}") 
    print("Status: Growing Well!")
