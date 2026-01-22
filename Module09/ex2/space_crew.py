#!/usr/bin/env python3

from enum import Enum
from datetime import datetime

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("Pydantic not found: Installation -> pip install pydantic")
    exit()


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=2, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        leadership = any(
                member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
                for member in self.crew)
        if not leadership:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced = 0
            for member in self.crew:
                if member.years_experience > 5:
                    experienced += 1
            if experienced < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) "
                                 "need 50% experienced crew (5+ years)")
        all_actived = any(member.is_active for member in self.crew)
        if not all_actived:
            raise ValueError("All crew members must be active")
        return self


def main():
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        mission = SpaceMission(
                mission_id='M2024_MARS',
                mission_name='Mars Colony Establishment',
                destination='Mars',
                launch_date=datetime(2024, 6, 6),
                duration_days=900,
                crew=[
                    CrewMember(
                        member_id='sconnor1',
                        name='Sarah Connor',
                        rank=Rank.COMMANDER,
                        age=32,
                        specialization='Mission Command',
                        years_experience=8,
                        is_active=True
                        ),
                    CrewMember(
                        member_id='jsmith2',
                        name='John Smith',
                        rank=Rank.LIEUTENANT,
                        age=26,
                        specialization='Navigation',
                        years_experience=6,
                        is_active=True
                        ),
                    CrewMember(
                        member_id='ajohnson3',
                        name='Alice Johnson',
                        rank=Rank.OFFICER,
                        age=29,
                        specialization='Engineering',
                        years_experience=2,
                        is_active=True
                        )
                    ],
                mission_status='planned',
                budget_millions=2500.0
                )

        print("Valid mission created:")
        print("Mission:", mission.mission_name)
        print("ID:", mission.mission_id)
        print("Destination:", mission.destination)
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print("Crew size:", len(mission.crew))
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")

    except ValidationError as error:
        for e in error.errors():
            print(e['msg'].replace("Value error, ", ""))

    print("\n=========================================")
    print("Expected validation error:")
    try:
        mission = SpaceMission(
                mission_id='M2026_MARS',
                mission_name='Mars Colony Establishment Again',
                destination='Mars',
                launch_date=datetime(2026, 1, 1),
                duration_days=500,
                crew=[
                    CrewMember(
                        member_id='rmarin-n',
                        name='Roger Marin',
                        rank=Rank.LIEUTENANT,
                        age=29,
                        specialization='Programming',
                        years_experience=1,
                        is_active=True
                        ),
                    CrewMember(
                        member_id='mgarcia3',
                        name='Manolo Garcia',
                        rank=Rank.LIEUTENANT,
                        age=21,
                        specialization='Navigation',
                        years_experience=7,
                        is_active=True
                        ),
                    CrewMember(
                        member_id='paguado',
                        name='Pedro Aguado',
                        rank=Rank.OFFICER,
                        age=49,
                        specialization='Engineering',
                        years_experience=12,
                        is_active=True
                        )
                    ],
                mission_status='planned',
                budget_millions=2500.0
                )
    except ValidationError as error:
        for e in error.errors():
            print(e['msg'].replace("Value error, Must", "Mission must"))

    try:
        from tools.generated_data.space_missions import SPACE_MISSIONS

    except ImportError:
        print("Could not import SPACE_MISSIONS")
        exit()

    for mission_data in SPACE_MISSIONS:
        try:
            mission = SpaceMission(**mission_data)

        except ValidationError as error:
            for e in error.errors():
                print(e['msg'].replace("Value error, ", ""))

        print("\n=========================================")
        print("Valid mission created:")
        print("Mission:", mission.mission_name)
        print("ID:", mission.mission_id)
        print("Destination:", mission.destination)
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print("Crew size:", len(mission.crew))
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")


if __name__ == '__main__':
    main()
