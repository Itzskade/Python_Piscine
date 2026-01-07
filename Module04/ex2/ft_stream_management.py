#!/usr/bin/env python3

import sys


def data_transmission() -> None:
    """Collect archivist input and print transmission log."""
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    print()

    print(f"[STANDARD] Archive status from {archivist_id}: {status_report}")
    print("[ALERT] System diagnostic: Communication "
          "channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete")
    print()


def ft_stream_management() -> None:
    """Run the communication system for data transmission."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    data_transmission()
    print("Three-channel communication test successful.")


if __name__ == '__main__':
    ft_stream_management()
