def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_day(day):
        if day > days:
            return
        print("Day", day)
        count_day(day + 1)

    count_day(1)
    print("Harvest time!")
