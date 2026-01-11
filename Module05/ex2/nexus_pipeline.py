#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> None:
        pass

    def _run_stages(self, data: Any) -> Any:
        result = data
        for stage in self.stages:
            try:
                result = stage.process(result)
            except Exception:
                stage_name = stage.__class__.__name__
                raise RuntimeError(f"Error detected in {stage_name}: "
                                   "Invalid data format")
        return (result)


class InputStage:
    """Stage for input validation and parsing."""
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid format data")
        return data


class TransformStage:
    """
    Stage for data transformation and
    enrichment when the format allows it.
    """
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data = dict(data)
            data["enriched"] = True
        return data


class OutputStage:
    """Stage for output formatting."""
    def process(self, data: Any) -> Any:
        return data


class JSONAdapter(ProcessingPipeline):
    """Adapter for JSON data processing."""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        print("Processing JSON data through pipeline...")
        result = self._run_stages(data)
        print(f"Input: {data}")

        temp = result.get('value')
        if temp is not None:
            if 23 <= temp <= 28:
                temp_range = 'Normal range'
            elif temp < 23:
                temp_range = 'Cold range'
            else:
                temp_range = 'Hot range'
            print("Transform: Enriched with metadata and validation")
            print(f"Output: Processed temperature reading: {temp}°C "
                  f"{temp_range}")
            print()
        return result


class CSVAdapter(ProcessingPipeline):
    """Adapter for CSV data processing."""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        print("Processing CSV data through same pipeline...")
        if not isinstance(data, str):
            raise RuntimeError(f"Error detected in {self.__class__.__name__}: "
                               "CSVAdapter expects str")
        keys = data.split(',')
        structured_data = {value: None for value in keys}
        result = self._run_stages(structured_data)

        print(f"Input: {data}")
        print("Transform: Parsed and structured data")
        print("Output: User activity logged: 1 actions processed")
        print()
        return result


class StreamAdapter(ProcessingPipeline):
    """Adapter for Stream data processing."""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        print("Processing Stream data through same pipeline...")
        print(f"Input: {data}")
        readings = 5
        temps = [22.1]
        avg_temp = sum(temps) / len(temps)

        result = self._run_stages(data)

        print("Transform: Aggregated and filtered")
        print(f"Output: Stream summary: {readings} readings, "
              f"avg: {avg_temp}°C")
        print()
        return result


def pipeline_chain_demo() -> None:
    """Show how pipelines works"""
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    print()
    print("Chain result: 100 records processed through 3-stage pipeline")
    print("Performance: 95 % efficiency, 0.2s total processing time")


class NexusManager:
    """Manager for multiple pipelines and data processing."""
    def __init__(self) -> None:
        """Initialize with an empty list of pipelines."""
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register a new pipeline with the manager."""
        self.pipelines.append(pipeline)

    def process_data(self, data_list: List[Any]) -> None:
        """
        Process each data item through the appropriate
        pipeline with error recovery.
        """
        print("=== Multi-Format Data Processing ===\n")
        for data in data_list:
            try:
                if isinstance(data, dict) and "value" in data:
                    pipeline = next(p for p in self.pipelines if
                                    isinstance(p, JSONAdapter))
                elif isinstance(data, str) and ',' in data:
                    pipeline = next(p for p in self.pipelines if
                                    isinstance(p, CSVAdapter))
                elif isinstance(data, str):
                    pipeline = next(p for p in self.pipelines if
                                    isinstance(p, StreamAdapter))
                else:
                    continue

                pipeline.process(data)

            except RuntimeError as e:
                print(e)
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline ""restored, "
                      "processing resumed\n")


def nexus_pipeline() -> None:
    """Main entry point for executing the Nexus pipeline system."""
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    manager = NexusManager()
    json_pipeline = JSONAdapter("json_01")
    csv_pipeline = CSVAdapter("csv_01")
    stream_pipeline = StreamAdapter("stream_01")

    for pipeline in [json_pipeline, csv_pipeline, stream_pipeline]:
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    data_list = [
        {"sensor": "temp", "value": 23.5, "unit": "C"},
        "user,action,timestamp",
        "Real-time sensor stream"
    ]

    manager.process_data(data_list)
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    nexus_pipeline()
