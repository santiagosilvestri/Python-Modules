import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                          "Gregory", "john", "kevin", "Liam", "santi"]

    print(f"\nInitial list of players: {players}")

    capitalized_players: list[str] = [
        player.capitalize() for player in players]

    print(f"New list with all names capitalized: {capitalized_players}")

    initial_capitalized_players: list[str] = [
        player for player in players if player == player.capitalize()]

    print(f"New list of capitalized names only: {initial_capitalized_players}")

    score_dict: dict[str, int] = {
        player: random.randint(0, 1000) for player in capitalized_players}

    print(f"Score dict: {score_dict}")

    average_score: float = round(sum(score_dict.values()) / len(score_dict), 2)

    print(f"Score average is {average_score:.2f}")

    high_scores: dict[str, int] = {
        player: score for player,
        score in score_dict.items() if score > average_score}

    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
