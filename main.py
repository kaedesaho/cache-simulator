from utils import generate_addresses, log, stats, bar_graph
from memory import Memory
from cache import Cache

trace_file = "/log.tsx"

ram_size = int(input("Enter a RAM size: "))
page_size = int(input("Enter a Page size: "))
cache_size = int(input("Enter a cache size: "))
lines_per_set = int(input("Enter a number of lines per set: "))
num_sets = cache_size // lines_per_set

num_reads = int(input("Enter a number of reads: "))
num_writes = int(input("Enter a number of writes: "))
num_accesses = num_reads + num_writes

memory = Memory(ram_size, page_size)
cache = Cache(num_sets, lines_per_set, page_size)

access_pattern = generate_addresses(ram_size, num_accesses)

hits = 0
time_stamp = 0
for address in access_pattern:
    time_stamp += 1
    page_num = address // page_size
    hit = cache.access(page_num)
    if hit:
        hits += 1
        
    log(trace_file, pid, time_stamp, address, hit)


ratio = stats(num_accesses, hits)
bar_graph(ratio)


