# Cache Simulator

## Overview

This project is a **cache and memory simulator** written in Python.  
It simulates CPU memory access using a cache with configurable parameters, supporting:

- Direct mapping / set-associative cache
- LRU/LFU hybrids replacement policy
- Page-based memory access

The simulator tracks **cache hits and misses** and simulates memory accesses.

## Features

- Configurable **RAM size**, **page size**, **cache size**, **lines per set**
- Tracks **hits, misses, and memory accesses**
- Implements **LRU/LFU replacement**
- Supports flexible **memory block size** for performance tuning
- Generates **trace logs** for memory accesses
- Optional **bar graph visualization** of cache hit ratio

## Project Structure
```
cache_simulator/
│
├── main.py # Simulation entry point
├── memory.py # Memory class (page-based)
├── cache.py # Cache class with LRU/LFU replacement
├── utils.py # Helper functions: generate addresses, log, stats, graphs
├── log.tsx # Trace log file (generated during simulation)
└── README.md
```

## Classes

### `Memory`
Simulates main memory as a dictionary of pages.

- memory.pages = { page_num: [0]*page_size }

- access(address) → reads data at given address

- write(address, value) → writes data

- Supports page-based memory for bytes, KB, or GB simulation

### `Cache`

Simulates the CPU cache with set-associative or direct-mapped policy.

- Stores cache lines with attributes:

  - valid, tag, last_used, num_used, dirty, data

- Handles cache hits and misses

- Implements LRU replacement

- Supports write-back with dirty line eviction


### How to Run

1. Clone repository:
```
@git clone https://github.com/yourusername/cache-simulator.git
cd cache-simulator
```

2. Run simulation:

```
python3 main.py
```

3. Input parameters when prompted:


- RAM size (in bytes, KB, or GB depending on page_size)

- Page size (number of bytes per page)

- Cache size (number of lines)

- Lines per set

- Number of reads and writes

4. Simulation outputs:

- Trace log in `log.tsx`

- Cache hit/miss ratio bar graph

- Cache hit ratio over time

## Authors

Brandon Warnke
Kaede Saho

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
