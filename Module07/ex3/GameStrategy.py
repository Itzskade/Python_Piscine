class GameStrategi(ABC):

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        ...

    @abstractmethod
    def prioritze_targets(self, available_targets: list) -> list:
        ...
