#!/usr/bin/env python3

from datetime import datetime
from typing import Optional

try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("Pydantic not found: Install -> pip install pydantic")
    exit()


class SpaceStation(BaseModel):
    """Pydantic model for Space Station validation."""
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=200)


def main() -> None:
    """Pydantic creation test."""
    print("Space Station Data Validation")
    print("========================================")

    try:
        station = SpaceStation(
                station_id='ISS001',
                name='International Space Station',
                crew_size=6,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime(2026, 1, 19),
                is_operational=True,
                notes="It works"
                )

        print("Valid station created:")
        print("ID:", station.station_id)
        print("Name:", station.name)
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status = ('Operational' if station.is_operational
                  else 'Non-Operational')
        print("Status:", status)

    except ValidationError as error:
        for e in error.errors():
            print(e['msg'])
        exit()

    print("\n========================================")
    print("Expected validation error:")
    try:
        _ = SpaceStation(
                station_id='ISS002',
                name='Universal Space Station',
                crew_size=30,
                power_level=80,
                oxygen_level=62.3,
                last_maintenance=datetime(2026, 1, 19),
                is_operational=True,
                notes="It doesn't work"
                )

    except ValidationError as error:
        for e in error.errors():
            print(e['msg'])

    try:
        from generated_data.space_stations import SPACE_STATIONS

    except ImportError:
        print("Could not import SPACE_STATIONS")
        exit()

    for station_data in SPACE_STATIONS:
        try:
            station = SpaceStation(**station_data)

        except ValidationError as error:
            for e in error.errors():
                print(e['msg'])
            continue
        print("\n========================================")
        print("Valid station created:")
        print("ID:", station.station_id)
        print("Name:", station.name)
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status = ('Operational' if station.is_operational
                  else 'Non-Operational')
        print("Status:", status)


if __name__ == '__main__':
    main()
