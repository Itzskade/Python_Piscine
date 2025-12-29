#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_stream_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 17:57:20 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/28 17:57:20 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys 

def data_transmission() -> None:
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    print()

    print(f"[STANDARD] Archive status from {archivist_id}: {status_report}")
    print("[ALERT] System diagnostic: Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete")
    print()
    

def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    data_transmission()
    print ("Three-channel communication test successful.")

if __name__ == '__main__':
    ft_stream_management()
