import random
import matplotlib.pyplot as plt



def generate_addresses( page_size, process_reads):
    addresses = []
    for i in range(len(process_reads) - 1):
        page_table = process_reads[i].get_page_table()
        num_reads = process_reads[i].get_num_reads()
        for j in range(len(page_table) - 1):
            if j > len(page_table):
                some_reads = random.randint(0, num_reads)
                num_reads -= some_reads
            elif num_reads == 0:
                break
            else:
                some_reads = num_reads
            start = (page_size * page_table[j]) + 1
            end = (page_size * page_table[j]) + page_size

            for _ in range(some_reads):
                addresses.append(random.randint(start, end))

    return addresses


def create_log_file(trace_file):
    with open(trace_file, 'w') as f:
        pass

def log(trace_file, time, address, hit):
    with open(trace_file, "a") as f:
        f.write(f"{time},{address},{hit}\n")


def line_graph(time, data):
    plt.plot(time, data)
    plt.ylabel("Hits")
    plt.xlabel("Time")
    plt.title("Cache Hit Ratio Over Time")
    plt.show()
