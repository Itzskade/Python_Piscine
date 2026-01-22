#!/usr/bin/env python3

from enum import Enum
from datetime import datetime
from typing import Optional

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("Pydantic not found: Install -> pip install pydantic")
    exit()


class ContactType(Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def custom_validation_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (
                self.contact_type == ContactType.PHYSICAL
                and self.is_verified is False
                ):
            raise ValueError("Physical contact reports must be verified")
        if (
                self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3
                ):
            raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                    )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                    "Strong signals (> 7.0) should include received messages"
                    )
        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")

    print("Valid contact report:")

    try:
        contact = AlienContact(
                contact_id='AC_2004_001',
                timestamp=datetime(2004, 7, 7),
                location='Area 51, Nevada',
                contact_type=ContactType.RADIO,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received='Greatings from Zeta Reticuli',
                is_verified=False,
                )

        print("ID:", contact.contact_id)
        print("Type:", contact.contact_type.value)
        print("Location:", contact.location)
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print("Witnesses", contact.witness_count)
        print("Message:", contact.message_received)

    except ValidationError as error:
        for e in error.errors():
            print(e['msg'].replace("Value error", ""))

    print("\n======================================")
    print("Expected validation error:")

    try:
        _ = AlienContact(
                contact_id='AC_2004_002',
                timestamp=datetime(2004, 12, 9),
                location='Area 51, Nevada',
                contact_type=ContactType.TELEPATHIC,
                signal_strength=9.5,
                duration_minutes=32,
                witness_count=2,
                message_received='Greatings from 42',
                is_verified=False,
                )

    except ValidationError as error:
        for e in error.errors():
            print(e['msg'].replace("Value error, ", ""))

    try:
        from tools.generated_data.alien_contacts import ALIEN_CONTACTS

    except ImportError:
        print("Could not import ALIEN_CONTACTS")
        exit()

    for alien_data in ALIEN_CONTACTS:
        try:
            contact = AlienContact(**alien_data)

        except ValidationError as error:
            for e in error.errors():
                print(e['msg'].replace("Value error, ", ""))

        print("\n======================================")
        print("ID:", contact.contact_id)
        print("Type:", contact.contact_type.value)
        print("Location:", contact.location)
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print("Witnesses", contact.witness_count)
        print("Message:", contact.message_received)


if __name__ == '__main__':
    main()
