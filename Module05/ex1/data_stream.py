#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Base class for all data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data (to be implemented in subclasses)."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter batch according to a criteria (optional)."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic stream statistics."""
        return {
            'stream_id': self.stream_id,
            'type': self.__class__.__name__,
            'processed_count': self.processed_count
        }


class SensorStream(DataStream):
    """Stream specialized in sensor/environmental data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.critical_count = 0
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        temperatures = []
        for item in data_batch:
            try:
                if 'temp:' in str(item):
                    temperature = float(str(item).split('temp:')[1])
                    temperatures.append(temperature)
                    if temperature > 45:
                        self.critical_count += 1
            except ValueError as e:
                print(e)

        batch_info = f"Processing sensor batch: {data_batch}"
        if temperatures:
            avg_temp = sum(temperatures) / len(temperatures)
            analysis = (
                    f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: {avg_temp:.1f}°C"
                    )
        else:
            analysis = "No temperature readings"

        return f"{batch_info}\n{analysis}"


class TransactionStream(DataStream):
    """Stream specialized in financial transactions."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.large_count = 0
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        net_flow = 0

        for item in data_batch:
            try:
                key, value = str(item).split(':')
                value = int(value.strip())
                if 'buy' in key.lower():
                    net_flow += value
                elif 'sell' in key.lower():
                    net_flow -= value
                if value > 1000:
                    self.large_count += 1
            except ValueError as e:
                print(e)

        batch_info = f"Processing transaction batch: {data_batch}"
        sign = '+' if net_flow >= 0 else '-'
        analysis = (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {sign}{abs(net_flow)} units"
                )
        return f"{batch_info}\n{analysis}"


class EventStream(DataStream):
    """Stream specialized in system events."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        error_count = 0

        for item in data_batch:
            if item.lower() == 'error':
                error_count += 1

        batch_info = f"Processing event batch: {data_batch}"
        if error_count:
            analysis = (f"Event analysis: {len(data_batch)} events, "
                        f"{error_count} error detected"
                        )
        else:
            analysis = (
                    f"Event analysis: {len(data_batch)} events, "
                    "no errors detected"
                    )

        return f"{batch_info}\n{analysis}"


class StreamProcessor:
    """Manages multiple streams polymorphically."""

    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print()

    def process_batch(self, data_batch: List[Any]) -> None:
        print("Batch 1 Results:")
        for stream in self.streams:
            if isinstance(stream, SensorStream):
                count = 0
                for item in data_batch:
                    item_str = str(item).lower()
                    if ':' in item_str and (
                            'temp' in item_str or
                            'humidity' in item_str or
                            'pressure' in item_str):
                        count += 1
                label = "readings"

            elif isinstance(stream, TransactionStream):
                count = 0
                for item in data_batch:
                    item_str = str(item).lower()
                    if ':' in item_str and (
                            'buy' in item_str or
                            'sell' in item_str):
                        count += 1
                label = "operations"

            elif isinstance(stream, EventStream):
                count = 0
                for item in data_batch:
                    item_str = str(item).lower()
                    if item_str in ['login', 'logout', 'error']:
                        count += 1
                label = "events"

            print(f"- {stream.__class__.__name__.replace('Stream', '')} "
                  f"data: {count} {label} processed")


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    event_batch = ["login", "error", "logout"]

    mixed_batch = [
            "temp:46", "temp:52",
            "buy:1100", "sell:300", "sell:100", "sell:200",
            "logout", "login", "logout"
            ]

    sensor = SensorStream("SENSOR_001")
    print(sensor.process_batch(sensor_batch))
    print()

    transaction = TransactionStream("TRANS_001")
    print(transaction.process_batch(transaction_batch))
    print()

    event = EventStream("EVENT_001")
    print(event.process_batch(event_batch))
    print()

    processor = StreamProcessor([sensor, transaction, event])
    processor.process_batch(mixed_batch)
    critical_sensors = sensor.critical_count
    large_transactions = transaction.large_count
    print()

    print("Stream filtering active: High-priority data only")
    print(
            f"Filtered results: {critical_sensors} critical sensor alerts, "
            f"{large_transactions} large transactions"
          )
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == '__main__':
    data_stream()
