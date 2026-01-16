def validate_ingredients(ingredients: str) -> str:
    """
    Return VALID if ingredients contain allowed element,
    else return INVALID.
    """
    allowed = ["fire", "water", "earth", "air"]
    if any(element in ingredients for element in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
