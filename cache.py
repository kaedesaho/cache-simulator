"""
Cache:
    Dictionary of lists of objects
    - {set_num : [Line object]}
    - Index in the list -> Line number
"""


class Line:
    def __init__(self, page_size):
        self.tag = None
        self.valid = False
        self.last_used = 0
        self.data = [0] * page_size

class CacheSet:
    def __init__(self, num_sets, lines_per_set, page_size):
        self.num_sets = num_sets
        self.lines_per_set = lines_per_set
        self.sets = {i: [Line(page_size) for _ in range(lines_per_set)] for i in range(num_sets)}

    def fill_line(self, line, tag, data, time_stamp):
        line.valid = True
        line.tag = tag
        line.data = data
        line.last_used = time_stamp

    def insert(self, page_num, data, time_stamp):
        tag = page_num // self.num_sets
        block = page_num % self.num_sets

        lines = self.sets[block]

        for line in lines:
            if not line.valid:
                self.fill_line(line, tag, data, time_stamp)
                return

        replace = min(lines, key=lambda l: l.last_used)

        self.fill_line(replace, tag, data, time_stamp)

    def access(self, page_num, time_stamp):
        tag = page_num // self.num_sets
        block = page_num % self.num_sets

        for line in self.sets[block]:
            if line.valid and line.tag == tag:
                line.last_used = time_stamp
                return True

        return False
