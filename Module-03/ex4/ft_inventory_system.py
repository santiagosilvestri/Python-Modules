import sys


def create_inventory(parameters: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for parameter in parameters:
        try:
            item, quantity = parameter.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item = item.strip()
        quantity = quantity.strip()

        if item == "" or quantity == "":
            print(f"Error - invalid parameter '{parameter}'")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            inventory[item] = int(quantity)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")

    return inventory


def analyze_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    total_quantity = sum(inventory.values())
    total_items = len(item_list)

    print(f"Item list: {item_list}")

    print(f"Total quantity of the {total_items} items: {total_quantity}")

    if total_items == 0:
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
        return

    for item in item_list:
        if total_quantity == 0:
            percentage = 0.0
        else:
            percentage = round(inventory[item] / total_quantity * 100, 1)

        print(f"Item {item} represents {percentage}%")

    most_abundant = item_list[0]
    least_abundant = item_list[0]

    for item in item_list[1:]:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item

        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant} "
          f"with quantity {inventory[most_abundant]}")

    print(f"Item least abundant: {least_abundant} "
          f"with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})

    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = create_inventory(sys.argv[1:])
    analyze_inventory(inventory)


if __name__ == "__main__":
    main()
