#!/usr/bin/env python3

class SecurePlant:
    """Represents plant with protected height & age values."""
    def __init__(self, name: str) -> None:
        """Initialize plant with name & protected attributes."""
        self.name = name
        self._height = 0
        self._age = 0

    def get_height(self) -> int:
        """Return current height of the plant."""
        return self._height

    def set_height(self, height: int) -> None:
        """Set plant height, rejecting negative values."""
        if height < 0:
            print(
                "Invalid operation attempted: "
                f"height {height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            print()
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def get_age(self) -> int:
        """Return current age of the plant."""
        return self._age

    def set_age(self, age: int) -> None:
        """Set plant age, rejecting negative values."""
        if age < 0:
            print(
                    "Invalid operation attempted: "
                    f"age {age} days [REJECTED]"
            )
            print("Security: Negative days rejected")
            print()
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")
            print()

    def display_info(self) -> None:
        """Display current plant information."""
        print(
            f"Current plant: {self.name} "
            f"{self.get_height()}cm {self.get_age()} days"
        )


def ft_garden_security() -> None:
    """Test SecurePlant with valid & invalid operations."""
    print("=== Garden Security ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_age(-5)
    rose.display_info()


if __name__ == "__main__":
    ft_garden_security()
