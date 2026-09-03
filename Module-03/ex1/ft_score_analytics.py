import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = []

    for parameter in sys.argv[1:]:
        try:
            score = int(parameter)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{parameter}'")

    if len(scores) == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_score = sum(scores)
    average_score = total_score / len(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
