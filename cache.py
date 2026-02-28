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
        self.num_used = 0
        self.data = [0] * page_size

class Cache:
    def __init__(self, num_sets, lines_per_set, page_size):
        self.num_sets = num_sets
        self.lines_per_set = lines_per_set
        self.sets = {i : [Line(page_size) for _ in range(lines_per_set)] for i in range(num_sets)}

    def access(self, page_num, time_stamp):
        tag = 
        block =

        # Check cache hit
        for line in self.sets[block]:
            if line.valid and line.tag == tag:
                line.last_used = time_stamp
                return True
            
        # Handle cache miss

            # Call function to handle 
        
        return False

