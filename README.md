# From Scripts to Systems — Student Materials

**Python Application Architecture for Instrument Control**

Welcome to the course. This repository contains everything you need for the 3-day training.

## Setup

```bash
# 1. Install Python dependencies
pip install PySide6 pyqtgraph pyserial pint PyYAML numpy

# 2. Verify your setup
python smoke_test.py
```

All checks should show `OK`. If any fail, ask your instructor.

## What's Here

```
labmonitor/         The course project (instrument-control application)
examples/           Starter scripts for Labs 1 and 2
labs/               Lab instructions and starter skeletons
slides/             Course slide decks (Days 1-3)
docs/               Simulator reference guide
smoke_test.py       Environment check script
```

## Running the Application

```bash
cd labmonitor
python main.py
```

Connect, Start, and watch live temperature and voltage data from the simulated instrument.

## Labs

| Lab | Title | Day | Starter File |
|-----|-------|-----|-------------|
| 1 | From Script to Classes | 1 | `examples/messy_script.py` |
| 2 | Refactor the Messy Driver | 1 | `examples/messy_driver.py` |
| 3 | Build the Adapter | 1 | `labmonitor/drivers/simulated.py` |
| 4 | Implement Strategies | 1 | `labmonitor/core/strategies.py` |
| 5 | Worker Thread | 2 | `labs/lab05_starter.py` |
| 6 | Mini-App Build | 2 | `labmonitor/` (full project) |
| 7 | Implement DataSinks | 3 | `labmonitor/core/data_sink.py` |
| 8 | Writer Thread | 3 | `labmonitor/core/writer_thread.py` |
| 9 | Configuration and Metadata | 3 | `labmonitor/configs/default_config.yaml` |
| 10 | Real-Time Plot | 3 | `labs/lab10_starter.py` |

Each lab has an instruction file in `labs/` (e.g. `labs/lab01_instructions.md`).

## Simulator

No hardware required. The simulator generates realistic instrument data. See `docs/simulator_guide.md` for commands, channels, and error modes.

## Need Help?

Ask your instructor.
