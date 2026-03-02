# Cache Simulator

## Overview

This project is a **cache and memory simulator** written in Python.  
It simulates CPU memory access using a cache with configurable parameters, supporting:

- Direct mapping / set-associative cache
- LRU replacement policy
- Page-based memory access

The simulator tracks **cache hits and misses** and simulates memory accesses.

## Features

- Configurable **RAM size**, **page size**, **cache size**, **lines per set**
- Tracks **hits, misses, and memory accesses**
- Implements **LRU replacement**
- Generates **trace logs** for memory accesses
- **Line chart visualization** of cache hit ratio

## Project Structure
```
cache_simulator/
│
├── main.py # Simulation entry point
├── memory.py # Memory class 
├── cache.py # Cache class with LRU replacement
├── utils.py # Helper functions: generate addresses, log, stats, graphs
├── log.tsx # Trace log file (generated during simulation)
└── README.md
```

## Classes

### `Memory`
Simulates main memory as a dictionary of pages.

- memory.pages = { page_num: [0] * page_size }

- access(address) → reads data at given address

- page-based memory for bytes, KB, or MB simulation

### `Cache`

Simulates the CPU cache with set-associative or direct-mapped policy.

- Stores cache lines with attributes:

  - valid, tag, last_used, data

- Handles cache hits and misses

- Implements LRU hybrid replacement


## How to Run

### 1. Clone repository:
```
@git clone https://github.com/yourusername/cache-simulator.git
cd cache-simulator
```

### 2. Run simulation:

```
python3 main.py
```

### 3. Input parameters when prompted:


- RAM size (in bytes, KB, or MB depending on page_size)

- Page size (number of bytes per page)

- Cache size (number of lines)

- Lines per set

- Number of reads 

### 4. Simulation outputs:

- Trace log in `log.tsx`

- Cache hit ratio line chart over time

## Authors

Brandon Warnke  
Kaede Saho

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
