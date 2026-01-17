from typing import List, Dict
from tools.card_generator import CardGenerator
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature
from ex1.SpellCard import SpellCard as Spell
from ex1.Deck import DeckError
from ex1.ArtifactCard import ArtifactCard as Artifact, ArtifactError
from ex3.CardFactory import CardFactory


class CreatureError(Exception):
    pass


class SpellError(Exception):
    pass


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.generator = CardGenerator()

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            data = self.generator.get_creature(name_or_power)
        else:
            data = self.generator.get_random_creature()
        if data is None:
            raise CreatureError(f"No creature found for {name_or_power}")
        return Creature(**data)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            data = self.generator.get_spell(name_or_power)
        else:
            data = self.generator.get_random_spell()
        if data is None:
            raise SpellError(f"No spells found for {name_or_power}")
        return Spell(**data)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            data = self.generator.get_artifact(name_or_power)
        else:
            data = self.generator.get_random_artifact()
        if data is None:
            raise ArtifactError(f"No artifacts found for {name_or_power}")
        return Artifact(**data)

    def create_themed_deck(self, size: int) -> Dict[str, List[Card]]:
        raw_cards = self.generator.generate_random_deck(size)
        deck_cards = []
        for data in raw_cards:
            if "attack" in data:
                deck_cards.append(Creature(**data))
            elif "effect_type" in data:
                deck_cards.append(Spell(**data))
            elif "durability" in data:
                deck_cards.append(Artifact(**data))
            else:
                raise DeckError("Not possible to generate a themed deck")
        return {'deck': deck_cards}

    def get_supported_types(self) -> List[str]:
        return ['creature', 'spell', 'artifact']
