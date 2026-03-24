# Acceleration Calculator

A modular Python utility that computes free-fall dynamics — calculating the time for an object to reach Earth from a given altitude and its resulting terminal velocity, with automated tabular output and file export.

---

## Overview

The **Acceleration Calculator** solves a core kinematics problem: given a set of distances, it determines how long an object in free fall takes to reach the ground and what velocity it attains upon impact. The program iterates over a user-defined range of distances, computes results using standard gravitational acceleration (32.174 ft/s²), and presents the output in a formatted table — both to the console and to a user-specified output file. Velocity is reported in both ft/s and mph for practical interpretation.

## Key Features

- **Free-Fall Time Computation** — Calculates descent time from any specified altitude using the kinematic equation `t = √(2s / g)`.
- **Impact Velocity Calculation** — Derives final velocity at ground contact via `v = g × t`.
- **Dual Unit Output** — Reports velocity in both feet per second (ft/s) and miles per hour (mph).
- **Configurable Distance Range** — Accepts user-defined starting distance, ending distance, and step interval (delta) for batch computation.
- **Formatted Tabular Display** — Outputs results in a clean, aligned table on the console.
- **File Export** — Writes all computed results to a user-named output file for persistence and further analysis.

## Tech Stack

| Component        | Technology      |
|------------------|-----------------|
| Language         | Python 3        |
| Standard Library | `math` (sqrt)   |
| I/O              | Console + File  |

## System Architecture

```
User Input (start, end, delta, filename)
        │
        ▼
┌───────────────────┐
│   Main Loop       │  Iterates over distance range
│   (range iterator) │
└────────┬──────────┘
         │
         ├──► time(s)      →  t = √(2s / g)
         │
         ├──► velocity(t)  →  v = g × t
         │
         ├──► Unit conversion: ft/s → mph
         │
         ├──► Console output (formatted table)
         │
         └──► File output (user-specified filename)
```

**Data Flow:**
1. The user provides a starting distance, ending distance, delta (step size), and an output filename.
2. The program iterates from the starting distance down to the ending distance in decrements of delta.
3. For each distance, it computes the free-fall time and impact velocity using modular helper functions.
4. Results are displayed in a formatted table and simultaneously written to the output file.

## Setup & Installation

### Prerequisites

- **Python 3.6+** installed on your system.

### Run the Program

1. **Clone the repository:**
   ```bash
   git clone https://github.com/samie-mirghani/acceleration-calculator.git
   cd acceleration-calculator
   ```

2. **Execute the script:**
   ```bash
   python "Project 3.py"
   ```

3. **Follow the prompts:**
   - Enter a starting distance in feet (integer values only).
   - Enter an ending distance (must be less than starting distance, integer).
   - Enter the delta / step decrement (integer).
   - Provide a filename for the output file.

### Example

```
Please enter the starting distance:   1000
Please enter the ending distance value:   100
Please enter the value of the delta:   100
Please enter your file name for the output:   results.txt
```

**Sample Output:**

```
Distance        Time      Velocity(ft/sec) Velocity(mph)
 1000.0000       7.8843      253.7398      173.0044
  900.0000       7.4803      240.7418      164.1421
  800.0000       7.0533      226.9986      154.7717
  ...
```

## License

This project is available for educational and personal use.

---

> Built as a practical exercise in applied physics computation and modular Python programming.
