#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float) -> None:
        self._name = name
        self._height = 0.0
        self._days_old = 0
        self._growth_rate = growth_rate
        self._stats: Plant.Statistics = Plant.Statistics()

        self.set_height(height)
        self.set_age(days_old)

    @staticmethod
    def is_older_than_year(days_old: int) -> bool:
        return days_old > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name}: {self._height}cm, "
              f"{self._days_old} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)
        self._stats.record_grow()

    def age(self, days: int = 1) -> None:
        self._days_old += days
        self._stats.record_age()

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, days_old: int) -> bool:
        if days_old < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._days_old = days_old
        return True

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old

    def display_statistics(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._tree_stats = Tree.TreeStatistics()
        self._stats = self._tree_stats

    def produce_shade(self) -> None:
        self._tree_stats.record_shade()
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and "
              f"{self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, harvest_season: str) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, days_old, growth_rate, color)
        self._seed_count = 0

    def bloom(self, seed_count: int = 42) -> None:
        super().bloom()
        self._seed_count = seed_count

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_statistics()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print("Is 30 days more than a year? -> "
          f"{Plant.is_older_than_year(30)}")
    print("Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    display_plant_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 1.0, 5.0)
    oak.show()
    display_plant_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    display_plant_statistics(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_statistics(anonymous)


if __name__ == "__main__":
    main()
