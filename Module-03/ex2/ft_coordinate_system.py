import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        data = input("Enter new coordinates as floats in format 'x,y,z': ")

        try:
            x_data, y_data, z_data = data.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        coordinates: list[float] = []

        for parameter in (x_data, y_data, z_data):
            parameter = parameter.strip()

            try:
                coordinates.append(float(parameter))
            except ValueError as error:
                print(f"Error on parameter '{parameter}': {error}")
                break
        else:
            return coordinates[0], coordinates[1], coordinates[2]


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    first_position = get_player_pos()

    print(f"Got a first tuple: {first_position}")
    print(f"It includes: X={first_position[0]}, "
          f"Y={first_position[1]}, "
          f"Z={first_position[2]}")

    distance_to_center = math.sqrt(first_position[0] ** 2
                                   + first_position[1] ** 2
                                   + first_position[2] ** 2)

    print(f"Distance to center: {round(distance_to_center, 4)}")

    print("\nGet a second set of coordinates")
    second_position = get_player_pos()

    distance_between = math.sqrt(
                        (second_position[0] - first_position[0]) ** 2
                        + (second_position[1] - first_position[1]) ** 2
                        + (second_position[2] - first_position[2]) ** 2)

    print("Distance between the 2 sets of coordinates: "
          f"{round(distance_between, 4)}")


if __name__ == "__main__":
    main()
