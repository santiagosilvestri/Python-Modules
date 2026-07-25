#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    days_old: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.days_old = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.days_old = 45

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.days_old = 120

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
