#!/usr/bin/env python3

import sys


def catch_errors(filename: str) -> None:
    """Attempt to read a file and handle errors with logging."""
    if filename == 'standard_archive.txt':
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to "
              f"'{filename}'...", file=sys.stderr)

    try:
        with open(filename, 'r') as vault:
            vault.read()
            print("SUCCESS: Archive recovered -- "
                  "``knowledge preserved for humanity´´")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix", file=sys.stderr)
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access", file=sys.stderr)
        print("STATUS: Crisis handled, security maintained\n")
    except Exception:
        print("RESPONSE: Unexpected anomaly", file=sys.stderr)
        print("STATUS: Crisis handled, \n")


def ft_crisis_response() -> None:
    """Run the crisis response system on multiple archives."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    catch_errors('lost_archive.txt')
    catch_errors('classified_vault.txt')
    catch_errors('standard_archive.txt')
    print("All crisis scenarios handled successfully. Archives secure")


if __name__ == '__main__':
    ft_crisis_response()
