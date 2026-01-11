def validate_ingredients(ingredients: str) -> str:
    """
    Return VALID if ingredients contain allowed element,
    else return INVALID.
    """
    allowed = ['fire', 'water', 'earth', 'air']
    parts = ingredients.split()

    if all(part in allowed for part in parts):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
