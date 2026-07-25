#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float) -> None:
        self._name = name
        self._height = 0.0
        self._days_old = 0
        self._growth_rate = growth_rate

        self.set_height(height)
        self.set_age(days_old)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days_old} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._days_old += 1

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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float, color: str) -> None:
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
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
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

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def main() -> None:
    rose = Flower("Rose", 15.0, 10, 0.8, "red")
    oak = Tree("Oak", 200.0, 365, 1.0, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")

    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato.show()

    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()


if __name__ == "__main__":
    main()
