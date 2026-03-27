"""
=============================================================================
 DAY 2 SOLUTIONS — Python Foundations & Functions
 From Scripts to Systems: Python Application Architecture
=============================================================================
 TRAINER USE ONLY — Do not distribute to students.
 Solutions for all three tiers (Beginner / Intermediate / Advanced).
=============================================================================
"""

# ─────────────────────────────────────────────────────────────
# TASK 1 SOLUTIONS: Data Types
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
temperature = 22.5
channel_name = "TEMP_CH1"
sample_count = 100
is_connected = True
print(type(temperature))   # <class 'float'>
print(type(channel_name))  # <class 'str'>
print(type(sample_count))  # <class 'int'>
print(type(is_connected))  # <class 'bool'>
msg = f"{channel_name}: {temperature}C ({sample_count} samples, {'connected' if is_connected else 'disconnected'})"

# ▸ INTERMEDIATE
print(int(22.5))           # 22 — truncates, doesn't round!
x = float(sample_count)    # 100.0
print(isinstance(x, float)) # True
# float("hello") → ValueError
# float("  22.5  ") → 22.5 (whitespace is stripped)

# ▸ ADVANCED
import sys
print(sys.getsizeof(0))           # 28
print(sys.getsizeof(10**100))     # 72
print(sys.getsizeof(22.5))        # 24
print(sys.getsizeof("TEMP_CH1"))  # 57
print(sys.getsizeof(True))        # 28 (bool IS int!)
print(0.1 + 0.2 == 0.3)           # False
print(round(0.1 + 0.2, 1) == 0.3) # True
print(sys.maxsize)                 # 9223372036854775807
x = 10 ** 1000; print(type(x))    # <class 'int'> — no overflow!


# ─────────────────────────────────────────────────────────────
# TASK 2 SOLUTIONS: Collections
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
readings = [22.1, 22.3, 22.0, 22.5, 22.3, 22.1, 22.7, 22.0, 23.1, 22.5]
unique = set(readings)
print(f"Duplicates: {len(readings) - len(unique)}")
channels = {"TEMP_1": 22.5, "TEMP_2": 23.1, "VOLT_1": 3.31}
for name, value in channels.items():
    print(f"{name}: {value}")

# ▸ INTERMEDIATE
print(channels.get("TEMP_99", "N/A"))  # "N/A" — no KeyError
new_readings = {"TEMP_3": 24.0, "VOLT_2": 3.28}
merged = channels | new_readings
config = (9600, 8, "N", 1)
# config[0] = 115200  → TypeError: tuples are immutable

# ▸ ADVANCED
import copy
a = [1, 2, 3]; b = a; b.append(4)
print(a)  # [1, 2, 3, 4] — both point to same list!
b = a.copy(); b.append(5)
print(a)  # [1, 2, 3, 4] — safe now

a = [[1, 2], [3, 4]]
b = copy.copy(a); b[0].append(99)
print(a)  # [[1, 2, 99], [3, 4]] — shallow copy shares inner lists!
b = copy.deepcopy(a)  # truly independent copy


# ─────────────────────────────────────────────────────────────
# TASK 3 SOLUTIONS: Control Flow
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
sensor_readings = [22.1, 23.5, -1.0, 48.2, 55.0, 22.0, 21.5, 22.8]
normal_count = 0
for i, r in enumerate(sensor_readings):
    if r < 0:
        continue
    if r > 50:
        print(f"ALARM at sample {i}: {r}C!")
        break
    print(f"Sample {i}: {r}C")
    if 0 <= r <= 50:
        normal_count += 1
print(f"Normal readings: {normal_count}")

# ▸ INTERMEDIATE
categories = {"cold": 0, "normal": 0, "warning": 0, "alarm": 0}
for r in sensor_readings:
    if r < 0: continue
    elif r < 10: categories["cold"] += 1
    elif r <= 40: categories["normal"] += 1
    elif r <= 50: categories["warning"] += 1
    else: categories["alarm"] += 1
print(categories)

attempts = 0
while attempts < 3:
    attempts += 1
    print(f"Attempt {attempts}...")
    if attempts == 3:
        print("Connected!")
        break

# ▸ ADVANCED
temps = [22.1, 23.5, 21.8]
volts = [3.31, 3.28, 3.35]
for i, (t, v) in enumerate(zip(temps, volts)):
    print(f"Channel {i}: {t}C, {v}V")

for r in sensor_readings:
    if r > 50:
        print(f"ALARM: {r}C!"); break
else:
    print("All clear")

from itertools import islice
for r in islice(sensor_readings, 3):
    print(r)


# ─────────────────────────────────────────────────────────────
# TASK 4 SOLUTIONS: Comprehensions
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
readings = [22.1, -1.0, 23.5, 999.9, 21.8, -5.0, 24.2]
positive = [r for r in readings if r >= 0]
flagged = [r if r <= 100 else "ERROR" for r in readings]

# ▸ INTERMEDIATE
valid_dict = {i: r for i, r in enumerate(readings) if 0 <= r <= 100}
unique_rounded = {round(r) for r in readings if 0 <= r <= 100}
valid = [r for r in readings if 0 <= r <= 100]
avg = sum(valid) / len(valid)

# ▸ ADVANCED
big_list = [x**2 for x in range(1_000_000)]
big_gen = (x**2 for x in range(1_000_000))
print(sys.getsizeof(big_list))  # ~8 MB
print(sys.getsizeof(big_gen))   # ~200 bytes

print(any(r > 100 for r in readings))  # True
print(all(r >= 0 for r in readings))   # False

cleaned = [clean for r in readings if (clean := round(r, 1)) >= 0]


# ─────────────────────────────────────────────────────────────
# TASK 5 SOLUTIONS: Functions Basics
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
def parse_reading(raw: str) -> float:
    parts = raw.split(":")
    return float(parts[1][:-1])

def is_valid(value, min_val=0.0, max_val=100.0) -> bool:
    return min_val <= value <= max_val

# ▸ INTERMEDIATE
def summarise(readings: list) -> tuple:
    if not readings:
        return (0, None, None, None)
    return (len(readings), min(readings), max(readings),
            sum(readings) / len(readings))

count, lo, hi, avg = summarise([22.1, 23.5, 21.8, 22.0])

# ▸ ADVANCED
# Mutable default trap:
def add_reading(value, readings=[]):
    readings.append(value)
    return readings
print(add_reading(1))  # [1]
print(add_reading(2))  # [1, 2] — same list!

# Fix:
def add_reading_fixed(value, readings=None):
    readings = readings if readings is not None else []
    readings.append(value)
    return readings

# Pass by object reference:
def modify(data): data.append(99)
my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # [1, 2, 3, 99]

def rebind(data): data = [99]
my_list = [1, 2, 3]
rebind(my_list)
print(my_list)  # [1, 2, 3] — unchanged!


# ─────────────────────────────────────────────────────────────
# TASK 6 SOLUTIONS: *args & **kwargs
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
def log_readings(*readings):
    if not readings:
        print("No readings")
        return
    for i, r in enumerate(readings):
        print(f"  Reading {i}: {r}")

data = [22.1, 23.5, 21.8]
log_readings(*data)

# ▸ INTERMEDIATE
def configure_sensor(**settings):
    if not settings:
        print("No settings")
        return
    for key, value in settings.items():
        print(f"  {key} = {value}")

config = {"baud": 9600, "timeout": 2}
configure_sensor(**config)

def record_batch(sensor_name, *readings):
    print(f"{sensor_name}: {len(readings)} readings, avg={sum(readings)/len(readings):.2f}")

# ▸ ADVANCED
def dispatch(command, *args, **kwargs):
    if command == "read":
        log_readings(*args)
    elif command == "config":
        configure_sensor(**kwargs)
    else:
        print(f"Unknown command: {command}")

# Argument order: def f(pos, /, normal, *args, kw_only, **kwargs)


# ─────────────────────────────────────────────────────────────
# TASK 7 SOLUTIONS: Scope & Closures
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
# Without global: prints 20, then 10
# With global x: prints 20, then 20

# ▸ INTERMEDIATE
def make_converter(factor):
    def convert(value):
        return value * factor
    return convert

celsius_to_f = make_converter(1.8)
print(celsius_to_f(100))  # 180.0

def make_threshold_checker(limit):
    def check(reading):
        return reading > limit
    return check

is_overheating = make_threshold_checker(50.0)
print(is_overheating(55.0))  # True
print(is_overheating(22.0))  # False

# ▸ ADVANCED
# Late-binding bug:
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]

# Fix:
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]

# Counter with nonlocal:
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter(), counter(), counter())  # 1 2 3


# ─────────────────────────────────────────────────────────────
# TASK 8 SOLUTIONS: Lambda & Higher-Order Functions
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
temps_c = [22.1, 23.5, 21.8, 24.0, 19.5, 25.2]
temps_f = list(map(lambda c: c * 9/5 + 32, temps_c))
in_range = list(filter(lambda c: 20 <= c <= 25, temps_c))

# ▸ INTERMEDIATE
temps_f_comp = [c * 9/5 + 32 for c in temps_c]
in_range_comp = [c for c in temps_c if 20 <= c <= 25]
# Comprehensions are cleaner!

data = [("TEMP", 22.5), ("VOLT", 3.3), ("TEMP", 21.0)]
sorted_data = sorted(data, key=lambda x: x[1])

# ▸ ADVANCED
from functools import reduce, partial
product = reduce(lambda a, b: a * b, [2, 3, 4, 5])  # 120
to_f = partial(lambda c, offset: c * 9/5 + offset, offset=32)

def compose(f, g):
    return lambda x: f(g(x))
double = lambda x: x * 2
add_one = lambda x: x + 1
double_then_add = compose(add_one, double)
print(double_then_add(5))  # 11


# ─────────────────────────────────────────────────────────────
# TASK 9 SOLUTIONS: Decorators
# ─────────────────────────────────────────────────────────────
import functools

# ▸ BEGINNER
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # Before, Hello!, After

# ▸ INTERMEDIATE
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned {result}")
        return result
    return wrapper

# ▸ ADVANCED
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Stacking: @log_call @timer means f = log_call(timer(f))
# log_call runs first (outer), timer runs inside


# ─────────────────────────────────────────────────────────────
# TASK 10 SOLUTIONS: Error Handling
# ─────────────────────────────────────────────────────────────

# ▸ BEGINNER
try:
    value = float("hello")
except ValueError as e:
    print(f"Bad data: {e}")
finally:
    print("Cleanup complete")

# ▸ INTERMEDIATE
class SensorError(Exception): pass

def parse_reading_safe(raw: str) -> float:
    try:
        parts = raw.split(":")
        value = float(parts[1][:-1])
    except (ValueError, IndexError) as e:
        raise SensorError(f"Cannot parse '{raw}': {e}") from e
    if not -40 <= value <= 200:
        raise SensorError(f"Out of range: {value}")
    return value

# ▸ ADVANCED
class ReadingError(SensorError): pass
class FormatError(SensorError): pass
class RangeError(SensorError): pass

# Exception chaining:
try:
    float("bad")
except ValueError as e:
    raise ReadingError("Parse failed") from e

# Context manager:
class SensorConnection:
    def __init__(self, name): self.name = name
    def __enter__(self):
        print(f"Connected to {self.name}"); return self
    def __exit__(self, *args):
        print(f"Disconnected from {self.name}")

with SensorConnection("TEMP_1") as conn:
    print("Reading...")
