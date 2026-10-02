#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.plant_age: int = plant_age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, "
              f"{self.plant_age} days old")


def main() -> None:
    print("=== Plant Factory Output ===")

    plant_data: list[tuple[str, float, int]] = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120)
    ]

    plants: list[Plant] = [Plant(n, h, a) for n, h, a in plant_data]

    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
