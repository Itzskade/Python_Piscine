#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List


def ft_len(data: Any) -> int:
    """Return number of elements."""
    count = 0
    for _ in data:
        count += 1
    return count


def ft_sum(data: List[int]) -> int:
    """Return sum of list values."""
    total = 0
    i = 0
    length = ft_len(data)
    while i < length:
        total += data[i]
        i += 1
    return total


def ft_avg(data: List[int]) -> float:
    """Return average of list values."""
    length = ft_len(data)
    if length == 0:
        return 0
    return ft_sum(data) / length


def ft_word_count(data: str) -> int:
    """Return number of words in string."""
    in_word = False
    count = 0
    for char in data:
        if char != " ":
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count


class DataProcessor(ABC):
    """Base class for all data processors."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Process numeric lists."""
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False

        for x in data:
            if not isinstance(x, (int, float)):
                return False

        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Numeric Processor requires a list of numbers")

        count = ft_len(data)
        total = ft_sum(data)
        avg = ft_avg(data)

        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Process text strings."""
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Text Processor requires a string")

        chars = ft_len(data)
        words = ft_word_count(data)

        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    """Process log entries."""
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("LogProcessor requires a string")

        if "ERROR" in data:
            return "[ALERT] ERROR level detected: Connection timeout"

        return "[INFO] INFO level detected: System ready"


def run_numeric_processor():
    """Run numeric processor demo."""
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    nums = [1, 2, 3, 4, 5, 'a']   # puede ser cualquier cosa
    print(f"Processing data: {nums}")

    if num_proc.validate(nums):
        print("Validation: Numeric data verified")
        print(num_proc.format_output(num_proc.process(nums)))
    else:
        print("Validation: Numeric data NOT valid")
        print("Skipping Numeric Processor...")
    print()


def run_text_processor():
    """Run text processor demo."""
    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    text = "Hello Nexus World"
    print(f'Processing data: "{text}"')

    if text_proc.validate(text):
        print("Validation: Text data verified")
        print(text_proc.format_output(text_proc.process(text)))
    else:
        print("Validation: Text data NOT valid")
        print("Skipping Text Processor...")
    print()


def run_log_processor():
    """Run log processor demo."""
    print("Initializing Log Processor...")
    log_proc = LogProcessor()
    log = "ERROR: Connection timeout"
    print(f'Processing data: "{log}"')

    if log_proc.validate(log):
        print("Validation: Log entry verified")
        print(log_proc.format_output(log_proc.process(log)))
    else:
        print("Validation: Log entry NOT valid")
        print("Skipping Log Processor...")
    print()


def test_processor_polymorphic():
    """Show polymorphic processing."""
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    inputs = [
        [1, 2, 3],
        "Hello World!",
        "INFO: System ready"
    ]

    i = 0
    length = ft_len(processors)
    while i < length:
        processor = processors[i]
        data = inputs[i]
        result = processor.process(data)
        print(f"Result {i + 1}: {result}")
        i += 1
    print()


def stream_processor():
    """Main execution flow."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    run_numeric_processor()
    run_text_processor()
    run_log_processor()

    test_processor_polymorphic()

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
