#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._plant_age: int = 0

        print(f"Plant created: {self.name}: {height}cm, {plant_age} days old")
        self.set_height(height)
        self.set_age(plant_age)

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, plant_age: int) -> None:
        if plant_age >= 0:
            self._plant_age = plant_age
            print(f"Age updated: {plant_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def show(self) -> None:
        print(f"Current state: {self.name}: {self.get_height()}cm, "
              f"{self.get_age()} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose: Plant = Plant("Rose", 15.0, 10)
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-5.0)
    rose.set_age(-10)
    print()
    rose.show()


if __name__ == "__main__":
    main()
