#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 days_old: int) -> None:
        self._name = name
        self._height = 0.0
        self._days_old = 0

        self.set_height(height)
        self.set_age(days_old)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days_old} days old")

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


def main() -> None:
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()

    if rose.set_height(25.0):
        print(f"Height updated: {rose.get_height():g}cm")

    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")

    if not rose.set_height(-5.0):
        print("Height update rejected")

    if not rose.set_age(-10):
        print("Age update rejected")

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
