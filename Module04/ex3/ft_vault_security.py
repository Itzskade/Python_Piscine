#!/usr/bin/env python3

def secure_extraction() -> None:
    """Read and display contents of 'classified_data.txt' securely."""
    print("SECURE EXTRACTION:")
    with open('classified_data.txt', 'r') as vault:
        reading = vault.read()
        print(reading)
    print()


def secure_preservation() -> None:
    """Write new security protocols into 'security_protocols.txt'."""
    print("SECURE PRESERVATION:")
    with open('security_protocols.txt', 'w') as vault:
        vault.write("[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")


def ft_vault_security() -> None:
    """Run the vault security system with extraction and preservation."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("Initiating secure vault access...\n")
    print("Vault connection established with failsafe protocols\n")

    secure_extraction()
    secure_preservation()
    print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


if __name__ == '__main__':
    ft_vault_security()
