#!/usr/bin/env python3

def recover_data() -> None:
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    file = open('ancient_fragment.txt', 'r')
    reading = file.read()
    print(reading)
    file.close()

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYYSTEM ===\n")
    recover_data()
    print()
    print("Data inscription complete. Storage unit sealed.")

if __name__ == '__main__':
    ft_ancient_text()
