"""
=============================================================================
 DAY 3 SOLUTIONS — ABC, Patterns & Instrumentation
 From Scripts to Systems: Python Application Architecture
=============================================================================
 TRAINER USE ONLY — Do not distribute to students.
 Solutions for all three tiers (Beginner / Intermediate / Advanced).
=============================================================================
"""
import random
from abc import ABC, abstractmethod
from datetime import datetime


# ─────────────────────────────────────────────────────────────
# TASK 1 SOLUTIONS: Build Your ABC Hierarchy
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
class Sensor(ABC):
    def __init__(self, name): self.name = name
    @abstractmethod
    def read(self) -> float: pass
    @abstractmethod
    def calibrate(self) -> None: pass
    def status(self) -> str: return f"{self.name} is active"

class TemperatureSensor(Sensor):
    def read(self): return round(random.uniform(20, 25), 2)
    def calibrate(self): print(f"Calibrating {self.name}")

class VoltageSensor(Sensor):
    def read(self): return round(random.uniform(3.0, 3.5), 3)
    def calibrate(self): print(f"Calibrating {self.name}")

# Sensor("test") -> TypeError!

# ▸ INTERMEDIATE
# In Sensor ABC:
# @property
# @abstractmethod
# def unit(self) -> str: ...

# In TemperatureSensor:
# @property
# def unit(self): return "C"

# In VoltageSensor:
# @property
# def unit(self): return "V"

# Concrete method on ABC:
# def format_reading(self) -> str:
#     return f"{self.name}: {self.read()} {self.unit}"

def take_readings(sensors, count):
    for sensor in sensors:
        readings = [sensor.read() for _ in range(count)]
        print(f"{sensor.name}: avg={sum(readings)/len(readings):.2f}")

# ▸ ADVANCED
class BrokenSensor(Sensor):
    def read(self): return 0.0
    # Missing calibrate() -> TypeError on instantiation

# __init_subclass__ registration (add to Sensor ABC):
# _registry = {}
# def __init_subclass__(cls, **kwargs):
#     super().__init_subclass__(**kwargs)
#     Sensor._registry[cls.__name__] = cls

print(Sensor.__subclasses__())  # [TemperatureSensor, VoltageSensor, ...]
temp = TemperatureSensor("T1")
print(isinstance(temp, Sensor))             # True
print(isinstance(temp, VoltageSensor))      # False
print(issubclass(TemperatureSensor, Sensor)) # True

# Removing unit from VoltageSensor -> TypeError: Can't instantiate abstract class

# Read-only name property:
# @property
# def name(self): return self._name
# In __init__: self._name = name.strip()

# Calibration offset with setter:
# @property
# def calibration_offset(self): return self._offset
# @calibration_offset.setter
# def calibration_offset(self, value):
#     if not isinstance(value, (int, float)):
#         raise TypeError("Offset must be numeric")
#     self._offset = value


# ─────────────────────────────────────────────────────────────
# TASK 2 SOLUTIONS: Mock Serial Conversation
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
def send_command_basic(command):
    if command == "*IDN?":
        return "SimSensor v1.0"
    elif command == "READ:TEMP":
        return str(round(random.uniform(20, 25), 2))
    elif command == "READ:VOLT":
        return str(round(random.uniform(3.0, 3.5), 3))
    else:
        return "ERROR: Unknown command"

# ▸ INTERMEDIATE
class CommandError(Exception): pass

def send_command(command):
    if command == "*IDN?": return "SimSensor v1.0"
    elif command == "READ:TEMP": return str(round(random.uniform(20, 25), 2))
    elif command == "READ:VOLT": return str(round(random.uniform(3.0, 3.5), 3))
    else: raise CommandError(f"Unknown: {command}")

# Conversation loop:
print(send_command("*IDN?"))
for _ in range(5): print(send_command("READ:TEMP"))
try:
    send_command("INVALID")
except CommandError as e:
    print(f"Error: {e}")

# ▸ ADVANCED
commands = {
    "*IDN?": lambda: "SimSensor v1.0",
    "READ:TEMP": lambda: str(round(random.uniform(20, 25), 2)),
    "READ:VOLT": lambda: str(round(random.uniform(3.0, 3.5), 3)),
}
_interval = 1.0  # state
_history = []

def send_command_advanced(cmd):
    _history.append(cmd)
    if len(_history) > 10: _history.pop(0)
    if cmd == "HIST?": return str(_history)
    if cmd.startswith("SET:INTERVAL"):
        global _interval
        _interval = float(cmd.split()[1])
        return "OK"
    handler = commands.get(cmd)
    if handler is None: raise CommandError(f"Unknown: {cmd}")
    return handler()


# ─────────────────────────────────────────────────────────────
# TASK 3 SOLUTIONS: Build the Adapter Pattern
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
class InstrumentAdapter(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def read_temperature(self) -> float: pass
    @abstractmethod
    def read_voltage(self) -> float: pass
    @abstractmethod
    def disconnect(self): pass

class SimulatedAdapter(InstrumentAdapter):
    def connect(self): print("Simulated: connected")
    def read_temperature(self): return round(random.uniform(20, 25), 2)
    def read_voltage(self): return round(random.uniform(3.0, 3.5), 3)
    def disconnect(self): print("Simulated: disconnected")

def run_acquisition(adapter, count):
    adapter.connect()
    try:
        for i in range(count):
            print(f"Reading {i+1}: {adapter.read_temperature()}C")
    finally:
        adapter.disconnect()

# ▸ INTERMEDIATE
class MockSerialAdapter(InstrumentAdapter):
    def connect(self): print("Serial: connected")
    def read_temperature(self): return float(send_command("READ:TEMP"))
    def read_voltage(self): return float(send_command("READ:VOLT"))
    def disconnect(self): print("Serial: disconnected")

# Swap: run_acquisition(MockSerialAdapter(), 5) — ZERO changes to run_acquisition!

# ▸ ADVANCED
def create_adapter(mode):
    if mode == "simulated": return SimulatedAdapter()
    if mode == "serial": return MockSerialAdapter()
    raise ValueError(f"Unknown mode: {mode}")

class AdapterRegistry:
    _adapters = {}
    @classmethod
    def register(cls, name, adapter_cls): cls._adapters[name] = adapter_cls
    @classmethod
    def create(cls, name): return cls._adapters[name]()

# Context manager (add to adapter class):
# def __enter__(self): self.connect(); return self
# def __exit__(self, *args): self.disconnect()


# ─────────────────────────────────────────────────────────────
# TASK 4 SOLUTIONS: Strategy Pattern
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
class MeasurementStrategy(ABC):
    @abstractmethod
    def execute(self, adapter) -> list: pass

class SingleShotStrategy(MeasurementStrategy):
    def execute(self, adapter):
        return [adapter.read_temperature()]

def run_measurement(adapter, strategy):
    adapter.connect()
    try:
        results = strategy.execute(adapter)
        print(f"Results: {results}")
    finally:
        adapter.disconnect()

# ▸ INTERMEDIATE
class AveragingStrategy(MeasurementStrategy):
    def __init__(self, count=10): self.count = count
    def execute(self, adapter):
        readings = [adapter.read_temperature() for _ in range(self.count)]
        return [sum(readings) / len(readings)]

class MaxStrategy(MeasurementStrategy):
    def __init__(self, count=10): self.count = count
    def execute(self, adapter):
        readings = [adapter.read_temperature() for _ in range(self.count)]
        return [max(readings)]

# ▸ ADVANCED
class MedianStrategy(MeasurementStrategy):
    def __init__(self, count=10): self.count = count
    def execute(self, adapter):
        readings = sorted([adapter.read_temperature() for _ in range(self.count)])
        mid = len(readings) // 2
        return [readings[mid]]

class ChainedStrategy(MeasurementStrategy):
    def __init__(self, *strategies): self.strategies = strategies
    def execute(self, adapter):
        results = []
        for s in self.strategies:
            results.extend(s.execute(adapter))
        return results


# ─────────────────────────────────────────────────────────────
# TASK 5 SOLUTIONS: Save & Load Readings
# ─────────────────────────────────────────────────────────────
import csv
import json

# ▸ BEGINNER
adapter = SimulatedAdapter(); adapter.connect()
task5_readings = [adapter.read_temperature() for _ in range(10)]
adapter.disconnect()

with open("readings.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "channel", "value"])
    for r in task5_readings:
        writer.writerow([datetime.now().isoformat(), "TEMP_1", r])

with open("readings.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ▸ INTERMEDIATE
with open("readings.csv") as f:
    reader = csv.DictReader(f)
    values = [float(row["value"]) for row in reader]
    print(f"Min: {min(values)}, Max: {max(values)}, Avg: {sum(values)/len(values):.2f}")

try:
    with open("missing.csv") as f: pass
except FileNotFoundError:
    print("File not found — using defaults")

# ▸ ADVANCED
metadata = {"experiment": "test_run_1", "num_readings": 10,
            "timestamp": datetime.now().isoformat(), "adapter": "SimulatedAdapter"}
with open("metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

from pathlib import Path
data_dir = Path("output"); data_dir.mkdir(exist_ok=True)
csv_path = data_dir / "readings.csv"


# ─────────────────────────────────────────────────────────────
# TASK 6 SOLUTIONS: Build DataSinks
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
class DataSink(ABC):
    @abstractmethod
    def open(self): pass
    @abstractmethod
    def write_reading(self, timestamp, channel, value): pass
    @abstractmethod
    def close(self): pass

class CsvSink(DataSink):
    def __init__(self, filename):
        self.filename = filename; self._file = None; self._writer = None
    def open(self):
        self._file = open(self.filename, "w", newline="")
        self._writer = csv.writer(self._file)
        self._writer.writerow(["timestamp", "channel", "value"])
    def write_reading(self, timestamp, channel, value):
        self._writer.writerow([timestamp, channel, value])
    def close(self):
        if self._file: self._file.close()

class PrintSink(DataSink):
    def open(self): print("--- Start ---")
    def write_reading(self, timestamp, channel, value):
        print(f"  {channel}: {value} at {timestamp}")
    def close(self): print("--- End ---")

# ▸ INTERMEDIATE
class CompositeSink(DataSink):
    def __init__(self, *sinks): self.sinks = sinks
    def open(self):
        for s in self.sinks: s.open()
    def write_reading(self, timestamp, channel, value):
        for s in self.sinks: s.write_reading(timestamp, channel, value)
    def close(self):
        for s in self.sinks: s.close()

# ▸ ADVANCED
class JsonSink(DataSink):
    def __init__(self, filename):
        self.filename = filename; self._records = []
    def open(self): self._records = []
    def write_reading(self, timestamp, channel, value):
        self._records.append({"timestamp": timestamp, "channel": channel, "value": value})
    def close(self):
        with open(self.filename, "w") as f:
            json.dump(self._records, f, indent=2)

# Context manager (add to DataSink or subclass):
# def __enter__(self): self.open(); return self
# def __exit__(self, *args): self.close()


# ─────────────────────────────────────────────────────────────
# CAPSTONE SOLUTIONS: Mini Data Acquisition System
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
def run_experiment_basic(adapter, strategy, sink, cycles):
    adapter.connect(); sink.open()
    for i in range(cycles):
        results = strategy.execute(adapter)
        for value in results:
            sink.write_reading(datetime.now().isoformat(), "TEMP_1", value)
    sink.close(); adapter.disconnect()

# run_experiment_basic(SimulatedAdapter(), SingleShotStrategy(), PrintSink(), 5)

# ▸ INTERMEDIATE
def run_experiment(adapter, strategy, sink, cycles):
    adapter.connect(); sink.open()
    try:
        for i in range(cycles):
            results = strategy.execute(adapter)
            for value in results:
                sink.write_reading(datetime.now().isoformat(), "TEMP_1", value)
            print(f"Cycle {i+1}: {results}")
    finally:
        sink.close(); adapter.disconnect()

# adapter = SimulatedAdapter()
# strategy = AveragingStrategy(count=5)
# sink = CompositeSink(CsvSink("capstone.csv"), PrintSink())
# run_experiment(adapter, strategy, sink, 10)
# Swap: strategy = SingleShotStrategy() — ZERO changes to run_experiment!

# ▸ ADVANCED
def run_experiment_robust(adapter, strategy, sink, cycles):
    adapter.connect(); sink.open()
    try:
        for cycle in range(cycles):
            for attempt in range(3):
                try:
                    results = strategy.execute(adapter)
                    break
                except Exception as e:
                    print(f"Retry {attempt+1}: {e}")
            for value in results:
                sink.write_reading(datetime.now().isoformat(), "TEMP_1", value)
    finally:
        sink.close(); adapter.disconnect()

# Config-driven:
# config = {"adapter": "simulated", "strategy": {"type": "averaging", "count": 5},
#           "sinks": ["csv:capstone.csv", "print"], "cycles": 10}

# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# Replace print() with logger.info()


# ─────────────────────────────────────────────────────────────
# Run tests if executing this file directly
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Uncomment to run unit tests:
    # unittest.main()
    pass
