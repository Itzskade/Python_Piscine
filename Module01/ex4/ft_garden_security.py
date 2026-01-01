#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        print(f"Plant created: {self.name}")
        self.height = 0
        self.age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.age = age
            print(f"Age updated: {self.age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
            return 

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

    def get_info(self) -> None:
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")

def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    plant.set_age(-10)
    plant.get_info()

if __name__ == "__main__":
    ft_garden_security()
