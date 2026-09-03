import random


ACHIEVEMENTS: list[str] = ["Boss Slayer",
                           "Collector Supreme",
                           "Crafting Genius",
                           "First Steps",
                           "Hidden Path Finder",
                           "Master Explorer",
                           "Sharp Mind",
                           "Speed Runner",
                           "Strategist",
                           "Survivor",
                           "Treasure Hunter",
                           "Unstoppable",
                           "Untouchable",
                           "World Savior"]


def gen_player_achievements() -> set[str]:
    selected = random.sample(ACHIEVEMENTS, random.randint(6, 9))
    return set(selected)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    all_distinct = alice.union(bob, charlie, dylan)
    all_common = alice.intersection(bob, charlie, dylan)

    print(f"All distinct achievements: {all_distinct}\n")
    print(f"Common achievements: {all_common}\n")

    only_alice = alice.difference(bob.union(charlie, dylan))
    only_bob = bob.difference(alice.union(charlie, dylan))
    only_charlie = charlie.difference(alice.union(bob, dylan))
    only_dylan = dylan.difference(alice.union(bob, charlie))

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")

    all_achievements = set(ACHIEVEMENTS)

    alice_missing = all_achievements.difference(alice)
    bob_missing = all_achievements.difference(bob)
    charlie_missing = all_achievements.difference(charlie)
    dylan_missing = all_achievements.difference(dylan)

    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    main()
