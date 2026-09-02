import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    try:
        content: str = file.read()

        print("---")
        print(content, end="")
        print("---")
    except OSError as error:
        print(f"Error reading file '{filename}': {error}")
        return
    finally:
        file.close()

    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
