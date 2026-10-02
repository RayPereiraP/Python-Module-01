#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0
            self.shade_calls: int = 0

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.plant_age: int = plant_age
        self.stats: Plant.Stats = self.Stats()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self.height += 1.5
        self.stats.grow_calls += 1

    def age(self) -> None:
        self.plant_age += 1
        self.stats.age_calls += 1

    def show(self) -> None:
        self.stats.show_calls += 1
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, color: str) -> None:
        super().__init__(name, height, plant_age)
        self.color: str = color
        self.has_bloomed: bool = False

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 plant_age: int, color: str) -> None:
        super().__init__(name, height, plant_age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        self.stats.shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")


def display_stats(plant: Plant) -> None:
    base_stats: str = (f"Stats: {plant.stats.grow_calls} grow, "
                       f"{plant.stats.age_calls} age, "
                       f"{plant.stats.show_calls} show")
    if isinstance(plant, Tree):
        base_stats += f" {plant.stats.shade_calls} shade"
    print(base_stats)


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}\n")

    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("\n[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("\n[statistics for Rose]")
    display_stats(rose)

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("\n[statistics for Oak]")
    display_stats(oak)
    print("\n[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print("\n=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("\n[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("\n[statistics for Sunflower]")
    display_stats(sunflower)

    print("\n=== Anonymous")
    anon: Plant = Plant.create_anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    display_stats(anon)


if __name__ == "__main__":
    main()
