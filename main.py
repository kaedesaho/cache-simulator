from utils import generate_addresses, create_log_file, log, line_graph
from memory import Memory
from cache import CacheSet

def convert_to_bytes(size, unit):
    unit = unit.lower()
    if unit == 'kb':
        return size * 1024
    elif unit == 'mb':
        return size * 1024 * 1024
    elif unit == 'b':
        return size
    else:
        return ValueError("Invalid Unit")


trace_file = "log.txt"
create_log_file(trace_file)

ram_size = int(input("Enter a RAM size: "))
ram_unit = str(input("Enter a RAM unit(B/KB/MB): "))
page_size = int(input("Enter a Page size: "))
page_unit = str(input("Enter a Page unit(B/KB/MB): "))
cache_size = int(input("Enter a cache size: "))
cache_unit = str(input("Enter a cache unit(B/KB/MB): "))
lines_per_set = int(input("Enter a number of lines per set: "))
#Direct map = lines_per_set = 1
#Fully associative = num_set = 1
#set associative = anything else

ram_size = convert_to_bytes(ram_size, ram_unit)
page_size = convert_to_bytes(page_size, page_unit)
cache_size = convert_to_bytes(cache_size, cache_unit)

num_lines = cache_size // page_size
num_sets = num_lines // lines_per_set

num_reads = int(input("Enter a number of reads: "))
num_writes = int(input("Enter a number of writes: "))
num_accesses = num_reads + num_writes

print("Creating Ram")
memory = Memory(ram_size, page_size)
print("Creating Cache")
cache = CacheSet(num_sets, lines_per_set, page_size)

print("Creating Access Pattern")
access_pattern = generate_addresses(ram_size, num_accesses)
print("Set Up Complete")

hits = 0
time_stamp = 0
time = [0]
info = [0]
for address in access_pattern:
    time_stamp += 1
    time.append(time_stamp)
    page_num = address // page_size
    hit = cache.access(page_num, time_stamp)
    if hit:
        hits += 1
    else:
        data = memory.access(address)
        cache.insert(page_num, data, time_stamp)

    info.append(hits)

    log(trace_file, time_stamp, address, hit)

line_graph(time, info)
