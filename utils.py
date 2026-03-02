import random
import matplotlib.pyplot as plt

def generate_addresses(ram_size, num_accesses):
    return [random.randint(0, ram_size - 1) for _ in range(num_accesses)]


def create_log_file(trace_file):
    with open(trace_file, 'w') as f:
        pass

def log(trace_file, time, address, hit):
    with open(trace_file, "a") as f:
        f.write(f"{time},{address},{hit}\n")
        
def stats(num_accesses, hits):
    hit_ratio = hits / num_accesses
    miss_ratio = 1 - hit_ratio
    return [hit_ratio, miss_ratio]

def line_graph(time, data):
    plt.plot(time, data)
    plt.ylabel("Hits")
    plt.xlabel("Time")
    plt.title("Cache Hit Ratio Over Time")
    plt.show()