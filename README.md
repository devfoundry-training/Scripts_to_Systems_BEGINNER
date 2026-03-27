# From Scripts to Systems

**Python Application Architecture for Instrument Control**

A 3-day beginner track for engineers without a Python background. Takes you from script-level code through to structured, testable instrument control systems.

---

## Structure

```
slides/               Presentation decks
  Day1_Script_to_Architecture.pptx             (38 slides)
  Day2_Python_Foundations_and_Functions.pptx    (54 slides)
  Day3_ABC_Patterns_and_Instrumentation.pptx   (49 slides)
tasks/                Tiered exercises — work through these during the course
  day2_tasks.py       10 tasks covering Python fundamentals
  day3_tasks.py       6 tasks + capstone covering patterns & instrumentation
solutions/            Reference solutions — check your work after each task
  day2_solutions.py
  day3_solutions.py
```

---

## Prerequisites

- Python 3.10+
- A text editor or IDE (VS Code recommended)
- No hardware required — all instrument examples use simulators
- No additional packages needed for Day 2
- Day 3 references `pyserial` but exercises use simulated instruments

---

## Day 1 — From Script to Architecture

Why scripts break, and how to fix them with objects, classes, and patterns.

| Topic | What You'll Learn |
|-------|-------------------|
| Why Scripts Break | Global state, tight coupling, the "200-line wall" |
| OOP from Scratch | Classes, `__init__`, `self`, state and responsibility |
| Composition vs Inheritance | When to use each, how to combine objects |
| Seams & Refactoring | Finding the cut points in messy code |
| Adapter Pattern (intro) | Making hardware swappable via an ABC interface |
| Strategy Pattern (intro) | Making measurement modes swappable |

Day 1 is slide-based with 4 progressive labs (refactoring messy scripts into clean classes). No task file — work directly from the lab instructions in the slides.

---

## Day 2 — Python Foundations & Functions

Covers the Python building blocks needed before tackling architecture patterns.

| Topic | What You'll Learn |
|-------|-------------------|
| Data Types | `int`, `float`, `str`, `bool`, type conversion, f-strings |
| Collections | Lists, dicts, tuples, sets — when to use each |
| Control Flow | `if`/`elif`/`else`, `for`/`while` loops, `break`/`continue` |
| Comprehensions | List and dict comprehensions as Pythonic shorthand |
| Functions | `def`, parameters, defaults, type hints, docstrings |
| `*args` / `**kwargs` | Flexible arguments, unpacking, star expressions |
| Scope & Closures | Local vs global, LEGB rule, closures for capturing state |
| Lambda & HOF | Anonymous functions, `map`/`filter`/`sorted` with keys |
| Decorators | `@timer`, `@log_call`, `functools.wraps`, stacking |
| Error Handling | `try`/`except`/`finally`, custom exceptions, exception chaining |

### Tasks (Day 2)

Open `tasks/day2_tasks.py` and work through the exercises. Each task corresponds to a topic above. Check your work against `solutions/day2_solutions.py`.

---

## Day 3 — ABC, Patterns & Instrumentation

Applies Day 2 foundations to real instrument control patterns. Starts with a catch-up on decorators and error handling if those weren't fully covered on Day 2.

| Topic | What You'll Learn |
|-------|-------------------|
| Catch-up | Decorators + error handling essentials (if needed from Day 2) |
| Abstract Base Classes | `@abstractmethod`, contracts, abstract `@property` |
| Instrumentation | Serial/SCPI communication, request-response pattern |
| Adapter Pattern | ABC + `SimulatedAdapter` + `SerialAdapter` — swappable hardware |
| Strategy Pattern | Measurement modes: single-shot, averaging, max |
| DataSink Pattern | CSV, print, and composite sinks for flexible output |
| Capstone | Mini data acquisition system wiring everything together |

### Tasks (Day 3)

Open `tasks/day3_tasks.py` and work through the exercises. The capstone at the end ties all the patterns together into one working system.

---

## How the Exercises Work

Every task uses a three-tier model. Start at the tier that matches your experience and move up if you finish early.

| Tier | Slides Colour | Who It's For |
|------|---------------|-------------|
| **Beginner** | Teal | New to Python — guided steps, core concepts |
| **Intermediate** | Blue | Some experience — less scaffolding, deeper understanding |
| **Advanced** | Yellow | Experienced — internals, edge cases, design patterns |

---

## Key Principle

> "The controller does not care whether the instrument is real or simulated, whether the data goes to CSV or JSON, or whether we measure once or average a hundred readings."

By the end of Day 3, you'll have built a system where every component is swappable:
- **Adapter** abstracts the hardware — swap `SimulatedAdapter` for `SerialAdapter` without changing the controller
- **Strategy** abstracts measurement modes — swap `SingleShot` for `Averaging` in one line
- **DataSink** abstracts output — swap `PrintSink` for `CsvSink` or use both via `CompositeSink`

---

## What Comes Next

After completing this beginner track, the next step is the advanced **From Scripts to Systems** course, which builds on these patterns to create a full desktop application with PySide6, threading, real-time plotting, and configuration management.

---

## Need Help?

Ask your instructor, or check `solutions/` to compare your approach.
