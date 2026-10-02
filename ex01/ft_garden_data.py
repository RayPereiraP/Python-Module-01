#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.plant_age: int = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    plant1: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Sunflower", 80, 45)
    plant3: Plant = Plant("Cactus", 15, 120)

    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
