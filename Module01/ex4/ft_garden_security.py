#!/usr/bin/env python3

class SecurePlant:
    """Represents name, height (cm) and age (days) of a plant."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        print(f"Plant created: {self.name}")
        self.height = 0
        self.age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set the height, rejecting negative values."""
        if height >= 0:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return

    def set_age(self, age: int) -> None:
        """Set the age, rejecting negative values."""
        if age >= 0:
            self.age = age
            print(f"Age updated: {self.age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
            return 

    def get_info(self) -> None:
        """Print the plant's name, height, and age."""
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")


def ft_garden_security() -> None:
    """Test the plant security system with invalid inputs."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    plant.set_age(-10)
    plant.get_info()

if __name__ == "__main__":
    ft_garden_security()
