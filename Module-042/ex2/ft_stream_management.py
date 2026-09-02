import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
    except OSError as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{filename}': {error}\n")
        return

    try:
        content: str = file.read()

        print("---")
        print(content, end="")

        if content and not content.endswith("\n"):
            print()

        print("---")

    except OSError as error:
        sys.stderr.write(
            f"[STDERR] Error reading file '{filename}': {error}\n")
        return

    finally:
        file.close()

    print(f"File '{filename}' closed.")

    transformed: str = content.replace("\n", "#\n")

    if content and not content.endswith("\n"):
        transformed += "#"

    print("Transform data:")
    print("---")
    print(transformed, end="")

    if transformed and not transformed.endswith("\n"):
        print()

    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    new_filename: str = sys.stdin.readline().rstrip("\n")

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")

    try:
        new_file: typing.IO[str] = open(new_filename, "w")
    except OSError as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{new_filename}': {error}\n")
        print("Data not saved.")
        return

    try:
        new_file.write(transformed)

    except OSError as error:
        sys.stderr.write(
            f"[STDERR] Error writing file '{new_filename}': {error}\n")
        print("Data not saved.")
        return

    finally:
        new_file.close()

    print(f"Data saved in file '{new_filename}'.")


if __name__ == "__main__":
    main()
