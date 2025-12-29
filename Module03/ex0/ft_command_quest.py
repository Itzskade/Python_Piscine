#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:29:34 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:29:34 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_command_quest() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    prog_name = sys.argv[0]
    if len(prog_name) > 1 and prog_name[0] == '.' and prog_name[1] == '/':
        prog_name = prog_name[2:]
    print(f"Program name: {prog_name}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")

if __name__ == '__main__':
    ft_command_quest()
