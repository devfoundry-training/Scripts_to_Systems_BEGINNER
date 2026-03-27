"""
=============================================================================
 DAY 2 TASKS — Python Foundations & Functions
 From Scripts to Systems: Python Application Architecture
=============================================================================
 Work through each task after the corresponding lecture section.
 Each task builds on the previous one, so keep your code!

 Tasks are split into three tiers:
   ▸ BEGINNER       — Core concepts, guided steps
   ▸ INTERMEDIATE   — Less scaffolding, deeper understanding
   ▸ ADVANCED        — Python internals, edge cases, patterns

 Start at the tier that matches your experience. If you finish early,
 move up! All tiers use the same sensor/instrumentation context.
=============================================================================
"""

# ─────────────────────────────────────────────────────────────
# TASK 1: Data Types (10 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Create variables for:
#      - temperature (22.5)
#      - channel name ("TEMP_CH1")
#      - sample count (100)
#      - is_connected (True)
#
#   2. Print the type of each variable using type()
#
#   3. Format a status message using an f-string:
#      "TEMP_CH1: 22.5C (100 samples, connected)"
#
# ▸ INTERMEDIATE
#   4. Convert the temperature to int — what value do you get?
#      Why doesn't it round to 23? (Hint: int() truncates)
#
#   5. Convert sample_count to float, then to str.
#      Use isinstance() to verify each conversion:
#      print(isinstance(sample_count, float))  # True or False?
#
#   6. Try float("hello") — what exception do you get?
#      Now try float("  22.5  ") — does whitespace matter?
#
# ▸ ADVANCED
#   7. Import sys. Use sys.getsizeof() to compare sizes of:
#      int(0), int(10**100), float(22.5), "TEMP_CH1", True
#      Why is a bool the same size as an int?
#
#   8. Print 0.1 + 0.2 == 0.3 — what do you get? Why?
#      Now try: round(0.1 + 0.2, 1) == 0.3
#      Explore sys.float_info.epsilon — what is it for?
#
#   9. Check sys.maxsize. Can Python integers exceed it?
#      Try: x = 10 ** 1000; print(type(x))
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 2: Collections (10 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Create a list of 10 temperature readings (include duplicates)
#
#   2. Use a set to find the unique readings.
#      How many duplicates were there?
#
#   3. Create a dict mapping channel names to their latest reading:
#      {"TEMP_1": 22.5, "TEMP_2": 23.1, "VOLT_1": 3.31}
#
#   4. Loop through the dict and print each channel and its value
#
# ▸ INTERMEDIATE
#   5. Use .get() with a default: channels.get("TEMP_99", "N/A")
#      Why is this safer than channels["TEMP_99"]?
#
#   6. Merge two dicts using |:
#      new_readings = {"TEMP_3": 24.0, "VOLT_2": 3.28}
#      merged = channels | new_readings
#
#   7. Create a tuple for immutable config: config = (9600, 8, "N", 1)
#      Try to change config[0] — what happens?
#
# ▸ ADVANCED
#   8. Create a = [1, 2, 3]. Set b = a. Append 4 to b.
#      Print a. What happened? Why?
#      Fix it with: b = a.copy() or b = a[:]
#
#   9. Now try with nested lists:
#      import copy
#      a = [[1, 2], [3, 4]]
#      b = copy.copy(a)       # shallow copy
#      b[0].append(99)
#      print(a)               # What happened to a?
#
#  10. Fix the nested case with copy.deepcopy().
#      When does shallow vs deep copy matter in practice?
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 3: Control Flow (10 min)
# ─────────────────────────────────────────────────────────────
# Given:
sensor_readings = [22.1, 23.5, -1.0, 48.2, 55.0, 22.0, 21.5, 22.8]

#
# ▸ BEGINNER
#   1. Loop through with enumerate(). Print "Sample {i}: {value}C"
#
#   2. Add a break: if any reading > 50, print an ALARM and stop
#
#   3. Add a continue: skip negative readings (don't process them)
#
#   4. Count how many readings were "normal" (0-50 range)
#
# ▸ INTERMEDIATE
#   5. Categorise each reading into ranges and count them:
#      - "cold":    < 10
#      - "normal":  10-40
#      - "warning": 40-50
#      - "alarm":   > 50
#      Print a summary: {"cold": 0, "normal": 5, "warning": 1, ...}
#
#   6. Use a while loop to simulate retrying a connection.
#      Try up to 3 times. On the 3rd attempt, "succeed".
#      Print each attempt number.
#
# ▸ ADVANCED
#   7. Create two lists:
#      temps = [22.1, 23.5, 21.8]
#      volts = [3.31, 3.28, 3.35]
#      Use zip() to loop through both together:
#      "Channel 0: 22.1C, 3.31V"
#
#   8. Use a for/else construct: loop through readings looking
#      for one > 50. If found, print "ALARM" and break.
#      If the loop completes without breaking, print "All clear".
#
#   9. from itertools import islice
#      Use islice(sensor_readings, 3) to process only the first 3.
#      When would you use this instead of sensor_readings[:3]?
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 4: Comprehensions (10 min)
# ─────────────────────────────────────────────────────────────
# Given:
readings = [22.1, -1.0, 23.5, 999.9, 21.8, -5.0, 24.2]

#
# ▸ BEGINNER
#   1. Use a list comprehension to filter out negative values
#      valid = [r for r in readings if ...]
#
#   2. Use a list comprehension to flag readings > 100 as "ERROR",
#      otherwise keep the number: [22.1, "ERROR", 23.5, ...]
#
# ▸ INTERMEDIATE
#   3. Build a dict: {index: reading} for valid readings only (0-100)
#      Hint: {i: r for i, r in enumerate(readings) if ...}
#
#   4. Use a set comprehension to get unique whole-number values:
#      {round(r) for r in readings if ...}
#
#   5. What's the average of the valid readings?
#      (Hint: sum() and len() work on lists)
#
# ▸ ADVANCED
#   6. Compare a list comprehension vs a generator expression:
#      big_list = [x**2 for x in range(1_000_000)]
#      big_gen  = (x**2 for x in range(1_000_000))
#      Use sys.getsizeof() on both. What's the difference?
#
#   7. Use any() and all() with generator expressions:
#      any(r > 100 for r in readings)   # Are there any errors?
#      all(r >= 0 for r in readings)    # Are all readings valid?
#
#   8. Walrus operator — filter AND capture in one pass:
#      cleaned = [clean for r in readings
#                 if (clean := round(r, 1)) >= 0]
#      Why is this useful? When would you avoid it?
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 5: Functions Basics (10 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Write parse_reading(raw: str) -> float
#      Input: "TEMP:22.5C"  Output: 22.5
#      Input: "VOLT:3.31V"  Output: 3.31
#      (Hint: split on ":", then strip the last character)
#
#   2. Write is_valid(value, min_val=0.0, max_val=100.0) -> bool
#      Test with: is_valid(22.5), is_valid(-1.0), is_valid(22.5, max_val=25)
#
# ▸ INTERMEDIATE
#   3. Write summarise(readings: list) -> tuple
#      Return (count, min, max, average) for a list of readings
#
#   4. Call summarise with [22.1, 23.5, 21.8, 22.0] and unpack:
#      count, lo, hi, avg = summarise(data)
#
#   5. What happens if you call summarise([])? (empty list)
#      How would you handle this gracefully?
#
# ▸ ADVANCED
#   6. Mutable default argument trap:
#      def add_reading(value, readings=[]):
#          readings.append(value)
#          return readings
#      Call add_reading(1), then add_reading(2). What's in the list?
#      Why? How do you fix it? (Hint: use None as default)
#
#   7. Python is "pass by object reference". Prove it:
#      def modify(data): data.append(99)
#      my_list = [1, 2, 3]
#      modify(my_list)
#      print(my_list)   # What do you see?
#
#   8. Now try rebinding vs mutating:
#      def rebind(data): data = [99]
#      my_list = [1, 2, 3]
#      rebind(my_list)
#      print(my_list)   # Different result! Why?
#      Use id() before and after to see what's happening.
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 6: *args & **kwargs (10 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Write log_readings(*readings) that prints each reading
#      with its index. Handle the empty case gracefully.
#
#   2. Create a list: data = [22.1, 23.5, 21.8]
#      Pass it to log_readings using unpacking: log_readings(*data)
#
# ▸ INTERMEDIATE
#   3. Write configure_sensor(**settings) that prints each
#      setting as "key = value". If no settings, print "No settings".
#
#   4. Create a dict: config = {"baud": 9600, "timeout": 2}
#      Pass it using unpacking: configure_sensor(**config)
#
#   5. Write record_batch(sensor_name, *readings) that prints
#      the sensor name, count, and average of the readings.
#
# ▸ ADVANCED
#   6. Write a dispatch() function:
#      def dispatch(command, *args, **kwargs):
#          # If command == "read", call read_sensor(*args)
#          # If command == "config", call configure_sensor(**kwargs)
#          # Otherwise, print "Unknown command"
#
#   7. What is the required argument order in a function signature?
#      def f(pos, /, normal, *args, kw_only, **kwargs): ...
#      Call f with different argument combinations to understand it.
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 7: Scope & Closures (10 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. PREDICT THE OUTPUT (don't run — think first!):
#      x = 10
#      def change(): x = 20; print(x)
#      change(); print(x)
#      # What prints? _______, _______
#
#   2. Now add "global x" inside change(). What changes?
#
# ▸ INTERMEDIATE
#   3. Write make_converter(factor) that returns a converter function.
#      celsius_to_f = make_converter(1.8)  # remembers factor=1.8
#      print(celsius_to_f(100))            # should print 180.0
#
#   4. Write make_threshold_checker(limit) that returns a function
#      checking if a reading exceeds the limit.
#      is_overheating = make_threshold_checker(50.0)
#      print(is_overheating(55.0))   # True
#      print(is_overheating(22.0))   # False
#
# ▸ ADVANCED
#   5. Late-binding closure bug:
#      funcs = [lambda: i for i in range(3)]
#      print([f() for f in funcs])  # Expected [0, 1, 2] — what do you get?
#      Fix it: funcs = [lambda i=i: i for i in range(3)]
#      Why does the default argument fix work?
#
#   6. Use nonlocal to modify an enclosing variable:
#      def make_counter():
#          count = 0
#          def increment():
#              nonlocal count
#              count += 1
#              return count
#          return increment
#
#   7. Explain the LEGB rule: Local, Enclosing, Global, Built-in.
#      Write code that demonstrates each scope level.
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 8: Lambda & Higher-Order Functions (10 min)
# ─────────────────────────────────────────────────────────────
# Given:
temps_c = [22.1, 23.5, 21.8, 24.0, 19.5, 25.2]

#
# ▸ BEGINNER
#   1. Use map() with a lambda to convert all to Fahrenheit (C * 9/5 + 32)
#      temps_f = list(map(lambda c: ..., temps_c))
#
#   2. Use filter() with a lambda to keep only readings between 20-25C
#
# ▸ INTERMEDIATE
#   3. Do both #1 and #2 using comprehensions instead. Which is cleaner?
#
#   4. Sort this list by the second element (the value):
#      data = [("TEMP", 22.5), ("VOLT", 3.3), ("TEMP", 21.0)]
#      sorted_data = sorted(data, key=lambda x: x[1])
#
# ▸ ADVANCED
#   5. Use functools.reduce to find the product of [2, 3, 4, 5]:
#      import functools
#      product = functools.reduce(lambda a, b: a * b, [2, 3, 4, 5])
#
#   6. Use functools.partial to create a pre-configured function:
#      from functools import partial
#      to_fahrenheit = partial(lambda c, offset: c * 9/5 + offset, offset=32)
#      print(to_fahrenheit(100))  # 212.0
#
#   7. Write compose(f, g) that returns a new function h(x) = f(g(x)):
#      double = lambda x: x * 2
#      add_one = lambda x: x + 1
#      double_then_add = compose(add_one, double)
#      print(double_then_add(5))  # 11
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 9: Decorators (15 min)
# ─────────────────────────────────────────────────────────────
import functools

#
# ▸ BEGINNER
#   1. Write a simple decorator that prints "Before" and "After":
#      def my_decorator(func):
#          def wrapper():
#              print("Before")
#              func()
#              print("After")
#          return wrapper
#
#   2. Apply it to a simple function:
#      @my_decorator
#      def say_hello():
#          print("Hello!")
#      say_hello()  # Should print Before, Hello!, After
#
# ▸ INTERMEDIATE
#   3. Write a @log_call decorator that handles any function:
#      - Use functools.wraps to preserve function metadata
#      - Accept *args and **kwargs
#      - Print: "Calling {name} with args={args} kwargs={kwargs}"
#      - Print: "  {name} returned {result}"
#
#   4. Apply @log_call to your parse_reading function from Task 5
#      Call parse_reading("TEMP:22.5C") and check the output
#
#   5. Apply @log_call to your is_valid function. Call with:
#      is_valid(22.5)  and  is_valid(22.5, max_val=25.0)
#      Notice how it logs the different argument styles
#
# ▸ ADVANCED
#   6. Write a parameterised decorator @repeat(n) that calls
#      the function n times:
#      @repeat(3)
#      def greet(name): print(f"Hello {name}!")
#      greet("Alice")  # prints 3 times
#      (Hint: you need THREE levels of nesting)
#
#   7. Stack @log_call and @timer on the same function.
#      import time
#      In what order do they execute? Why?
#
#   8. Write @validate_range(min_val, max_val) that checks
#      the return value of a function is in range, raising
#      ValueError if not.
#
# ─────────────────────────────────────────────────────────────

# Your code here:




# ─────────────────────────────────────────────────────────────
# TASK 10: Error Handling (15 min)
# ─────────────────────────────────────────────────────────────
#
# ▸ BEGINNER
#   1. Use try/except to handle a ValueError:
#      try:
#          value = float("hello")
#      except ValueError as e:
#          print(f"Bad data: {e}")
#
#   2. Add a finally block that prints "Cleanup complete"
#      regardless of whether the conversion succeeded or failed.
#
#   3. Try converting these and handle each case:
#      "22.5" (should work), "hello" (ValueError), None (TypeError)
#
# ▸ INTERMEDIATE
#   4. Create a custom SensorError exception class:
#      class SensorError(Exception): pass
#
#   5. Update your parse_reading(raw) function to:
#      - Catch ValueError if float() fails (bad data)
#      - Catch IndexError if split() gives wrong parts (bad format)
#      - Raise SensorError with a helpful message in both cases
#
#   6. Add range validation: if value < -40 or value > 200,
#      raise SensorError(f"Out of range: {value}")
#      Test with: "TEMP:22.5C", "GARBAGE", "TEMP:999.9C"
#
# ▸ ADVANCED
#   7. Build an exception hierarchy:
#      class SensorError(Exception): pass
#      class ReadingError(SensorError): pass
#      class FormatError(SensorError): pass
#      class RangeError(SensorError): pass
#      Use the right subclass for each error case.
#      Catch SensorError to handle all of them.
#
#   8. Use exception chaining with raise ... from ...:
#      try:
#          float("bad")
#      except ValueError as e:
#          raise ReadingError("Could not parse") from e
#      What extra info does this give in the traceback?
#
#   9. Write a context manager for sensor connections:
#      class SensorConnection:
#          def __enter__(self): print("Connected"); return self
#          def __exit__(self, *args): print("Disconnected")
#      with SensorConnection() as conn: ...
#
# ─────────────────────────────────────────────────────────────

# Your code here:


