import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan", "santi"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use", "trekking"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)

        yield player, action


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)

        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    for index in range(1000):
        player, action = next(event_stream)

        print(f"Event {index}: Player {player} did action {action}")

    event_stream = gen_event()
    events: list[tuple[str, str]] = []

    for _ in range(10):
        events.append(next(event_stream))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
