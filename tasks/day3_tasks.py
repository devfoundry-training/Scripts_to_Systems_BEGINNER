"""
=============================================================================
 DAY 3 TASKS — ABC, Patterns & Instrumentation
 From Scripts to Systems: Python Application Architecture
=============================================================================
 Work through each task after the corresponding lecture section.
 Each task builds on the previous one — keep your code!
 By the end, you'll have a complete mini data acquisition system.

 Tasks are split into three tiers:
   ▸ BEGINNER       — Core concepts, guided steps
   ▸ INTERMEDIATE   — Less scaffolding, deeper understanding
   ▸ ADVANCED        — Python internals, edge cases, patterns

 Start at the tier that matches your experience. If you finish early,
 move up! All tiers use the same sensor/instrumentation context.
=============================================================================
"""
import random
from abc import ABC, abstractmethod
from datetime import datetime


# ─────────────────────────────────────────────────────────────
# TASK 1: Build Your ABC Hierarchy (15 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Create a Sensor ABC (inherit from ABC) with:
#      - __init__(self, name) that stores the name
#      - read() and calibrate() as abstract methods
#      - status() as a concrete method: return f"{self.name} is active"
#
#   2. Create TemperatureSensor(Sensor) — read() returns random 20-25
#      Create VoltageSensor(Sensor) — read() returns random 3.0-3.5
#      Both should implement calibrate() (just print "Calibrated")
#
#   3. Try: sensor = Sensor("test") — what error do you get?
#
# ▸ INTERMEDIATE
#   4. Make unit an abstract @property on the Sensor ABC:
#      @property
#      @abstractmethod
#      def unit(self) -> str: ...
#
#   5. Implement unit as a property in each subclass:
#      @property
#      def unit(self): return "C"  # or "V" for VoltageSensor
#
#   6. Add a concrete format_reading() method to the ABC:
#      def format_reading(self) -> str:
#          return f"{self.name}: {self.read()} {self.unit}"
#      Call it on both sensors — same method, different output!
#
#   7. Write take_readings(sensors: list, count: int) that calls
#      read() on each sensor 'count' times. It works with ANY sensor!
#
# ▸ ADVANCED
#   8. Create a BrokenSensor that only implements read() (not calibrate).
#      Try to instantiate it. Read the error message carefully.
#
#   9. Add __init_subclass__ to Sensor for automatic registration:
#      _registry = {}
#      def __init_subclass__(cls, **kwargs):
#          super().__init_subclass__(**kwargs)
#          Sensor._registry[cls.__name__] = cls
#      Check Sensor._registry after defining your subclasses.
#
#  10. Use isinstance() and issubclass() checks:
#      isinstance(temp, Sensor)       # True
#      isinstance(temp, VoltageSensor) # ?
#      issubclass(TemperatureSensor, Sensor)  # ?
#      Use Sensor.__subclasses__() to list all sensor implementations.
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 2: Mock Serial Conversation (15 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Write a function send_command(command: str) -> str that simulates
#      an instrument responding to commands:
#
#      "*IDN?"       -> "SimSensor v1.0"
#      "READ:TEMP"   -> str(random.uniform(20, 25))
#      "READ:VOLT"   -> str(random.uniform(3.0, 3.5))
#      anything else -> "ERROR: Unknown command"
#
#   2. Test it: print(send_command("*IDN?"))
#      print(send_command("READ:TEMP"))
#
# ▸ INTERMEDIATE
#   3. Create a CommandError custom exception class
#
#   4. Change send_command to raise CommandError for unknown commands
#      instead of returning an error string
#
#   5. Write a conversation loop: send *IDN?, then 5x READ:TEMP,
#      then an invalid command. Handle the CommandError gracefully.
#
# ▸ ADVANCED
#   6. Refactor send_command to use a dispatch dict instead of if/elif:
#      commands = {
#          "*IDN?": lambda: "SimSensor v1.0",
#          "READ:TEMP": lambda: str(random.uniform(20, 25)),
#      }
#      result = commands.get(cmd, lambda: None)()
#
#   7. Add "SET:INTERVAL {value}" support. Store the interval
#      in a variable and return "OK". Use .startswith() to match.
#
#   8. Implement a command history buffer:
#      Keep a list of the last 10 commands sent.
#      Add a "HIST?" command that returns the history.
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 3: Build the Adapter Pattern (20 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Create InstrumentAdapter ABC with abstract methods:
#      connect(), read_temperature() -> float,
#      read_voltage() -> float, disconnect()
#
#   2. Implement SimulatedAdapter — returns random data:
#      read_temperature() -> random.uniform(20, 25)
#      read_voltage() -> random.uniform(3.0, 3.5)
#
#   3. Write run_acquisition(adapter, count) that:
#      - Connects the adapter
#      - Takes 'count' temperature readings and prints them
#      - Disconnects the adapter
#
# ▸ INTERMEDIATE
#   4. Implement MockSerialAdapter — uses your send_command()
#      function from Task 2 as its "instrument":
#      read_temperature() -> float(send_command("READ:TEMP"))
#
#   5. Test: swap SimulatedAdapter for MockSerialAdapter.
#      How many lines of run_acquisition did you change? (Zero!)
#
# ▸ ADVANCED
#   6. Add a factory function:
#      def create_adapter(mode):
#          if mode == "simulated": return SimulatedAdapter()
#          if mode == "serial": return MockSerialAdapter()
#          raise ValueError(f"Unknown mode: {mode}")
#
#   7. Implement an adapter registry:
#      class AdapterRegistry:
#          _adapters = {}
#          @classmethod
#          def register(cls, name, adapter_cls): ...
#          @classmethod
#          def get(cls, name): ...
#      AdapterRegistry.register("sim", SimulatedAdapter)
#      adapter = AdapterRegistry.get("sim")
#
#   8. Add context manager support (__enter__/__exit__):
#      with SimulatedAdapter() as adapter:
#          readings = [adapter.read_temperature() for _ in range(5)]
#      # auto-disconnects on exit
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 4: Strategy Pattern (15 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Create MeasurementStrategy ABC with abstract method:
#      execute(adapter: InstrumentAdapter) -> list[float]
#
#   2. Implement SingleShotStrategy — takes ONE reading, returns [value]
#
#   3. Write run_measurement(adapter, strategy) that connects,
#      executes the strategy, prints results, and disconnects
#
# ▸ INTERMEDIATE
#   4. Implement AveragingStrategy(count=10) — takes 'count' readings,
#      returns [average]
#
#   5. Implement MaxStrategy(count=10) — takes 'count' readings,
#      returns [max_value]
#
#   6. Test with SimulatedAdapter + each of the 3 strategies.
#      Swap strategies by changing ONE line.
#
# ▸ ADVANCED
#   7. Implement MedianStrategy(count=10) — returns [median_value]
#      (Hint: sort the readings and take the middle element)
#
#   8. Implement strategy chaining — run multiple strategies in sequence:
#      class ChainedStrategy(MeasurementStrategy):
#          def __init__(self, *strategies): ...
#          def execute(self, adapter): ...
#      # Returns combined results from all strategies
#
#   9. Make strategies configurable at runtime via a dict:
#      strategy_config = {"type": "averaging", "count": 20}
#      strategy = create_strategy(strategy_config)
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 5: Save & Load Readings (15 min)
# ─────────────────────────────────────────────────────────────
import csv
import json

#
# ▸ BEGINNER
#   1. Use your SimulatedAdapter to take 10 temperature readings
#
#   2. Write them to a CSV file with columns:
#      timestamp, channel, value
#
#   3. Read the CSV back and print each row
#
# ▸ INTERMEDIATE
#   4. Calculate and print: min, max, average from the file data
#
#   5. Handle FileNotFoundError gracefully when reading:
#      try:
#          with open("missing.csv") as f: ...
#      except FileNotFoundError:
#          print("File not found — using defaults")
#
# ▸ ADVANCED
#   6. Write experiment metadata to a JSON file:
#      {"experiment": "test_run_1", "num_readings": 10,
#       "timestamp": "...", "adapter": "SimulatedAdapter"}
#
#   7. Use pathlib.Path instead of string paths:
#      from pathlib import Path
#      data_dir = Path("output")
#      data_dir.mkdir(exist_ok=True)
#      csv_path = data_dir / "readings.csv"
#
#   8. Rewrite your CSV code using csv.DictWriter/DictReader:
#      writer = csv.DictWriter(f, fieldnames=["timestamp", "channel", "value"])
#      writer.writeheader()
#      Compare clarity with the basic csv.writer approach.
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 6: Build DataSinks (15 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Create a DataSink ABC with abstract methods:
#      open(), write_reading(timestamp, channel, value), close()
#
#   2. Implement CsvSink(filename) — writes readings to a CSV file
#
#   3. Implement PrintSink — prints readings to console
#
# ▸ INTERMEDIATE
#   4. Implement CompositeSink(*sinks) — delegates to multiple sinks:
#      class CompositeSink(DataSink):
#          def __init__(self, *sinks): self.sinks = sinks
#          def write_reading(...): for s in self.sinks: s.write_reading(...)
#
#   5. Create: CompositeSink(CsvSink("output.csv"), PrintSink())
#      Write 5 readings through it. Check both console AND file.
#
# ▸ ADVANCED
#   6. Implement JsonSink(filename) that writes readings
#      as a JSON array of objects. Add it to the CompositeSink.
#
#   7. Implement buffered writing — collect N records before flushing:
#      class BufferedSink(DataSink):
#          def __init__(self, inner_sink, buffer_size=5): ...
#          def write_reading(...):
#              self.buffer.append(reading)
#              if len(self.buffer) >= self.buffer_size: self.flush()
#
#   8. Add context manager support (__enter__/__exit__) to DataSink:
#      with CompositeSink(CsvSink("out.csv"), PrintSink()) as sink:
#          sink.write_reading(...)
#      # auto-closes all sinks on exit
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# CAPSTONE TASK: Mini Data Acquisition System (30 min)
# ─────────────────────────────────────────────────────────────
# Build a complete data acquisition pipeline:
#
# ▸ BEGINNER
#   1. Use SimulatedAdapter as your data source
#   2. Use SingleShotStrategy for measurement
#   3. Use PrintSink for output
#   4. Write run_experiment(adapter, strategy, sink, cycles):
#      - Connect the adapter, open the sink
#      - For each cycle: execute strategy, write result to sink
#      - Disconnect adapter, close sink
#   5. Run 5 measurement cycles
#
# ▸ INTERMEDIATE
#   6. Switch to AveragingStrategy(count=5)
#   7. Switch to CompositeSink(CsvSink("capstone.csv"), PrintSink())
#   8. Add try/finally to ensure cleanup happens even if errors occur:
#      try:
#          adapter.connect(); sink.open()
#          for cycle in range(cycles): ...
#      finally:
#          adapter.disconnect(); sink.close()
#   9. Run 10 cycles. Check the CSV file.
#  10. Swap to SingleShotStrategy. Run again.
#      How many lines of run_experiment did you change? (ZERO!)
#
# ▸ ADVANCED
#  11. Add error recovery — retry on failure:
#      for cycle in range(cycles):
#          for attempt in range(3):
#              try:
#                  result = strategy.execute(adapter)
#                  break
#              except Exception as e:
#                  print(f"Retry {attempt+1}: {e}")
#
#  12. Implement a configuration dict that drives the pipeline:
#      config = {
#          "adapter": "simulated",
#          "strategy": {"type": "averaging", "count": 5},
#          "sinks": ["csv:capstone.csv", "print"],
#          "cycles": 10
#      }
#      Write run_from_config(config) that builds and runs everything.
#
#  13. Add logging with the logging module:
#      import logging
#      logging.basicConfig(level=logging.INFO)
#      logger = logging.getLogger(__name__)
#      Replace print() calls with logger.info() / logger.error()
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# Run tests if executing this file directly
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    pass
