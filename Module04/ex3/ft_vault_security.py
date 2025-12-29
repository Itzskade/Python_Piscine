#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_vault_security.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 18:20:17 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/28 18:20:17 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def secure_extraction() -> None:
    print("SECURE EXTRACTION:")
    with open('classified_data.txt', 'r') as vault:
        reading = vault.read()
        print(reading)
    print()


def secure_preservation() -> None:
    print("SECURE PRESERVATION:")
    with open('security_protocols.txt', 'w') as vault:
        vault.write("[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")


def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("Initiating secure vault access...\n")
    print("Vault connection established with failsafe protocols\n")

    secure_extraction()
    secure_preservation()
    print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


if __name__ == '__main__':
    ft_vault_security()
