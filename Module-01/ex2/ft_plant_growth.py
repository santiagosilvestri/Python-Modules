#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    days_old: int
    growth_rate: float

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.days_old += 1


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days_old = 30
    rose.growth_rate = 0.8

    initial_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    weekly_growth = round(rose.height - initial_height, 1)

    print(f"Growth this week: {weekly_growth}cm")


if __name__ == "__main__":
    main()
