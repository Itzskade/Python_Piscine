def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_name = seed_type.capitalize()
    msg = f"{seed_name} seeds: {quantity} {unit}"
    if unit == "packets":
        print(f"{msg} available")
    elif unit == "grams":
        print(f"{msg} total")
    elif unit == "area":
        print(f"{msg} square meters")
    else:
        print("Unknown unit type")
