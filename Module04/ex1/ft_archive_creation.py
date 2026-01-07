#!/usr/bin/env python3

def create_file():
    """Create a new file 'new_discovery.txt' and return file object."""
    file = open('new_discovery.txt', 'w')
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")
    return file


def write_file(file) -> None:
    """Write predefined entries into the given file."""
    entries = [
            "New quantum algorith discovered",
            "Efficiency increased by 347 %",
            "Archived by Data Archivist trainee"
    ]
    count = 1
    print("Inscribing preservation data...")
    for entry in entries:
        file.write(f"ENTRY {count:03d} {entry}\n")
        print(f"ENTRY {count:03d} {entry}")
        count += 1
    file.close()


def ft_archive_creation() -> None:
    """Run the preservation system to create a new archive."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file = create_file()
    write_file(file)
    print()

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == '__main__':
    ft_archive_creation()
