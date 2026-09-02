def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                return (True, file.read())

        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "File written successfully")

        return (False, "Invalid action")

    except OSError as error:
        return (False, str(error))


def main() -> None:
    print(secure_archive("archive.txt"))

    print(secure_archive("new_archive.txt", "write", "Hello!Mi name es Santi"))


if __name__ == "__main__":
    main()
