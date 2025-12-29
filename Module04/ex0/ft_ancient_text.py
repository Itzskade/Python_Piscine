#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 16:00:56 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/28 16:00:56 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def recover_data():
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    file = open('ancient_fragment.txt', 'r')
    reading = file.read()
    print(reading)
    file.close()

def ft_ancient_text():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYYSTEM ===\n")
    recover_data()
    print()

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")

if __name__ == '__main__':
    ft_ancient_text()
