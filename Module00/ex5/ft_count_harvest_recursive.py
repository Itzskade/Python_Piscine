def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def countdown(day: int) -> None:
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        countdown(day + 1)
    countdown(1)
