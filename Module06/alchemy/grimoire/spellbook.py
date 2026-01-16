from alchemy.grimoire.validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Return a message recording the spell
    or rejecting it if invalid.
    """
    valid = validate_ingredients(ingredients)

    if valid.endswith('INVALID'):
        return f"Spell rejected: {spell_name} ({valid})"
    return f"Spell recorded: {spell_name} ({valid})"
