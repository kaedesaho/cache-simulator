"""
Memory:
    Dictionary of lists
    - {page_num : [page]}
    - Index in the list -> Location in the page
"""

class Memory:
    def __init__(self, ram_size, page_size):
        self.page_size = page_size
        self.num_pages = ram_size // page_size
        self.pages = {i : [0] * self.page_size for i in range(self.num_pages)}

    def access(self, address):
        page_num = address // self.page_size
        offset = address % self.page_size
        return self.pages[page_num][offset]